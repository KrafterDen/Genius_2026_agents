# Work-block execution contract

The numbered prompts define substantial research/engineering packages sized for a **180–240 minute productive session**. This is a planning allocation, not a minimum-duration trick. Do not sleep, repeatedly browse, generate irrelevant files or rerun equivalent experiments just to reach 180 minutes. Start with the core tasks; when they finish rapidly, execute the block's genuinely useful depth work. If all useful work is done sooner, record actual time and an honest under-target reason. Parallel worker-minutes are not elapsed wall time.

## Start
Read scoped instructions/state; inspect git status and pending work; verify prerequisites. Create or update `.agent/execplans/Bxx.md` with objective, evidence, milestones, tests, risks, suggested workers, dependencies and rollback. Record an ISO timestamp and pre-run revision. Use read-only/restricted workers unless a task needs writes. Do not merely output a plan: execute this block.

## During
Keep the active plan current, save meaningful checkpoints and use actual tool output. Track allocated workers and expensive jobs. Run small pilots before a large matrix. Stop futile searches or hyperparameter sweeps at their bounds; redirect to relevant alternatives. A long process should have logs and a recoverable manifest, not a fabricated status. Any anticipated context limit triggers a checkpoint, not an arbitrary final claim.

## End
Produce artifacts and execute acceptance checks. Write a concise `.agent/block_reports/Bxx.md`, update STATUS.json and NEXT.md, and write `.agent/blocks/xx.json` using the bundled schema. Include start/end, measured elapsed minutes, gate evidence and commands, changed files, source IDs, actual model assignments, remaining blockers and exact next actions. File checksums or test logs are preferred to self-assertion. A code review does not replace execution.

Status meanings: `passed` = the scoped block has produced its promised, evidence-backed outcome, possibly a negative scientific result. `blocked` = a required dependency cannot be obtained. `needs_revision` = a failed gate. No final report is `submission_ready` until requirements and authentic human actions are resolved. A finished draft and an authorized submission are different states.

## Stop/recovery
Do not bypass permissions, pay for a dependency, leak credentials or alter unrelated user files. If a hard blocker occurs, save the exact failure and complete safe independent preparation; never substitute invented data. Limit a local fix loop to three materially different attempts, then record a diagnosis and choose a supported fallback or checkpoint. The external runner stops at blocked/failed states. AUTOPILOT can reorder independent preparation with an explicit dependency record, but cannot skip scientific gates.
