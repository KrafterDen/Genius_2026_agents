# Optional local runner and validation

The prompts work without this tool: bootstrap00 → AUTOPILOT, then RESUME as needed. The runner is an optional explicit local process loop that gives each later block a fresh Codex context. It is not a hosted/background service and does not run unless the user starts it. Existing Codex usage/plan limits apply; no new paid account is created.

## Validate the pack
From the project parent directory (Python3.11+ for complete TOML checks):
```bash
python TextileRoute_Codex_Prompt_Pack/tools/validate_pack.py
python -m unittest discover -s TextileRoute_Codex_Prompt_Pack/tools/tests -v
```
These tests cover this package and runner contracts. They do not train a model or test your installed Codex/account.

## Bootstrap before any actual run
Run prompt00 interactively. It must verify your actual CLI/version/flags/model availability and web research, perform a harmless invocation, and save `.agent/runtime/runner_config.json` using `repository_template/runner_config.example.json` only as a proposal. It must add real validation evidence paths and the exact `codex --version` output. Do not manually turn `validated` to true without the checks. Do not bypass permissions if noninteractive approval is unavailable; use the interactive workflow or adjust permitted settings with explicit user consent.

## Dry-run example
Run from the initialized project root:
```bash
python TextileRoute_Codex_Prompt_Pack/tools/run_blocks.py --repo . --from-block 1 --to-block 19
```
No agents are launched by default and the dry run does not write state.

## Explicit execution
Only after validated bootstrap and deliberate user authorization:
```bash
python TextileRoute_Codex_Prompt_Pack/tools/run_blocks.py --repo . --from-block 1 --to-block 19 --execute
```
For a smaller authorized batch add `--max-blocks 2`. Safety upper bound per invocation defaults to360 minutes and can be changed with `--timeout-minutes`. This is not a forced minimum; the runner never sleeps to make a block last three hours. Actual timing and the agent's duration report are logged separately.

The runner checks predecessor completion, current CLI version, actual artifact paths and nonempty gate evidence. A zero process exit code is not enough. A failed/blocked state stops the loop. A prior passed state is skipped only if its evidence still exists. It never sends emails, publishes or submits the project. It prevents a second runner in the same repository using a lock.

## Recovery
Use RESUME interactively to repair a failed block or re-run the explicit requested range after inspecting the failure. Do not delete a live lock. If a machine crashes, inspect process state before removing a stale `.agent/runtime/runner.lock`. On POSIX, timeout/interrupt terminates the launched process group; on Windows, nested child jobs may require separate inspection because terminating the main process cannot guarantee all descendants stopped. Never start another GPU run blindly.

Keep logs and personal information local. Config examples require adapting to the installed version, especially web-search/native-subagent capability. This package's offline tests do not prove those capabilities exist on your computer. If native subagents are unavailable, record sequential role fallback rather than claiming all requested models ran.
