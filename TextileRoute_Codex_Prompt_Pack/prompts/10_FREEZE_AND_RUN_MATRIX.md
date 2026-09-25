# Block 10 — Freeze the protocol, code and final experiment matrix

Make final evaluation genuinely confirmatory to the extent the data permits. Resolve ambiguity before opening held-out outcomes and make the complete run matrix executable.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B10.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B10.md` and `.agent/blocks/10.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
All development results, method implementations, source/label audit, risk scope and protocol.

## Suggested delegation
Sol Medium: final experiment harness. Luna Xhigh: manifests/checksums and dry-run tests. Astra High: independent pre-test validity audit, bounded to concrete risks.

## Work sequence

### Reconcile protocol with development — 40–55 min
Document all changes since preregistration, why they were made and that they used development data only. Freeze the primary comparison, targets, profile sources, metrics, weights, seeds, tuning bounds, calibration rule and planned sensitivity analyses. Specify exactly which analyses are confirmatory versus exploratory.

### Run matrix and immutable manifests — 50–65 min
Create a bounded machine-readable matrix with per-run hashes, split IDs, model/config versions, budget and expected artifacts. Implement resumable execution that does not duplicate finished runs or overwrite evidence. Validate success/failure states and partial run recovery. Pin dependencies and record actual hardware.

### End-to-end dry run — 45–60 min
Execute the entire fit/calibrate/predict/evaluate/report chain on development or legal small fixtures, not the final labels. Validate every output schema, saved model, group and metric. Check resources and total trial count. Test interruption, failed fit and result cache invalidation.

### Freeze gate — 45–60 min
Have Astra audit code/protocol/calibration and sample-size claims before final access. Resolve critical issues. Write a freeze manifest with code revision and hashes, a test-access policy and exactly what will happen on negative outcomes. Prepare the independent evaluation script and lock relevant configs.

## Independent web challenge
Independent pre-test challenge should look for ways a claimed improvement could be an artifact of split design, review budget or calibration reuse. It may force a narrower inference, not a more favourable test.

## Expected artifacts
- `configs/experiments.json`
- `configs/freeze.json`
- `scripts/run_experiments.py`
- `scripts/evaluate_frozen.py`
- `protocol/final_analysis_plan.md`
- `research/challenges/10_pretest_audit.md`
- `docs/freeze_receipt.md`

## Acceptance gates
1. No final labels influenced model, policy, threshold or presentation of a winner.
2. All primary and robustness analyses are specified and bounded.
3. Dry run succeeds and fault recovery preserves evidence.
4. Freeze manifest binds code/data/splits/configs; critical audit issues are closed.

## Meaningful depth work after the core
Rehearse a clean checkout/environment and dependency-lock recovery, independently verify metric equations and prepare an exact resource-measurement protocol.

## Stop, narrow or invalidate when necessary
If a critical leak or label defect is found, invalidate the development claims, fix the source and repeat affected gates before opening the final test.
