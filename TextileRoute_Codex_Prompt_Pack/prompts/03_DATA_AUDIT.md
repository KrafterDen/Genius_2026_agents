# Block 03 — Retrieve small data first and decide whether the target is identifiable

Acquire and audit the real dataset before committing to a model. This block is a hard go/no-go gate for the proposed mixture-threshold task.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B03.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B03.md` and `.agent/blocks/03.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
S06–S08; candidate hypotheses; recycler profiles; actual resource budget.

## Suggested delegation
Luna Xhigh: safe manifest/download and parsing after format verification. Sol Medium: label/group audit. Read-only challenger: find a better legal dataset or safer target if the candidate cannot support the task.

## Work sequence

### Access, license and manifest — 40–55 min
Resolve DOI 10.5281/zenodo.18269172 and retrieve the landing metadata/license, file list, small composition table and supplied mean spectra before any hyperspectral cubes. Record hashes, versions, file sizes, exact license and attribution. The pack does not prove access or license. Handle network errors explicitly; do not execute sample repository scripts before inspecting them. Respect download budget and raw immutability.

### Physical measurement audit — 55–70 min
Inspect wavelength units/range, reflectance or other representation, preprocessing already applied, missing values, metadata identifiers, textiles versus garments, scans/pixels/views, dark/white calibration and supplier labels. Count truly independent units and trace shared provenance. Inspect representative spectra and anomalies. Photographs are context, not fibre ground truth. Summarize what exact versus rounded/ambiguous composition means in the actual files.

### Target feasibility and alternative search — 50–65 min
For every candidate process profile count eligible/ineligible/unknown items, mixtures, threshold-near cases and provenance groups. Keep unknown labels distinct. Calculate plausible final/calibration sample sizes and whether risk claims are even supportable. Independently search for supplementary datasets with compatible measurements and legal labels; do not merge incompatible instruments without a justified protocol. Prefer a narrow valid study over fake breadth.

### Decision, fixtures and reporting — 35–50 min
Produce a data card and machine-readable audit, grouping/target schemas and representative test fixtures. Decide proceed, narrow or blocked. A feasible fallback may be pure-versus-blend or an explicitly exploratory routing benchmark, but must change the title/claim. Publish counts and all unsupported profiles. Write a reproducible audit command and preserve its output.

## Independent web challenge
Search for a more appropriate dataset, target or acquisition subset. Compare label quality and independent units, not headline data volume. A different dataset requires a new license/group audit.

## Expected artifacts
- `data/manifests/dataset_manifest.json`
- `protocol/data_audit.json`
- `protocol/data_audit.md`
- `docs/dataset_card.md`
- `protocol/grouping.json`
- `protocol/target_feasibility.csv`
- `research/challenges/03_data.md`
- `research/decisions/ADR-003-data-gate.md`

## Acceptance gates
1. Real file retrieval and license are verified or the block is explicitly blocked.
2. Physical sample/garment counts replace misleading pixel counts.
3. Threshold labels and independent positive/negative cases exist for the chosen target.
4. No ambiguous compositions are silently treated as exact negatives or zero impurity.

## Meaningful depth work after the core
Inspect additional acquisition examples, test parser robustness against malformed rows, characterize supplier rounding and image/metadata mismatches, and calculate how conclusions change under plausible label ambiguity.

## Stop, narrow or invalidate when necessary
If no legal accessible dataset supports any defensible textile target, checkpoint BLOCKED_BY_DATA. Continue only independent scaffolding and literature work; synthetic fixtures are not substitute scientific results.
