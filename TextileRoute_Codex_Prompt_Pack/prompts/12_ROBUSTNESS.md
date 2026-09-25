# Block 12 — Evaluate preregistered robustness and delimit generalization

Find where the prototype fails, using predefined tests and honest exploratory labels. Do not turn simulated shifts into external industrial validation.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B12.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B12.md` and `.agent/blocks/12.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
Final frozen outputs; predefined robustness matrix; real data provenance and label audit.

## Suggested delegation
Sol Medium: robustness interpretation. Luna Xhigh: test runner and figures. Independent Sol reviewer: realism of perturbations and overclaim checks.

## Work sequence

### Run planned robustness matrix — 55–70 min
Execute only preregistered tests as confirmatory: available independent acquisition groups, near-threshold versus pure materials, missing/rounded composition, sensor/wavelength variants or noise levels justified before testing. Use realistic ranges grounded in measurements or sources. Keep synthetic stress tests explicitly separate from real shifted data.

### Unknown and unsupported cases — 45–60 min
Inspect out-of-scope fibres, absent mixture combinations, layers/finishes not represented, profile mismatches and invalid spectra. Verify the system declines an unsupported decision rather than extrapolating confidently. Report coverage loss as part of robustness, not just reduced error among a tiny accepted subset.

### Label and scenario sensitivity — 45–60 min
Apply documented ambiguity assumptions without treating them as true chemical labels. Show how conclusions change with profile threshold and review/cost budget only as permitted sensitivity or labelled exploration. No scenario-specific threshold becomes a hidden retuned final model. Check count-versus-mass and no-accepted denominators.

### Independent challenge and limitations — 35–50 min
Have reviewer distinguish tested population from extrapolation and plausible physical effects from artificial perturbations. Build a failure gallery with evidence IDs and a limitations section. Update model/data cards and restrict allowed claims; do not overwrite the primary result.

## Independent web challenge
Search primary evidence on NIR/textile measurement failure modes and challenge the realism of the selected stress tests. Do not imply robustness to an untested sensor or whole garments.

## Expected artifacts
- `results/robustness/`
- `docs/failure_gallery.md`
- `docs/generalization_limits.md`
- `docs/model_card.md`
- `research/challenges/12_robustness.md`
- `results/robustness_summary.json`

## Acceptance gates
1. Confirmatory and exploratory robustness analyses are clearly separated.
2. Synthetic perturbations are not described as a real factory test.
3. Unsupported inputs have safe, explicit output behavior.
4. Claim scope reflects failed groups, uncertain labels and coverage loss.

## Meaningful depth work after the core
Inspect a bounded set of representative spectra/photos for failure interpretation, add API input-error tests and prepare a compact valid-versus-invalid use table.

## Stop, narrow or invalidate when necessary
If only a narrow in-dataset benefit survives, report exactly that. No broad generalization claim is required for the work to be scientifically honest.
