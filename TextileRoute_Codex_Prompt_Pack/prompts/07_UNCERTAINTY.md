# Block 07 — Implement uncertainty and selective decisions without false guarantees

Build an explicit reference uncertainty/routing layer and verify its actual statistical target. Generic existing risk control is a baseline, not yet the custom contribution.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B07.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B07.md` and `.agent/blocks/07.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
Baselines, source papers S15–S19, protocol and risk audit, actual calibration sizes.

## Suggested delegation
Sol Medium: risk/calibration implementation. Luna Xhigh: edge-case tests and documentation. Astra High: bounded audit of risk conditioning, calibration reuse and insufficient sample size.

## Work sequence

### Method selection and assumptions — 40–50 min
Compare confidence calibration, interval-based routing and a suitable existing precision/risk-control approach. Read original assumptions and current implementation docs. Choose based on the actual eligible/ineligible counts and grouping. Record formal versus empirical claims, exchangeability limitations and any abstention policy dependence.

### Implementation and reference checks — 60–75 min
Implement risk/coverage outputs, honest unknown/inconclusive cases and ACCEPT/REVIEW/not-eligible semantics. Retain simple threshold baselines. Ensure calibration is separate from hyperparameter selection under the selected method. Where feasible compare the implementation against an official/reference example. Avoid dependencies that duplicate a simpler correct implementation without benefit.

### Edge cases and diagnostic experiments — 45–60 min
Test zero accepted items, zero observed errors, one error, highly imbalanced labels, unknown components, threshold equality, absent classes, tiny calibration sets and forced distribution shifts. Compare claimed uncertainty to observed behavior on development data. Show insufficient evidence rather than falsely precise confidence.

### Independent audit and integration — 40–55 min
Provide Astra the exact estimand, derivation, source assumptions, implementation and test output. Resolve every critical concern. Update API/UI wording so it cannot imply individual chemical purity or guaranteed batch quality. Freeze this as an existing-method reference for the custom pilot.

## Independent web challenge
Search current primary risk-control methods and challenge whether a direct binary method is more appropriate than composition intervals. Reject fashionable but mismatched statistics.

## Expected artifacts
- `src/textileroute/calibration/`
- `src/textileroute/policies/selective.py`
- `tests/test_selective_risk.py`
- `protocol/guarantee_scope.md`
- `research/challenges/07_risk_control.md`
- `docs/uncertainty_reference.md`

## Acceptance gates
1. Risk numerator/denominator, rejection and undefined cases are correct.
2. No marginal-coverage-to-selective-precision leap remains.
3. Calibration/test boundaries and small-sample caveats are enforced in code and wording.
4. A reference implementation or independently calculated cases validate the metrics.

## Meaningful depth work after the core
Add adversarial toy examples exposing confidence/coverage confusion and compare empirical versus analytic bounds under declared assumptions. Use simulation only to test mathematics, not to claim real-textile reliability.

## Stop, narrow or invalidate when necessary
If no meaningful risk certificate is possible, output an empirical policy with uncertainty and clear non-certification. Never force an ACCEPT action just to improve coverage.
