#!/usr/bin/env python3
"""Validate resumable repository controls without third-party dependencies."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import re
import sys

STATES = {"not_started", "in_progress", "passed", "blocked", "needs_revision"}
CLI_VERIFIED_MODELS = {"gpt-5.6-sol", "gpt-5.6-luna"}
EXPECTED = (
    "AGENTS.md", "PROJECT.md", "PLANS.md", "STATUS.json", "NEXT.md",
    "HUMAN_ACTIONS.md", ".agent/tasks.json", ".agent/execplans/B00.md",
    ".agent/blocks/00.json", ".agent/block_reports/B00.md",
    "docs/environment_audit.md", "docs/codex_capabilities.md",
    "scripts/smoke.py", "src/textileroute/__init__.py",
    "research/sources.jsonl", "research/claims.csv", "research/search_log.jsonl",
    "TextileRoute_Codex_Prompt_Pack/START_HERE_RU.md",
)


class ValidationError(ValueError):
    pass


def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ValidationError(f"invalid JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError(f"expected JSON object: {path}")
    return value


def evidence_path(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValidationError(f"evidence path must be repository-relative: {relative!r}")
    path = (root / relative).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError as exc:
        raise ValidationError(f"evidence path escapes repository: {relative}") from exc
    return path


def require_evidence(root: Path, relative: str) -> None:
    path = evidence_path(root, relative)
    if not path.is_file() or path.stat().st_size == 0:
        raise ValidationError(f"missing or empty evidence: {relative}")


def validate_state(root: Path, state: dict, filename_id: str) -> None:
    if state.get("block_id") != filename_id or not re.fullmatch(r"\d{2}", filename_id):
        raise ValidationError(f"block ID mismatch in {filename_id}.json")
    status = state.get("status")
    if status not in STATES:
        raise ValidationError(f"invalid status for block {filename_id}: {status!r}")
    if not isinstance(state.get("gates"), list) or not isinstance(state.get("evidence"), list):
        raise ValidationError(f"block {filename_id} needs gates and evidence arrays")
    if not isinstance(state.get("next_action"), str) or not state["next_action"].strip():
        raise ValidationError(f"block {filename_id} needs an exact next_action")
    if status == "passed":
        if not state.get("started_at") or not state.get("ended_at"):
            raise ValidationError(f"passed block {filename_id} lacks timestamps")
        minutes = state.get("elapsed_minutes")
        if isinstance(minutes, bool) or not isinstance(minutes, (int, float)) or minutes < 0:
            raise ValidationError(f"passed block {filename_id} lacks measured duration")
        if minutes < 180 and not state.get("under_target_reason"):
            raise ValidationError(f"block {filename_id} needs honest under-target reason")
        if not state["gates"] or not state["evidence"]:
            raise ValidationError(f"passed block {filename_id} lacks acceptance evidence")
    for gate in state["gates"]:
        if not isinstance(gate, dict) or not gate.get("name") or not isinstance(gate.get("passed"), bool):
            raise ValidationError(f"malformed gate in block {filename_id}")
        if status == "passed" and not gate["passed"]:
            raise ValidationError(f"failed gate in passed block {filename_id}")
        if gate["passed"]:
            require_evidence(root, gate.get("evidence_path"))
    if status == "passed":
        for relative in state["evidence"]:
            require_evidence(root, relative)


def validate_tasks(tasks: dict, root: Path | None = None) -> None:
    entries = tasks.get("tasks")
    if not isinstance(entries, list):
        raise ValidationError("tasks must be an array")
    seen: set[str] = set()
    active_writers: dict[str, str] = {}
    for task in entries:
        if not isinstance(task, dict) or not isinstance(task.get("id"), str):
            raise ValidationError("malformed task")
        task_id = task["id"]
        if task_id in seen:
            raise ValidationError(f"duplicate task ID: {task_id}")
        seen.add(task_id)
        if task.get("status") not in STATES:
            raise ValidationError(f"invalid task status: {task_id}")
        if task["status"] == "passed":
            if task.get("passed") is not True or not task.get("evidence"):
                raise ValidationError(f"passed task lacks verified evidence: {task_id}")
            if root:
                for relative in task["evidence"]:
                    require_evidence(root, relative)
        elif task.get("passed") is not False:
            raise ValidationError(f"incomplete task pre-passed: {task_id}")
        if task["status"] == "in_progress":
            for scope in task.get("write_scope", []):
                if not isinstance(scope, str) or not scope or Path(scope).is_absolute() or ".." in Path(scope).parts:
                    raise ValidationError(f"invalid write scope: {scope!r}")
                for owned, owner in active_writers.items():
                    if scope == owned or scope.startswith(owned.rstrip("/") + "/") or owned.startswith(scope.rstrip("/") + "/"):
                        raise ValidationError(f"conflicting writers for {scope}: {owner}, {task_id}")
                active_writers[scope] = task_id


def assess_attempt(*, stopped: bool, command_exit: int | None, model: str,
                   network_available: bool, needs_network: bool,
                   available_models: set[str] | None = None) -> str:
    """A local execution may pass only with an observed successful command and prerequisites."""
    if available_models is None:
        available_models = CLI_VERIFIED_MODELS
    if stopped or model not in available_models or (needs_network and not network_available):
        return "blocked"
    if command_exit is None:
        return "blocked"
    if command_exit != 0:
        return "needs_revision"
    return "passed"


def validate_sources(root: Path) -> None:
    seed = read_json(root / "TextileRoute_Codex_Prompt_Pack/sources/sources.json")
    ids = [item["id"] for item in seed.get("sources", [])]
    if not ids or len(ids) != len(set(ids)):
        raise ValidationError("seed source IDs missing or duplicated")
    records = []
    for line in (root / "research/sources.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    observed = [item.get("id") for item in records]
    if observed != ids:
        raise ValidationError("source register differs from immutable seed IDs/order")
    if any(not item.get("url") or not item.get("retrieval_status") for item in records):
        raise ValidationError("source register lacks URL/retrieval status")
    with (root / "research/claims.csv").open(newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        if not {"claim_id", "source_ids", "status"}.issubset(rows.fieldnames or []):
            raise ValidationError("claims register lacks required columns")
        for row in rows:
            for source_id in row["source_ids"].split(";"):
                if source_id and source_id not in ids:
                    raise ValidationError(f"unknown claim source ID: {source_id}")


def validate_repository(root: Path, required_block: str | None = None) -> None:
    root = root.resolve()
    for relative in EXPECTED:
        require_evidence(root, relative)
    status = read_json(root / "STATUS.json")
    if status.get("schema_version") != 1 or status.get("project") != "TextileRoute":
        raise ValidationError("invalid project STATUS schema")
    if status.get("submission_ready") is not False or status.get("student_contribution_verified") is not False:
        raise ValidationError("bootstrap cannot mark release or student contribution verified")
    blocks = sorted((root / ".agent/blocks").glob("[0-9][0-9].json"))
    if len(blocks) != 20:
        raise ValidationError("expected one state for each block 00-19")
    for block in blocks:
        validate_state(root, read_json(block), block.stem)
    if required_block and read_json(root / f".agent/blocks/{required_block}.json").get("status") != "passed":
        raise ValidationError(f"required block {required_block} has not passed")
    if status.get("active_block") not in {f"{i:02d}" for i in range(20)}:
        raise ValidationError("STATUS active_block is invalid")
    if not (root / ".agent/execplans" / f"B{status['active_block']}.md").is_file():
        raise ValidationError("active block has no ExecPlan")
    if not isinstance(status.get("next_action"), str) or not status["next_action"].strip():
        raise ValidationError("STATUS has no next_action")
    validate_tasks(read_json(root / ".agent/tasks.json"), root)
    validate_sources(root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--require-block", choices=[f"{i:02d}" for i in range(20)])
    args = parser.parse_args()
    try:
        validate_repository(args.repo, args.require_block)
    except (ValidationError, OSError, KeyError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2
    print("PASS: repository controls, states, sources, evidence paths and ownership")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
