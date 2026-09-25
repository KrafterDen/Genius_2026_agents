# Block 05 — Implement audited data ingestion, preprocessing and leakage guards

Build the reproducible data path that future experiments will use. Correctness, units and grouping are more important than a large model.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B05.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B05.md` and `.agent/blocks/05.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
Audited manifest, target schema, protocol, resource budget and current official library documentation.

## Suggested delegation
Luna Xhigh: parsers, CLI and tests under explicit schemas. Sol Medium: preprocessing/group handling. Independent reviewer: leakage and safe file loading.

## Work sequence

### Typed contracts and loaders — 45–60 min
Implement validated sample/group identifiers, wavelengths, spectra, composition targets/unknown values and metadata provenance. Fetching and processing are separate commands. Reject unsupported shape/units instead of guessing. Keep immutable raw data and deterministic derived hashes. Use safe CSV/JSON/array formats; do not load arbitrary executable pickles from the web.

### Candidate spectral pipeline — 50–65 min
Implement no-preprocessing baseline and justified candidate transforms such as scaling, SNV or Savitzky–Golay derivatives only after source and data checks. Each tunable/fitted transform participates correctly in a pipeline and is fit within allowed folds. Handle negative/invalid values explicitly; do not blindly clip scientifically meaningful measurements. Preserve the supplied mean-spectrum baseline.

### Group splits and command interface — 40–55 min
Implement the preregistered group allocator and produce immutable split manifests. Add small real-data smoke and clearly synthetic boundary fixtures. Create deterministic audit/prepare commands with errors and helpful messages. No automatic download of full cubes if mean spectra are sufficient. Record processing runtime and memory.

### Integration and failure tests — 45–60 min
Test duplicate scans across folds, repeated garment IDs, unknown labels, reordered wavelengths, missing files, malformed compositions, cached-data hashes and reproducibility. Have a reviewer trace one sample end-to-end and confirm information from the held-out set does not influence preprocessing. Save executed logs and an architecture note.

## Independent web challenge
Have the challenger compare using supplied mean spectra with spatial subsampling/cubes, and current tooling alternatives. Adopt the simpler pipeline unless the additional data solves a measured bottleneck.

## Expected artifacts
- `src/textileroute/data/`
- `src/textileroute/spectra/`
- `scripts/prepare_data.py`
- `data/splits/`
- `tests/test_data_pipeline.py`
- `tests/test_leakage_guards.py`
- `docs/data_pipeline.md`

## Acceptance gates
1. A clean command reconstructs processed data from verified inputs.
2. No independent group crosses a split; leakage tests catch deliberate violations.
3. Units, missing labels and preprocessing state are checked rather than inferred silently.
4. Real smoke execution and memory measurements fit the actual machine.

## Meaningful depth work after the core
Property-test composition parsing and group allocation, exercise cache invalidation and partial-download recovery, and add a small fresh-environment integration test.

## Stop, narrow or invalidate when necessary
If the requested array/cube does not fit memory, stream or narrow justified inputs. Do not buy cloud memory, disable validation or discard difficult samples without logging.
