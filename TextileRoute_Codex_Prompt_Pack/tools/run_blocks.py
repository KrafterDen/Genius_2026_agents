#!/usr/bin/env python3
"""Explicit opt-in sequential Codex runner. Standard library, Python >=3.10.

Default is a read-only dry run. It does not implement model subagents itself;
Codex does that using the repository instructions and verified native features.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone

PACK = Path(__file__).resolve().parents[1]
FORBIDDEN = ("--yolo", "--dangerously-bypass-approvals-and-sandbox", "danger-full-access")

class RunnerError(RuntimeError):
    pass

def read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise RunnerError(f"Cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RunnerError(f"Expected a JSON object: {path}")
    return value

def inside(repo: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative:
        raise RunnerError("An evidence path must be a nonempty relative string")
    p = (repo / relative).resolve()
    try:
        p.relative_to(repo.resolve())
    except ValueError as exc:
        raise RunnerError(f"Path escapes the repository: {relative}") from exc
    if Path(relative).is_absolute():
        raise RunnerError(f"Use a repository-relative evidence path: {relative}")
    return p

def verify_state(repo: Path, block_id: str) -> dict:
    state_path = repo / ".agent" / "blocks" / f"{block_id}.json"
    state = read_json(state_path)
    if state.get("block_id") != block_id or state.get("status") != "passed":
        raise RunnerError(f"Block {block_id} has not passed: {state.get('status')}")
    for key in ("started_at", "ended_at", "next_action"):
        if not isinstance(state.get(key), str) or not state[key]:
            raise RunnerError(f"Block {block_id}: missing {key}")
    elapsed = state.get("elapsed_minutes")
    if isinstance(elapsed, bool) or not isinstance(elapsed, (int, float)) or elapsed < 0:
        raise RunnerError(f"Block {block_id}: invalid measured elapsed_minutes")
    if elapsed < 180 and not state.get("under_target_reason"):
        raise RunnerError(f"Block {block_id}: record an honest under_target_reason; do not pad time")
    gates, evidence = state.get("gates"), state.get("evidence")
    if not isinstance(gates, list) or not gates or not isinstance(evidence, list) or not evidence:
        raise RunnerError(f"Block {block_id}: missing gates/evidence")
    for gate in gates:
        if not isinstance(gate, dict) or gate.get("passed") is not True or not gate.get("name"):
            raise RunnerError(f"Block {block_id}: an acceptance gate failed or is missing")
        p = inside(repo, gate.get("evidence_path", ""))
        if not p.is_file() or p.stat().st_size == 0:
            raise RunnerError(f"Missing/non-file gate evidence: {p}")
    for item in evidence:
        p = inside(repo, item)
        if not p.is_file() or p.stat().st_size == 0:
            raise RunnerError(f"Missing/non-file evidence: {p}")
    return state

def validate_config(repo: Path, config: dict) -> list[str]:
    if config.get("validated") is not True:
        raise RunnerError("Bootstrap has not validated the runner configuration")
    if config.get("web_search_verified") is not True:
        raise RunnerError("Verified web research capability is required; do not substitute memory")
    version = config.get("validated_for_codex_version")
    if not isinstance(version, str) or not version.strip():
        raise RunnerError("Missing actual validated Codex version")
    evidence = config.get("validation_evidence_paths", [])
    if not evidence:
        raise RunnerError("Missing real configuration validation evidence")
    for relative in evidence:
        p = inside(repo, relative)
        if not p.is_file() or p.stat().st_size == 0:
            raise RunnerError(f"Missing validation evidence: {p}")
    argv = config.get("command_template")
    if not isinstance(argv, list) or not argv or any(not isinstance(x, str) for x in argv):
        raise RunnerError("command_template must be a nonempty string array")
    binary = Path(argv[0]).name.lower()
    if binary not in {"codex", "codex.exe"}:
        raise RunnerError("Command must invoke a validated codex binary directly, without a shell")
    joined = " ".join(argv)
    if any(flag in joined for flag in FORBIDDEN):
        raise RunnerError("Permission-bypass configuration is forbidden")
    if "exec" not in argv or "-" not in argv or "{last_message}" not in joined:
        raise RunnerError("Validate a codex exec template with stdin '-' and a last-message path")
    # cwd is fixed by this runner. A template must not redirect work elsewhere.
    for i, token in enumerate(argv):
        if token in {"--cd", "-C"} and (i + 1 >= len(argv) or argv[i + 1] != "{repo}"):
            raise RunnerError("An explicit working-directory argument must use {repo}")
        if token.startswith("--cd=") and token != "--cd={repo}":
            raise RunnerError("An explicit working directory must be {repo}")
    return argv

def block_prompt(repo: Path, block: dict) -> str:
    rel = block["prompt"]
    path = inside(PACK, rel)
    if not path.is_file():
        raise RunnerError(f"Prompt missing: {path}")
    return (
        "Execute the following ONE work block in this repository. Read existing AGENTS.md and durable state first.\n"
        f"Repository: {repo}\nPrompt pack: {PACK}\n"
        "This invocation is controlled by an external sequential runner. Do not start another runner, "
        "do not continue into subsequent blocks, and do not bypass any permissions. Save actual evidence "
        "and the block state before exiting. Failed/missing scientific dependencies must remain blocked.\n\n"
        + path.read_text(encoding="utf-8")
    )

def terminate_process(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        return
    try:
        if os.name == "posix":
            os.killpg(proc.pid, signal.SIGTERM)
        else:
            proc.terminate()
        proc.wait(timeout=10)
    except (ProcessLookupError, subprocess.TimeoutExpired):
        if proc.poll() is None:
            if os.name == "posix":
                os.killpg(proc.pid, signal.SIGKILL)
            else:
                proc.kill()
            proc.wait()

def invoke(argv: list[str], prompt: str, repo: Path, log: Path, timeout_seconds: float) -> int:
    kwargs = {"start_new_session": True} if os.name == "posix" else {}
    with log.open("w", encoding="utf-8") as output:
        proc = subprocess.Popen(argv, cwd=repo, stdin=subprocess.PIPE, stdout=output,
                                stderr=subprocess.STDOUT, text=True, encoding="utf-8", **kwargs)
        try:
            proc.communicate(prompt, timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            terminate_process(proc)
            raise RunnerError("Block timeout; process stopped. Inspect partial run logs before resuming.")
        except KeyboardInterrupt:
            terminate_process(proc)
            raise
    return int(proc.returncode)

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--config", type=Path, help="Default: <repo>/.agent/runtime/runner_config.json")
    parser.add_argument("--from-block", type=int, default=1)
    parser.add_argument("--to-block", type=int, default=19)
    parser.add_argument("--max-blocks", type=int, default=19, help="Cap actual invocations")
    parser.add_argument("--timeout-minutes", type=float, default=360, help="Safety upper bound, never a minimum")
    parser.add_argument("--execute", action="store_true", help="Explicitly authorize local Codex invocations")
    args = parser.parse_args(argv)
    repo = args.repo.resolve()
    if not repo.is_dir():
        raise RunnerError(f"Repository directory does not exist: {repo}")
    if not (1 <= args.from_block <= args.to_block <= 19):
        raise RunnerError("Run bootstrap00 interactively first; choose block range01–19")
    if args.max_blocks < 1 or args.timeout_minutes <= 0:
        raise RunnerError("Positive invocation cap and timeout required")
    blocks = read_json(PACK / "block_manifest.json")["blocks"]
    selected = [b for b in blocks if args.from_block <= int(b["id"]) <= args.to_block]
    print("Mode:", "EXECUTE (uses your existing Codex account/limits)" if args.execute else "DRY RUN — no agents launched")
    for b in selected:
        print(f"{b['id']}: {b['title']}")
    if not args.execute:
        print("Run00 first; inspect tools/README.md and validate local CLI arguments before --execute.")
        return 0
    if not (repo / "AGENTS.md").is_file():
        raise RunnerError("Missing root AGENTS.md; initialize first")
    verify_state(repo, "00")
    config = read_json(args.config.resolve() if args.config else repo / ".agent/runtime/runner_config.json")
    command = validate_config(repo, config)
    check = subprocess.run([command[0], "--version"], cwd=repo, capture_output=True,
                           text=True, encoding="utf-8", timeout=30, check=False)
    observed = (check.stdout or check.stderr).strip()
    if check.returncode != 0 or observed != config["validated_for_codex_version"].strip():
        raise RunnerError("Codex version differs from validated version; revalidate configuration, do not guess")
    runtime = repo / ".agent/runtime"
    runtime.mkdir(parents=True, exist_ok=True)
    lock = runtime / "runner.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise RunnerError("Runner lock exists. Check for a live process before manually removing a stale lock.") from exc
    with os.fdopen(fd, "w") as f:
        f.write(str(os.getpid()))
    completed = 0
    try:
        for b in selected:
            state_path = repo / ".agent/blocks" / f"{b['id']}.json"
            if state_path.is_file() and read_json(state_path).get("status") == "passed":
                verify_state(repo, b["id"])
                print(f"Skipping evidenced completed block {b['id']}")
                continue
            for dependency in b["dependencies"]:
                verify_state(repo, dependency)
            if completed >= args.max_blocks:
                print("Invocation cap reached; checkpoint retained.")
                break
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
            last = runtime / f"{b['id']}_{stamp}_last.md"
            log = runtime / f"{b['id']}_{stamp}_process.log"
            substitutions = {"{repo}": str(repo), "{last_message}": str(last)}
            actual = command[:]
            for i, token in enumerate(actual):
                for before, after in substitutions.items():
                    token = token.replace(before, after)
                actual[i] = token
            start = time.monotonic()
            print(f"Starting block {b['id']}; log: {log}", flush=True)
            code = invoke(actual, block_prompt(repo, b), repo, log, args.timeout_minutes * 60)
            elapsed = (time.monotonic() - start) / 60
            event = {"block_id": b["id"], "ended_at": datetime.now(timezone.utc).isoformat(),
                     "wall_minutes": round(elapsed, 3), "exit_code": code,
                     "process_log": str(log.relative_to(repo)), "last_message": str(last.relative_to(repo))}
            with (runtime / "runner_events.jsonl").open("a", encoding="utf-8") as out:
                out.write(json.dumps(event) + "\n")
            if code != 0:
                raise RunnerError(f"Codex block {b['id']} exited {code}; inspect logs and resume deliberately")
            verify_state(repo, b["id"])
            completed += 1
            print(f"Block {b['id']} evidenced complete; actual invocation wall time {elapsed:.1f} minutes.")
        print("Runner finished its requested scope. No project has been automatically submitted or published.")
        return 0
    finally:
        lock.unlink(missing_ok=True)

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RunnerError, OSError, subprocess.SubprocessError) as exc:
        print(f"STOP: {exc}", file=sys.stderr)
        raise SystemExit(2)
    except KeyboardInterrupt:
        print("Interrupted. Inspect partial jobs before RESUME.", file=sys.stderr)
        raise SystemExit(130)
