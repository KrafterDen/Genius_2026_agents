# Block 14 — Build a clear, offline demonstration using the actual trained pipeline

Create a working local demo that shows the decision, evidence and limitations without pretending a camera can chemically identify clothing.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B14.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B14.md` and `.agent/blocks/14.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
Validated model/policy, measured example spectra, claim ledger, model card and actual deployment constraints.

## Suggested delegation
Luna Xhigh: UI components and deterministic tests. Sol Medium: model/UI integration. Independent reviewer: scientific wording and actual end-to-end behavior.

## Work sequence

### Interaction design and technology challenge — 35–50 min
Choose a small local interface after checking current official docs and alternatives: a lightweight web app or desktop-like local page, not a paid hosted product. Plan an end-to-end story: select/upload a valid spectrum, choose a sourced profile, display decision and reason, show unknown requirements and optional review queue. Use photographs only as context with that label.

### Implementation — 65–80 min
Connect to the actual saved preprocessing/model/calibration/policy, never a mock scoring function. Add allowed sample examples, input schema validation, unsupported-input handling, profile source/date, calibrated/empirical status, version and provenance. Cache models locally. No external API needed at inference. Avoid uploading data or exposing a public server.

### Demonstration scenarios and explanation — 40–55 min
Show a clear eligible case, ambiguous/review case, unsupported/not-eligible case and an actual failure/limitation. Use measured or clearly synthetic fixture labels correctly. Include comparison with the selected existing baseline using frozen results, not live retuning. Prepare screenshots and a compact user guide.

### End-to-end testing — 40–55 min
Run the app offline after installing dependencies, exercise valid/invalid uploads and record actual UI behavior. Test local-only binding, asset loading, deterministic outputs, graceful missing-model handling and displayed number consistency. Review accessibility/readability and scientific honesty. Save test evidence and a reliable recording sequence.

## Independent web challenge
Have an independent role compare a simpler UI stack and test whether the proposed interface misleads users about guaranteed purity, unknown requirements or original data.

## Expected artifacts
- `app/`
- `scripts/launch_demo.py`
- `tests/test_demo_integration.py`
- `docs/demo_user_guide.md`
- `docs/demo_test_evidence.md`
- `presentation/demo_storyboard.md`
- `research/challenges/14_demo_stack.md`

## Acceptance gates
1. Demo uses the actual pipeline and works without network at inference.
2. Spectrum/photograph roles and measurement limitations are unmistakable.
3. Known, ambiguous, unsupported and failure cases are represented honestly.
4. End-to-end testing and ledger consistency are recorded.

## Meaningful depth work after the core
Add automated screenshot/browser smoke checks if available, keyboard accessibility, local deployment troubleshooting and a recorded fallback demonstration.

## Stop, narrow or invalidate when necessary
If UI tools are unavailable, use a reproducible CLI plus local static report rather than invent a finished app. Do not hide a nonfunctional model behind a polished mockup.
