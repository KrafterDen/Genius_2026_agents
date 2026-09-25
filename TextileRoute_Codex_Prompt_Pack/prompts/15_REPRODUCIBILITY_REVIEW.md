# Block 15 — Reproduce the whole project and prepare authentic student understanding

Have a fresh reviewer reproduce the work from documented artifacts and make the student contribution/defense plan concrete without fabricating its completion.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B15.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B15.md` and `.agent/blocks/15.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
Code/lockfiles, frozen run manifests, results ledger, demo, contribution logs and literature.

## Suggested delegation
Luna Xhigh: clean-environment installation and packaging checks. Sol Medium: independent reproduction and student-facing explanations. Astra High: one targeted final science audit if critical uncertainty remains.

## Work sequence

### Fresh setup rehearsal — 50–65 min
Use a clean project-local environment or worktree, not the orchestrator’s hidden state. Follow README commands from raw licensed inputs or small legal smoke fixtures to prediction and metric recomputation. Record exact deviations. Check lockfile portability on the actual OS, no hidden cloud dependencies and resource constraints.

### Evidence and implementation audit — 45–60 min
Review every headline against the prior-art matrix, data source, protocol, output table and allowable inference. Inspect grouping, calibration, test access, failed experiments and final result changes. Verify manifests and model loading safety. Fix packaging/docs, but do not silently tune scientific results.

### Student contribution and learning package — 50–65 min
Create a plain-language Ukrainian/Russian support workbook and English defense questions explaining NIR, mixtures, criteria, model, held-out groups, sample size and environmental limits. Provide the planned substantive student experiment, steps, expected kinds of outcomes (not fake observations), and prompts to interpret results. Record only the student’s actually supplied work/answers. Prepare an honest division-of-contributions draft with pending fields.

### Release-candidate rehearsal — 35–50 min
Run the local demo as a new user, check licenses, remove private/raw restricted data from candidate archives, and create a reproducibility report. Consolidate human needs into one list. If student work/narration is pending, keep drafts progressing but submission_ready false. Reviewer signs only an audit identity as an AI role, not an external scientist.

## Independent web challenge
An independent reviewer should treat the README as the only onboarding context and identify every hidden assumption. Research unfamiliar scientific objections using primary sources.

## Expected artifacts
- `README.md`
- `docs/reproducibility_report.md`
- `docs/final_science_audit.md`
- `contribution/learning_workbook.md`
- `contribution/defense_questions.md`
- `contribution/contributions_draft.md`
- `HUMAN_ACTIONS.md`

## Acceptance gates
1. A new environment can reproduce the documented smoke and key metric path.
2. No claim relies on untracked local state or undisclosed excluded results.
3. Student and agent work are truthfully separated; pending student work is not marked done.
4. No restricted/private content enters candidate public bundles.

## Meaningful depth work after the core
Add small reproducibility regression tests, check dependency/license transitivity and translate difficult concepts without changing statistical meaning.

## Stop, narrow or invalidate when necessary
If key results cannot reproduce, invalidate readiness and fix the source of failure. Do not substitute a screenshot for reproducibility or a generated essay for student understanding.
