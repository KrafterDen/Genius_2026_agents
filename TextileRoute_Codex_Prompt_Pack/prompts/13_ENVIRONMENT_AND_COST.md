# Block 13 — Quantify the measured value and separate it from hypothetical benefits

Create a defensible environmental and resource assessment that can survive skeptical judging. Distinguish classification improvement, routing decisions and downstream industrial effects.


## Execution rules for this block
Treat the allocations below as a substantive **180–240-minute work package**, not a request to idle for three hours. Apply `framework/SESSION_CONTRACT.md`: execute core work, then useful depth work; report actual elapsed wall time and any under-target reason. Do not count parallel worker time as wall time.

Use the lead orchestrator **GPT-6 Sol High**. Suggested workers below are adaptable; choose the cheapest requested tier capable of the actual task, record real models/efforts and keep an independent challenge. Browse for material external facts and current tooling; use existing source records as starting points, not infallible truth. All specific architectures, libraries and methods here are proposals to test.

Before work read root AGENTS.md, STATUS.json, NEXT.md and the active plan. Create/update `.agent/execplans/B13.md`. Resolve reversible choices without asking the user. Respect scoped write ownership, data/test boundaries and `HUMAN_GATES.md`. After work run real acceptance checks, write `.agent/block_reports/B13.md` and `.agent/blocks/13.json`, update STATUS/NEXT and preserve the exact next command. A status of passed means the scoped outcome is evidenced, not that the project won or the results are positive.

## Path convention
`framework/`, `sources/`, `repository_template/` and `prompts/` are relative to the immutable prompt-pack folder. Project paths such as `src/`, `configs/`, `.agent/`, `results/` and `submission/` are relative to the initialized repository root.

## Required context
Frozen results, industrial sources/profiles, actual runtime logs, current supporting primary environmental literature.

## Suggested delegation
Sol Medium: environmental causal-chain analysis and cost framing. Luna Xhigh: measurements and tables. Independent reviewer: greenwashing/unsupported-number audit.

## Work sequence

### Environmental mechanism and boundaries — 45–60 min
Trace material collection/reuse triage, composition sensing, routing, recycler intake, processing and displaced output. Identify which links were directly tested. Explain tradeoffs: fewer unsuitable items versus rejecting usable material and review effort. Separate fibre criteria from full recyclability. Reopen primary sources for every quantitative environmental assumption.

### Measured computing and practical requirements — 45–60 min
Measure CPU/GPU runtime, peak memory where available, model size and per-spectrum latency on the real machine. Separate one-off training from inference. Explain that a real deployment needs a spectrometer/integration even if the research used public data. Do not invent energy from parameter count; use a actual meter/telemetry or leave energy unmeasured.

### Scenario and review-cost analysis — 50–65 min
If useful, construct labelled scenarios with explicit inputs, uncertainty and units. Without masses do not convert item acceptance to tonnes or stream contamination mass. Without measured human times use number of oracle reviews, not hours saved. Use sensitivity tables rather than unsupported precise returns or emissions savings. Report performance under the same budget across methods.

### Evidence audit and integration — 40–55 min
Check each numerical claim against measured/derived/assumed flags. Reviewer must try to remove inflated ecological language and expose hidden industrial dependencies. Update verified_summary/claim ledger only through documented extensions without changing test metrics. Write clear explanations for non-specialists and judges.

## Independent web challenge
Independently search whether the proposed routing benefit plausibly changes an environmental outcome and what additional evidence would be needed. A recycler case study is not a lifecycle assessment of our software.

## Expected artifacts
- `docs/environmental_assessment.md`
- `docs/resource_cost_analysis.md`
- `results/resources.json`
- `results/scenarios.json`
- `research/challenges/13_impact.md`
- `results/claim_ledger.csv`

## Acceptance gates
1. Measured technical outcomes and hypothetical environmental effects are distinct.
2. No invented mass, emissions, energy, human time or factory validation is used.
3. Compute requirements are actually measured where claimed.
4. Tradeoffs and real spectrometer/deployment needs are disclosed.

## Meaningful depth work after the core
Build unit-checking tests for scenario calculations, compare CPU-only and available GPU inference honestly, and validate sensitivity to documented profile/cost assumptions.

## Stop, narrow or invalidate when necessary
If the measured outcome is only a benchmark improvement, state potential rather than achieved recycling benefit. Do not enlarge the impact claim to compensate for weak metrics.
