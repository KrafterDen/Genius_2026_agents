# Block 09 — Implement the selected method, fair review workflow and ablations

Turn the chosen pilot into maintainable code with a complete ablation suite. Freeze interfaces so the final experiment is not a collection of changing notebooks.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B09.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B09.md` and `.agent/blocks/09.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
ADR008, method specification, baselines, data/calibration pipeline, preregistered protocol.

## Suggested delegation
Luna Xhigh: well-specified modules/tests. Sol Medium: algorithm integration and experiments. Independent read-only Sol reviewer: fairness and hidden data access.

## Work sequence

### Production-quality method module — 55–70 min
Implement the selected contribution with typed inputs, deterministic configuration, explicit unknown states and provenance. Keep fitting, prediction, calibration and action selection separate. Limit writable scope per worker. Avoid a monolithic notebook, cloud dependency or mutable global state. Reuse the verified baseline interfaces.

### Ablation and budget parity — 45–60 min
Implement component-off, simpler-score and relevant existing-method alternatives. Match review count, data and tuning allowances. Clarify whether querying a label changes training or only current decisions; do not leak test labels into subsequent predictions under a different protocol. Record all oracle/idealized assumptions.

### Development verification — 45–60 min
Run bounded group-wise development comparisons, profile memory/runtime and investigate edge cases. Check labels cannot accidentally enter input features. Add tests for saved/loaded predictions, no-acceptance conditions, incomplete composition and deterministic review order/ties. Remove only demonstrably broken code, not bad outcomes.

### Independent review and revision — 35–50 min
Reviewer inspects the real call graph, metadata joins, fitting boundaries, comparison fairness and tested actions. Fix issues and rerun affected development experiments. Update the method description and baseline matrix. No held-out test inspection yet.

## Independent web challenge
Have a reviewer search for implementation/reference pitfalls in the exact selected method and check whether a smaller equivalent formulation suffices.

## Expected artifacts
- `src/textileroute/policies/custom.py`
- `configs/ablations.json`
- `tests/test_custom_policy.py`
- `tests/test_no_label_leakage.py`
- `docs/method_implementation.md`
- `research/challenges/09_implementation.md`
- `results/development/ablations/`

## Acceptance gates
1. Contribution-off and strongest applicable reference comparators work.
2. Review/data/compute budgets are matched or differences disclosed.
3. All decision inputs and label access obey the protocol.
4. Independent code review findings are resolved or explicit blockers.

## Meaningful depth work after the core
Use property/boundary tests, a second metric implementation and counterfactual metadata checks. Improve maintainability only where it supports reproducibility or correctness.

## Stop, narrow or invalidate when necessary
Do not add a new second contribution because the first lacks a dramatic gain. Revise the claim and preserve the evidence.
