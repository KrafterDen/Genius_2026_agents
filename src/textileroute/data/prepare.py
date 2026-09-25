"""Deterministic local serialization of audited means and the frozen group map."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path

from .open_textile import DataContractError, load_verified_open_textile
from .splits import load_frozen_group_split


def _canonical_json(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=False,
                       separators=(",", ":")) + "\n").encode("utf-8")


def _hash_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _write_once(path: Path, content: bytes) -> str:
    """Publish complete bytes once; never overwrite a concurrently created file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    expected_hash = _hash_bytes(content)
    if path.exists() or path.is_symlink():
        if path.is_symlink() or not path.is_file() or _hash_bytes(path.read_bytes()) != expected_hash:
            raise DataContractError(f"existing derived file differs; keep it for audit: {path}")
        return expected_hash
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.",
                                         suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError:
            if path.is_symlink() or not path.is_file() or _hash_bytes(path.read_bytes()) != expected_hash:
                raise DataContractError(f"derived file appeared with different content: {path}")
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    return expected_hash


def prepare_open_textile(
    manifest_path: Path,
    pin_path: Path,
    raw_dir: Path,
    split_plan_path: Path,
    processed_dir: Path,
    split_output_path: Path,
    protocol_path: Path,
    repository_root: Path,
    implementation_paths: tuple[str, ...],
) -> dict[str, str]:
    """Hash-check inputs and write source-valued JSON; never train a model."""
    data = load_verified_open_textile(manifest_path, pin_path, raw_dir)
    split = load_frozen_group_split(split_plan_path, data)
    if len(implementation_paths) != len(set(implementation_paths)) or any(
        Path(relative_path).is_absolute() or ".." in Path(relative_path).parts
        for relative_path in implementation_paths
    ):
        raise DataContractError("implementation source paths must be unique and repository-relative")
    protocol_hash = hashlib.sha256(protocol_path.read_bytes()).hexdigest()
    if protocol_hash != "65ed47e79118e45a8d46453f3b5cb53993558e2b8f8157ddc597e3b73cc8dfd7":
        raise DataContractError("B04 frozen protocol hash changed; amend before preparation")
    wavelengths_bytes = _canonical_json({
        "unit": "nm",
        "representation": "source_mean_swir_reflectance",
        "wavelengths": data.wavelengths_nm,
    })
    spectrum_lines = []
    metadata_lines = []
    fold_by_piece = dict(split.fold_by_piece)
    for piece in data.pieces:
        spectrum_lines.append(_canonical_json({
            "piece_id": piece.piece_id,
            "spectrum_reflectance": piece.spectrum_reflectance,
        }).rstrip(b"\n"))
        metadata_lines.append(_canonical_json({
            "piece_id": piece.piece_id,
            "parent_group_id": piece.parent_group_id,
            "outer_fold": fold_by_piece[piece.piece_id],
            "label_status": piece.label_status,
            "reported_percent": dict(piece.reported_percent),
            "author_defined_natural_share_nominal": piece.author_defined_natural_share,
            "swir_roi_y_start_y_end_x_start_x_end": piece.swir_roi,
            "rgb_mean_context_only": piece.rgb_mean,
            "color_context_only": piece.color,
            "texture_context_only": piece.texture,
            "extra_information": piece.extra_information,
        }).rstrip(b"\n"))
    spectra_bytes = b"\n".join(spectrum_lines) + b"\n"
    metadata_bytes = b"\n".join(metadata_lines) + b"\n"
    split_bytes = _canonical_json({
        "schema_version": 1,
        "source_plan": split.source_protocol,
        "source_plan_sha256": hashlib.sha256(split_plan_path.read_bytes()).hexdigest(),
        "fold_count": split.fold_count,
        "group_fold": dict(split.fold_by_parent_group),
        "piece_fold": dict(split.fold_by_piece),
        "note": "internal exploratory outer folds only; no confirmatory final set",
    })
    hashes = {
        "wavelengths_nm.json": _write_once(processed_dir / "wavelengths_nm.json", wavelengths_bytes),
        "spectra.jsonl": _write_once(processed_dir / "spectra.jsonl", spectra_bytes),
        "metadata.jsonl": _write_once(processed_dir / "metadata.jsonl", metadata_bytes),
        "frozen_outer_folds.json": _write_once(split_output_path, split_bytes),
    }
    provenance_bytes = _canonical_json({
        "schema_version": 1,
        "source_doi": data.doi,
        "source_license": data.license_id,
        "source_sha256": dict(data.verified_source_sha256),
        "protocol_sha256": protocol_hash,
        "source_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "tracked_source_pin_sha256": hashlib.sha256(pin_path.read_bytes()).hexdigest(),
        "implementation_sha256": {
            relative_path: hashlib.sha256((repository_root / relative_path).read_bytes()).hexdigest()
            for relative_path in implementation_paths
        },
        "derived_sha256": hashes,
        "physical_piece_count": len(data.pieces),
        "parent_group_count": len(split.fold_by_parent_group),
        "nominal_label_piece_count": sum(piece.label_status != "unknown" for piece in data.pieces),
        "model_fitted": False,
        "performance_result": None,
    })
    hashes["provenance.json"] = _write_once(processed_dir / "provenance.json", provenance_bytes)
    return hashes
