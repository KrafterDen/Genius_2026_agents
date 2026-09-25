#!/usr/bin/env python3
"""Validate prompt-pack structure and checksums; no external services used."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def validate() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"Invalid JSON {path.relative_to(ROOT)}: {exc}")
    try:
        import tomllib
    except ImportError:
        errors.append("Python3.11+ is required for this complete TOML validation (runner itself supports3.10)")
    else:
        for path in ROOT.rglob("*.toml.example"):
            try:
                value = tomllib.loads(path.read_text(encoding="utf-8"))
                if path.parent.name == "agents":
                    for key in ("name", "description", "developer_instructions", "model", "model_reasoning_effort"):
                        if not value.get(key):
                            errors.append(f"Missing {key}: {path}")
            except Exception as exc:
                errors.append(f"Invalid TOML {path}: {exc}")
    blocks = json.loads((ROOT / "block_manifest.json").read_text())["blocks"]
    if [b["id"] for b in blocks] != [f"{n:02}" for n in range(20)]:
        errors.append("Expected consecutive blocks00–19")
    for b in blocks:
        path = ROOT / b["prompt"]
        if not path.is_file():
            errors.append(f"Missing prompt: {b['prompt']}")
            continue
        content = path.read_text(encoding="utf-8")
        for marker in ("## Independent web challenge", "## Acceptance gates", "## Suggested delegation", "## Meaningful depth work"):
            if marker not in content:
                errors.append(f"Missing {marker} in {path.name}")
        if len(content.split()) < 400:
            errors.append(f"Unexpectedly short work block: {path.name}")
    for name in ("prompts/AUTOPILOT.md", "prompts/RESUME.md", "prompts/CHALLENGER.md", "START_HERE_RU.md", "repository_template/AGENTS.md"):
        if not (ROOT / name).is_file():
            errors.append(f"Missing critical file {name}")
    registry = json.loads((ROOT / "sources/sources.json").read_text())["sources"]
    ids = [x["id"] for x in registry]
    if len(set(ids)) != len(ids):
        errors.append("Duplicate source IDs")
    for source in registry:
        if not source["url"].startswith("https://") or not source.get("retrieval_status"):
            errors.append(f"Invalid source {source['id']}")
    manifest = ROOT / "MANIFEST.json"
    if not manifest.is_file():
        errors.append("Missing final integrity manifest")
    else:
        data = json.loads(manifest.read_text())
        for item in data["files"]:
            p = ROOT / item["path"]
            if not p.is_file():
                errors.append(f"Missing manifest file {item['path']}")
            elif hashlib.sha256(p.read_bytes()).hexdigest() != item["sha256"]:
                errors.append(f"Checksum mismatch {item['path']}")
    return errors

if __name__ == "__main__":
    issues = validate()
    if issues:
        print("FAILED\n" + "\n".join(issues))
        raise SystemExit(1)
    print("PASS: structure, JSON, TOML,20 prompts, source IDs and integrity manifest.")
