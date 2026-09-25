# B00 local environment audit

Observed 2026-09-25, UTC. Commands were read-only except creating this repository's project-local `.venv/` and repository controls.

| Item | Observed result |
|---|---|
| Workspace | `/home/krafterden9/ChatGPT/Genius _ 2026`; pack at `TextileRoute_Codex_Prompt_Pack/` |
| Git | Existing `.git`, unborn HEAD; initially only the pack was untracked. No remote, commit or global configuration change made by B00. |
| OS | Arch Linux, x86_64, kernel 7.1.8-arch1-3 |
| Python | 3.14.7; standard-library-only package/control scripts; `.venv` made with `python3 -m venv .venv` |
| CPU memory | 15 GiB total, about 10 GiB available at inspection; 15 GiB swap |
| Disk | 389 GiB filesystem, 103 GiB free at inspection |
| GPU | `nvidia-smi` executable and working; NVIDIA GeForce RTX 2060, 6144 MiB VRAM, driver 610.57.04, CUDA user-mode version shown as 13.3. No GPU experiment run. |
| Network | `curl -I -L --max-time 12 https://developers.openai.com/codex/subagents` returned HTTP 200; Codex `--search` emitted actual web-search events. |
| Browser | This task's web browser/search tool opened official OpenAI documentation. Browser access is available for source verification. |
| Codex | `/usr/bin/codex`, `codex-cli 0.149.0`; CLI model support differs from desktop task support. See `docs/codex_capabilities.md`. |

## Local execution choice

No external Python packages are needed for the bootstrap. Run with `PYTHONPATH=src:. .venv/bin/python ...`; this is a local, dependency-free control environment, not an ML environment lock. Later data/model dependencies must be chosen after the dataset audit and pinned before a scientific run. No data files, labels, model fits or GPU measurements were produced here.

## Proposed research pipeline, pending gates

Verify source license and files → audit specimen and group metadata → define a sourced recycler profile and unobserved conditions → freeze splits, hypotheses and metrics → fit grouped classical baselines → calibrate and evaluate review/eligibility decisions → report measured risk, coverage and uncertainty → render local demonstration and draft materials from a verified claim ledger. The candidate 71-sample description is source metadata, not a validated count of independent evaluation units.
