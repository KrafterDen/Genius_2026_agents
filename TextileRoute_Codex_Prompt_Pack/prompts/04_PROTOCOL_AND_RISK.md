# Block 04 — Preregister the experiment and validate what can be claimed

Design the evaluation before modelling so the project can distinguish real gains from leakage, threshold selection and small-sample overconfidence.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B04.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B04.md` and `.agent/blocks/04.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
Actual audited data/group counts; provisional method/prior art; scientific contract; S14–S19.

## Suggested delegation
Sol Medium: evaluation design and metric implementation specification. Astra High: independent selective-risk/tiny-sample audit. Luna Xhigh: schema, boundary calculations and reproducibility checks.

## Work sequence

### Operational target and estimands — 40–55 min
Write the exact decision population, fibre criteria, unsupported non-fibre conditions, action semantics and count-based metrics. Define accepted-set risk, coverage, review rate, false rejection, reference label error and what mass-based data would additionally require. Specify empty-acceptance behavior, ambiguous labels and valid review-oracle simulation language. State primary endpoint and secondary analyses.

### Splits, calibration and power — 55–70 min
Choose a realistic grouped design given the actual independent units. Justify train/tune/calibration/final allocation or carefully nested grouped evaluation if data is too small; state which formal guarantees do not apply. Prevent dependent scans, fitted preprocessing and threshold tuning from crossing boundaries. Derive uncertainty and minimum detectable/supported effects. Include zero-error binomial sanity checks and repeated-fold limitations.

### Frozen research protocol draft — 50–65 min
Specify baselines, maximum tuning trials, candidate contribution, ablations, deployment profiles, seeds, cost/review budgets and robustness tests. Separate realistic domain tests from synthetic stress. Define success, equivalence, negative and inconclusive outcomes. Describe label-error sensitivity without pretending supplier labels are chemical truth. Create a final-test access log and a change-control rule.

### Red-team resolution and executable checks — 35–50 min
The Astra reviewer must try to invalidate the risk statement, reveal selection bias or show that the sample size cannot support it. Respond with a revision or explicit downgrade. Implement/reference testable metric contracts, independent-unit checks and mock calculations. Sign the protocol by revision/hash, not by impersonating a human approval.

## Independent web challenge
Compare different evaluation/risk-control frameworks online. Have Astra review the closest method’s actual assumptions, not an informal summary; provide a concrete counterexample when a claimed implication is false.

## Expected artifacts
- `protocol/preregistered_protocol.md`
- `protocol/metrics.json`
- `protocol/split_plan.json`
- `protocol/risk_analysis.md`
- `protocol/test_access_log.jsonl`
- `research/challenges/04_statistics.md`
- `tests/test_metric_contracts.py`

## Acceptance gates
1. Selective risk is not confused with marginal interval coverage or batch purity.
2. Independent units, calibration boundaries and no-retuning policy are explicit.
3. Risk sample-size calculations are reproducible and impossible guarantees removed.
4. Primary/secondary analyses and negative-result handling are specified before final test access.

## Meaningful depth work after the core
Construct synthetic unit-test counterexamples to pixel leakage, reject-all scoring, post-hoc threshold selection and misleading repeated-fold confidence. These are testing fixtures, not empirical environmental evidence.

## Stop, narrow or invalidate when necessary
If valid precision guarantees are impossible, continue with explicitly empirical or exploratory evaluation. Do not manufacture more independence through augmentation or repeated cross-validation.
