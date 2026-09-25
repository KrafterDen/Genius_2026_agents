# Block 06 — Establish strong low-compute baselines and honest learning curves

Produce a reliable baseline table on development data only. The project must beat or meaningfully characterize existing simple approaches before adding complexity.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B06.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B06.md` and `.agent/blocks/06.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
Frozen development split/protocol; data pipeline; prior-art matrix; actual hardware.

## Suggested delegation
Luna Xhigh: run adapters and test code. Sol Medium: modelling and bounded experiment selection. Independent Sol challenger: stronger simple baselines. Astra only for an unresolved evaluation error.

## Work sequence

### Baseline implementation — 50–60 min
Implement a naïve/reference strategy, conventional composition-regression baseline (PLS/Ridge or evidence-backed alternative), and direct profile-eligibility classifier. Include a standard calibrated confidence/rejection policy and composition-then-threshold policy. Use comparable data and tuning budgets. Do not assume neural methods are superior. Unknown labels follow the protocol.

### Bounded development experiments — 60–75 min
Run a small preregistered grid on development folds with per-run manifests, configurations, seeds, fitting times and model sizes. Tune all preprocessing inside the folds. Include learning curves by independent items where meaningful. Log unsuccessful methods and all trials. A tiny 1D CNN is optional only if justified by data, budget and a separate challenge.

### Error analysis and practical comparison — 40–55 min
Report composition error, eligibility outcomes and risk/coverage/review curves, including reject-all behavior. Inspect threshold-near, pure, blended and unknown cases separately. Check whether a few items dominate apparent improvement. Identify relevant spectral or label limitations rather than blindly increasing architecture size.

### Independent replication and handoff — 35–50 min
Have another worker reproduce a selected baseline from a fresh invocation and verify metrics against predictions. Compare with a stronger existing alternative found by the challenger. Freeze a development-only baseline reference and write exact remaining room for improvement without looking at the final test.

## Independent web challenge
Search for a better simple spectroscopy or selective-classification baseline and compare it fairly. Recent publication date alone is not sufficient reason to replace PLS or a small classifier.

## Expected artifacts
- `src/textileroute/models/`
- `src/textileroute/policies/baselines.py`
- `configs/baselines.json`
- `results/development/baselines/`
- `research/challenges/06_models.md`
- `docs/baseline_analysis.md`

## Acceptance gates
1. Direct eligibility plus rejection and a classical spectral baseline are included.
2. All reported development metrics reproduce from stored predictions.
3. No final-test data was used for selection.
4. Trials are bounded and computationally appropriate; failures are preserved.

## Meaningful depth work after the core
Add group-level error plots, permutation sanity checks where statistically valid, and resource/learning-curve comparisons. Investigate numerical instability in small folds.

## Stop, narrow or invalidate when necessary
If simple methods are already as good as feasible custom methods, preserve that outcome. Do not cherry-pick a weak baseline or a favourable split.
