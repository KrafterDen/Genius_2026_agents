"""Describe the released OpenTextile specimen metadata and mean spectra.

This is a read-only scientific inventory. It does not train or evaluate a model.
"""

import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def main(raw_dir):
    names = [
        "ground_truth_final.csv",
        "swir_mean_spectra.csv",
        "swir_mean_spectra_coordinates.csv",
        "rgb_mean_values.csv",
    ]
    tables = {name: read_csv(raw_dir / name) for name in names}
    labels = tables[names[0]]
    fibres = [key for key in labels[0] if key.endswith("[%]")]
    table_ids = {name: [row["Label"] for row in rows] for name, rows in tables.items()}
    groups = defaultdict(list)
    for row in labels:
        match = re.fullmatch(r"sample_(\d+)(?:-\d+)+", row["Label"])
        group = match.group(1) if match else "unparsed:" + row["Label"]
        groups[group].append(row["Label"])

    composition_sums = Counter()
    reported_fibres = Counter()
    profiles = {}
    for fibre, threshold, name in [
        ("Cotton [%]", 80, "JRC2024_MECH_COTTON80"),
        ("Polyester [%]", 95, "JRC2024_CHEM_POLYESTER95"),
        ("Cotton [%]", 88, "INFINITED_COTTON88_PREFERENCE"),
    ]:
        status = Counter()
        ids = defaultdict(list)
        near = defaultdict(list)
        for row in labels:
            flag = row["Unknown or outlier?"]
            if flag == "unknown":
                key = "unknown_composition"
            else:
                value = float(row[fibre]) if row[fibre] else 0.0
                key = ("flagged_outlier_" if flag == "outlier" else "unflagged_") + (
                    "above_or_at" if value >= threshold else "below"
                )
                if abs(value - threshold) <= 5:
                    near[str(value)].append(row["Label"])
            status[key] += 1
            ids[key].append(row["Label"])
        profiles[name] = {
            "fibre": fibre,
            "threshold_percent": threshold,
            "status_counts": dict(status),
            "ids_by_status": dict(ids),
            "within_five_percentage_points": dict(near),
        }

    for row in labels:
        values = [float(row[fibre]) for fibre in fibres if row[fibre]]
        composition_sums[str(sum(values))] += 1
        reported_fibres[len(values)] += 1

    spectra = tables["swir_mean_spectra.csv"]
    bands = [key for key in spectra[0] if key != "Label"]
    wavelengths = [float(key) for key in bands]
    numeric = [float(row[key]) for row in spectra for key in bands if row[key]]
    per_piece_spectral_mean = {
        row["Label"]: sum(float(row[key]) for key in bands) / len(bands)
        for row in spectra
    }
    representative_ids = [
        "sample_4-1",   # reported 100% cotton
        "sample_15-1",  # reported 100% polyester
        "sample_2-1",   # reported polyester/cotton mixture
        "sample_24-1",  # composition unknown
        "sample_14-1",  # source outlier flag
    ]
    representative = {
        specimen_id: {"mean_reflectance": per_piece_spectral_mean[specimen_id]}
        for specimen_id in representative_ids
    }
    coordinates = tables["swir_mean_spectra_coordinates.csv"]
    invalid_roi = [
        row["Label"] for row in coordinates
        if not (
            int(row["y_start"]) < int(row["y_end"])
            and int(row["x_start"]) < int(row["x_end"])
        )
    ]
    result = {
        "dataset": "OpenTextile-NIR, Zenodo record 18269172",
        "sample_rows": len(labels),
        "distinct_ids": len(set(table_ids[names[0]])),
        "physical_parent_id_groups_conservative": len(groups),
        "multi_piece_parent_groups": {key: value for key, value in groups.items() if len(value) > 1},
        "flags": dict(Counter(row["Unknown or outlier?"] or "unflagged" for row in labels)),
        "composition_sum_counts": dict(composition_sums),
        "reported_fibre_count_distribution": {str(k): v for k, v in reported_fibres.items()},
        "fibre_columns": fibres,
        "table_rows_and_id_consistency": {
            name: {
                "rows": len(ids),
                "distinct_ids": len(set(ids)),
                "missing_from_ground_truth": sorted(set(ids) - set(table_ids[names[0]])),
                "missing_from_table": sorted(set(table_ids[names[0]]) - set(ids)),
            }
            for name, ids in table_ids.items()
        },
        "swir_mean_spectra": {
            "bands": len(bands),
            "wavelength_min": min(wavelengths),
            "wavelength_max": max(wavelengths),
            "wavelength_monotone": all(a < b for a, b in zip(wavelengths, wavelengths[1:])),
            "nonempty_values": len(numeric),
            "missing_cells": len(spectra) * len(bands) - len(numeric),
            "nonfinite_values": sum(not math.isfinite(v) for v in numeric),
            "value_min": min(numeric),
            "value_max": max(numeric),
            "negative_values": sum(v < 0 for v in numeric),
            "values_over_one": sum(v > 1 for v in numeric),
            "lowest_mean_reflectance_id": min(per_piece_spectral_mean, key=per_piece_spectral_mean.get),
            "highest_mean_reflectance_id": max(per_piece_spectral_mean, key=per_piece_spectral_mean.get),
            "representative_piece_means": representative,
        },
        "invalid_swir_roi_ids": invalid_roi,
        "profiles": profiles,
        "interpretation": "Percentages are supplier-reported nominal fibre shares; empty component cells are unlisted, not chemically verified zeros. Unknown rows have no usable composition. Outlier flags are retained separately.",
    }
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main(Path(sys.argv[1]))
