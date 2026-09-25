"""Strict, read-only parser for the audited OpenTextile-NIR v1.0 small files.

Nominal supplier shares are never represented as chemical measurements. Raw files
are verified against the local record manifest before any content is parsed.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path


FIBRE_COLUMNS = (
    "Polyamide [%]",
    "Viscose [%]",
    "Lyocell [%]",
    "Modacrylic [%]",
    "Polyacrylic [%]",
    "Wool [%]",
    "Carbon fibre [%]",
    "Polyurethane [%]",
    "Elastane [%]",
    "Polyester [%]",
    "Cotton [%]",
)
COMPOSITION_COLUMNS = (
    "Label",
    "Unknown or outlier?",
    *FIBRE_COLUMNS,
    "Color",
    "Texture",
    "Extra information",
)
REQUIRED_FILES = (
    "ground_truth_final.csv",
    "swir_mean_spectra.csv",
    "swir_mean_spectra_coordinates.csv",
    "rgb_mean_values.csv",
)
PIECE_ID = re.compile(r"^sample_(\d+)-\d+(?:-\d+)?$")


class DataContractError(ValueError):
    """A source file or field does not match the audited release contract."""


@dataclass(frozen=True)
class Piece:
    piece_id: str
    parent_group_id: str
    label_status: str  # nominal, source_residual_outlier, or unknown
    reported_percent: tuple[tuple[str, float], ...]
    spectrum_reflectance: tuple[float, ...]
    swir_roi: tuple[int, int, int, int]
    rgb_mean: tuple[float, float, float]
    color: str
    texture: str
    extra_information: str

    def nominal_percent(self, fibre_column: str) -> float | None:
        """Return a nominal component of a complete row, never chemical truth."""
        if fibre_column not in FIBRE_COLUMNS:
            raise DataContractError(f"unsupported fibre column: {fibre_column}")
        if self.label_status == "unknown":
            return None
        return dict(self.reported_percent).get(fibre_column, 0.0)

    @property
    def author_defined_natural_share(self) -> float | None:
        if self.label_status == "unknown":
            return None
        return sum(
            self.nominal_percent(name) or 0.0
            for name in ("Cotton [%]", "Wool [%]", "Lyocell [%]")
        )


@dataclass(frozen=True)
class OpenTextileData:
    doi: str
    license_id: str
    wavelengths_nm: tuple[float, ...]
    pieces: tuple[Piece, ...]
    verified_source_sha256: tuple[tuple[str, str], ...]


def _digest(path: Path, algorithm: str) -> str:
    h = hashlib.new(algorithm)
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _verified_paths(manifest_path: Path, pin_path: Path, raw_dir: Path) -> tuple[dict[str, Path], dict]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    primary = manifest.get("primary", {})
    pin = json.loads(pin_path.read_text(encoding="utf-8"))
    if primary.get("doi") != "10.5281/zenodo.18269172" or pin.get("dataset_doi") != primary.get("doi"):
        raise DataContractError("manifest is not the audited OpenTextile record")
    if (primary.get("version") != "1.0" or primary.get("license") != "CC-BY-4.0"
            or pin.get("version") != primary.get("version")
            or pin.get("license") != primary.get("license")):
        raise DataContractError("unsupported OpenTextile version or license")
    by_name = {entry["name"]: entry for entry in primary.get("files", [])}
    pins = pin.get("required_files", {})
    if set(pins) != set(REQUIRED_FILES):
        raise DataContractError("source pin does not list the exact required small files")
    result: dict[str, Path] = {}
    for name in REQUIRED_FILES:
        entry = by_name.get(name)
        expected = pins[name]
        if entry is None or entry.get("retrieval_status") != "retrieved_hash_verified":
            raise DataContractError(f"required verified file missing from manifest: {name}")
        if (entry.get("source_size_bytes") != expected["size_bytes"]
                or entry.get("source_md5") != expected["source_md5"]
                or entry.get("local_sha256") != expected["local_sha256"]):
            raise DataContractError(f"local manifest disagrees with tracked source pin: {name}")
        path = raw_dir / name
        if not path.is_file():
            raise DataContractError(f"required raw file missing: {path}")
        if path.stat().st_size != entry.get("source_size_bytes"):
            raise DataContractError(f"source size changed: {name}")
        if _digest(path, "md5") != entry.get("source_md5"):
            raise DataContractError(f"source MD5 mismatch: {name}")
        if _digest(path, "sha256") != entry.get("local_sha256"):
            raise DataContractError(f"local SHA-256 mismatch: {name}")
        result[name] = path
    return result, primary


def _read_table(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, delimiter=";")
        header = reader.fieldnames
        if header is None or len(header) != len(set(header)):
            raise DataContractError(f"missing or duplicate header: {path.name}")
        rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise DataContractError(f"malformed semicolon row: {path.name}")
    ids = [row["Label"] for row in rows] if "Label" in header else []
    if len(ids) != len(set(ids)):
        raise DataContractError(f"duplicate piece ID in {path.name}")
    return header, rows


def _finite(value: str, context: str) -> float:
    try:
        parsed = float(value)
    except ValueError as exc:
        raise DataContractError(f"non-numeric {context}: {value!r}") from exc
    if not math.isfinite(parsed):
        raise DataContractError(f"non-finite {context}")
    return parsed


def _parse_composition(row: dict[str, str]) -> tuple[str, tuple[tuple[str, float], ...]]:
    flag = row["Unknown or outlier?"]
    if flag not in ("", "unknown", "outlier"):
        raise DataContractError(f"unsupported label flag for {row['Label']}: {flag!r}")
    reported = []
    for name in FIBRE_COLUMNS:
        value = row[name]
        if not value:
            continue
        share = _finite(value, f"{row['Label']} {name}")
        if share < 0 or share > 100:
            raise DataContractError(f"composition outside [0,100]: {row['Label']} {name}")
        reported.append((name, share))
    total = sum(value for _, value in reported)
    if flag == "unknown":
        if reported:
            raise DataContractError(f"unknown composition has values: {row['Label']}")
        return "unknown", ()
    if not reported or not math.isclose(total, 100.0, abs_tol=1e-6):
        raise DataContractError(f"nominal composition does not total 100: {row['Label']}")
    return ("source_residual_outlier" if flag == "outlier" else "nominal"), tuple(reported)


def load_verified_open_textile(manifest_path: Path, pin_path: Path, raw_dir: Path) -> OpenTextileData:
    """Verify source bytes and parse the audited mean-spectrum release, without fitting."""
    paths, source_record = _verified_paths(manifest_path, pin_path, raw_dir)
    composition_header, composition_rows = _read_table(paths["ground_truth_final.csv"])
    spectrum_header, spectrum_rows = _read_table(paths["swir_mean_spectra.csv"])
    coordinate_header, coordinate_rows = _read_table(paths["swir_mean_spectra_coordinates.csv"])
    rgb_header, rgb_rows = _read_table(paths["rgb_mean_values.csv"])
    if tuple(composition_header) != COMPOSITION_COLUMNS:
        raise DataContractError("composition columns differ from audited v1.0 schema")
    if tuple(coordinate_header) != ("Label", "y_start", "y_end", "x_start", "x_end"):
        raise DataContractError("SWIR coordinate columns differ from audited schema")
    if tuple(rgb_header) != ("Label", "R", "G", "B"):
        raise DataContractError("RGB mean columns differ from audited schema")
    if len(spectrum_header) != 289 or spectrum_header[0] != "Label":
        raise DataContractError("expected Label plus 288 wavelength columns")
    wavelengths = tuple(_finite(value, "wavelength header") for value in spectrum_header[1:])
    if (not all(a < b for a, b in zip(wavelengths, wavelengths[1:]))
            or not math.isclose(wavelengths[0], 953.04, abs_tol=0.01)
            or not math.isclose(wavelengths[-1], 2547.64, abs_tol=0.01)):
        raise DataContractError("unsupported wavelength order/range; expected audited nm grid")
    if len(composition_rows) != 71:
        raise DataContractError("expected 71 physical piece rows in v1.0")
    expected_ids = {row["Label"] for row in composition_rows}
    tables = (spectrum_rows, coordinate_rows, rgb_rows)
    if any({row["Label"] for row in rows} != expected_ids for rows in tables):
        raise DataContractError("piece IDs disagree across source tables")
    spectrum_by_id = {row["Label"]: row for row in spectrum_rows}
    coordinate_by_id = {row["Label"]: row for row in coordinate_rows}
    rgb_by_id = {row["Label"]: row for row in rgb_rows}
    pieces = []
    for row in composition_rows:
        piece_id = row["Label"]
        match = PIECE_ID.fullmatch(piece_id)
        if match is None:
            raise DataContractError(f"unsupported piece ID: {piece_id}")
        status, reported = _parse_composition(row)
        spectrum = tuple(
            _finite(spectrum_by_id[piece_id][column], f"{piece_id} spectrum")
            for column in spectrum_header[1:]
        )
        if any(value < 0 or value > 1 for value in spectrum):
            raise DataContractError(
                f"reflectance outside audited fractional [0,1] scale in {piece_id}; inspect source"
            )
        try:
            bounds = tuple(int(coordinate_by_id[piece_id][key])
                           for key in ("y_start", "y_end", "x_start", "x_end"))
        except ValueError as exc:
            raise DataContractError(f"non-integer SWIR ROI for {piece_id}") from exc
        if min(bounds) < 0 or bounds[0] >= bounds[1] or bounds[2] >= bounds[3]:
            raise DataContractError(f"invalid SWIR ROI for {piece_id}")
        rgb = tuple(_finite(rgb_by_id[piece_id][key], f"{piece_id} RGB mean")
                    for key in ("R", "G", "B"))
        if any(value < 0 or value > 255 for value in rgb):
            raise DataContractError(f"RGB mean outside [0,255] for {piece_id}")
        pieces.append(Piece(
            piece_id=piece_id,
            parent_group_id=match.group(1),
            label_status=status,
            reported_percent=reported,
            spectrum_reflectance=spectrum,
            swir_roi=bounds,
            rgb_mean=rgb,
            color=row["Color"],
            texture=row["Texture"],
            extra_information=row["Extra information"],
        ))
    source_hashes = tuple(
        (name, next(entry["local_sha256"] for entry in source_record["files"]
                    if entry["name"] == name))
        for name in REQUIRED_FILES
    )
    return OpenTextileData(
        doi=source_record["doi"],
        license_id=source_record["license"],
        wavelengths_nm=wavelengths,
        pieces=tuple(pieces),
        verified_source_sha256=source_hashes,
    )
