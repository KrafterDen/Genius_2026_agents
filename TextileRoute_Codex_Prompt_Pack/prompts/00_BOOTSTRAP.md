# Block 00 — Initialize the repository and a recoverable autonomous workflow

You are the lead orchestrator, preferably GPT-6 Sol with high reasoning. Create the working repository and control system for TextileRoute. Execute this initialization, not merely describe how it could be done. The project is a local, source-grounded study of NIR-based textile routing for GENIUS AI; it is not a promise of industrial purity or novelty. The entire pack is expected at `<repo>/TextileRoute_Codex_Prompt_Pack/`. Locate that exact folder in the open workspace; do not scan unrelated personal directories. If the pack itself was opened as the entire workspace and its parent is outside the authorized workspace, do not write into the parent or recursively copy the pack. Produce a no-write diagnostic and request the single necessary workspace correction described in START_HERE_RU.md.

**First prompt:** create the repository controls described below and in REPO_BLUEPRINT; do not assume they already exist. Locate this pack before following its relative paths.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B00.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B00.md` and `.agent/blocks/00.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
Pack START_HERE_RU.md; framework/REPO_BLUEPRINT.md, PROJECT_CHARTER.md, ORCHESTRATION.md, MODEL_ROUTING.md, SCIENTIFIC_CONTRACT.md, HUMAN_GATES.md; repository_template/; sources/; current workspace status.

## Suggested delegation
Luna Xhigh: bounded filesystem/template and smoke-test tasks. Sol Medium: current Codex/environment capability research. Separate Luna read-only audit of initialized state. The orchestrator integrates. Astra is unnecessary unless a material scientific ambiguity is discovered.

## Work sequence

### Workspace and capabilities — planning allocation 35–45 min
Inspect directory, existing AGENTS.md, git status, permissions and available tools without changing unrelated work. Detect OS, Python, disk, RAM, GPU/CUDA and actual nvidia-smi availability; absence is a supported CPU-first case. Inspect Codex version/help and verify current official model/subagent documentation through available web tools. Record which requested model/effort combinations can really run. Test one small child task if delegation is available; log actual model, not inferred model. Record network and browser capabilities. No administrator installs, global config edits or sandbox bypasses.

### Control plane and repository skeleton — 60–75 min
Follow REPO_BLUEPRINT. Safely merge the repository templates, then create a minimal importable package, test directory and a small executable smoke test that actually runs. Initialize PROJECT.md, STATUS.json, NEXT.md, PLANS.md, HUMAN_ACTIONS.md, .agent/tasks.json and per-block states. Create research/source/claims/search logs and result/data directories with proper ignore rules. Preserve the pack untouched. Root AGENTS.md must explain navigation, scientific honesty, actual source research, independent challenge, model routing, one-writer ownership, resumability and human boundaries; do not bury thousands of lines in it. Add scoped data/results/document instructions only when needed. Create an initial feature/gate inventory with false/not_started flags, not pre-passed claims. Copy the source register as starting evidence, retaining unverified data-file status.

### Local execution and role configuration — 45–60 min
Choose a minimal project-local Python environment after inspecting installed tools. Implement the documented version-compatible native subagent roles from the .toml.example files, preserving existing configuration. Roles may be adapted, but model and effort must be explicit and known unavailable roles must be labelled. Create a capability record and a validated local runner configuration only after checking each CLI argument against installed help and a harmless smoke invocation. Use the bundled optional runner as a reference; do not run it recursively from this session. No paid API assumption. Create a repository validator that checks state schemas, expected files, source IDs and evidence paths, using standard library where possible. Establish reproducible logging and basic test commands.

### Failure/restart rehearsal — 40–60 min
Exercise the initialized test suite and validator. Rehearse a stopped block, a missing artifact, unknown model, unavailable network and a failed command in controlled fixtures; each must remain failed/blocked, not become passed. Check that NEXT.md plus the active plan is enough to resume without the chat. Audit that private data, credentials, raw downloads and logs will not be accidentally published. Generate a concise actual environment report, proposed pipeline and batched human actions. Explain the dataset and genuine student-contribution gates without requiring the user to choose libraries.

## Independent web challenge
Have a separate Sol Medium reviewer inspect current official Codex practices for native subagents, worktrees, plan/state and noninteractive execution. Prefer the simplest verified mechanism; do not build a custom multi-agent platform if native delegation is sufficient.

## Expected artifacts
- `AGENTS.md`
- `PROJECT.md`
- `PLANS.md`
- `STATUS.json`
- `NEXT.md`
- `HUMAN_ACTIONS.md`
- `docs/environment_audit.md`
- `docs/codex_capabilities.md`
- `scripts/validate_repository.py`
- `.agent/tasks.json`
- `.agent/blocks/00.json`

## Acceptance gates
1. Existing user files and instructions are preserved; no global or public changes occurred.
2. A real smoke test and repository validator run successfully and logs are saved.
3. Available versus unavailable models, actual hardware and network state are recorded accurately.
4. States are resumable, incomplete experiments are not claimed, and human release gates are visible.

## Meaningful depth work after the core
Add fault-injection tests for path traversal in artifact manifests, invalid states, conflicting writers and safe reruns. Audit local instructions for contradictory or oversized context. Build a small deterministic fixture that future pipeline tests can use, clearly marked synthetic.

## Stop, narrow or invalidate when necessary
If the environment cannot execute or browse, save exact blockers and prepare everything safe offline. Never claim a validated runner/configuration before testing it. Do not request administrative access or silently widen permissions.
