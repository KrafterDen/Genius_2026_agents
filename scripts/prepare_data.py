#!/usr/bin/env python3
"""Prepare verified OpenTextile mean spectra locally, without downloading data."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

from textileroute.data.open_textile import DataContractError  # noqa: E402
from textileroute.data.prepare import prepare_open_textile  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=REPOSITORY_ROOT,
                        help="repository containing the audited local manifest and raw files")
    args = parser.parse_args()
    root = args.repository_root.resolve()
    try:
        hashes = prepare_open_textile(
            manifest_path=root / "data/manifests/dataset_manifest.json",
            pin_path=root / "configs/open_textile_v1_sources.json",
            raw_dir=root / "data/raw/open_textile_zenodo_18269172",
            split_plan_path=root / "protocol/split_plan.json",
            processed_dir=root / "data/processed/open_textile_v1",
            split_output_path=root / "data/splits/open_textile_v1_frozen_outer_folds.json",
            protocol_path=root / "protocol/preregistered_protocol.md",
            implementation_paths=(
                root / "src/textileroute/data/open_textile.py",
                root / "src/textileroute/data/splits.py",
                root / "src/textileroute/data/prepare.py",
                root / "src/textileroute/spectra/transforms.py",
                root / "scripts/prepare_data.py",
            ),
        )
    except (DataContractError, FileNotFoundError, PermissionError) as exc:
        print(f"preparation stopped without overriding source data: {exc}", file=sys.stderr)
        return 2
    print(json.dumps({"status": "prepared", "sha256": hashes}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
