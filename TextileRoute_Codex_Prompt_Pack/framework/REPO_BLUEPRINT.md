# Repository blueprint and ownership

The prompt pack stays at `<repo>/TextileRoute_Codex_Prompt_Pack/`. Bootstrap copies `repository_template/` safely into the repository and adapts it, without overwriting existing instructions or user work. The following are target paths, not claims that their implementation already exists.

| Path | Contents / owner |
|---|---|
| `AGENTS.md` | Thin root constitution: project, evidence rules, state navigation, autonomy and human boundaries; orchestrator. |
| `PLANS.md` | Instructions for live, self-contained block ExecPlans; orchestrator. |
| `PROJECT.md` | Scope, hypothesis, target population and current decision status. |
| `STATUS.json`, `NEXT.md`, `HUMAN_ACTIONS.md` | Actual machine/human checkpoint, exact next commands, batched authentic human needs. |
| `.agent/execplans/Bxx.md` | Current plan, progress, decisions, surprises and validation for each block. |
| `.agent/blocks/xx.json`, `.agent/block_reports/Bxx.md` | Evidence-backed block completion and narrative handoff. |
| `.agent/tasks.json`, `.agent/dispatch.jsonl`, `.agent/sessions.jsonl` | Feature/gate inventory, real model assignments and timing/usage. |
| `.agent/locks/`, `.agent/runtime/` | Scoped ownership and validated local tools; temporary runtime logs remain local. |
| `.codex/config.toml`, `.codex/agents/*.toml` | Project-only settings verified against installed Codex; examples must not be blindly activated. |
| `configs/project.json` | Actual task, target and assumptions. |
| `configs/resource_budget.json` | Bounded compute, downloads, search/delegation limits, paid services off. |
| `configs/recycler_profiles.json` | Source-dated fibre criteria; unobserved requirements; historic/scenario/current status. |
| `configs/experiments.json`, `configs/freeze.json` | Reproducible run matrix and frozen hypotheses/splits/hashes. |
| `research/sources.jsonl`, `research/claims.csv`, `research/search_log.jsonl` | Primary evidence, supported wording and actual web searches. |
| `research/prior_art_matrix.csv`, `research/challenges/`, `research/decisions/` | Closest existing work, independent objections and resolved decisions. |
| `protocol/` | Data audit, grouping, calibration, evaluation, risk mathematics and preregistered stress tests. |
| `data/raw/`, `data/processed/`, `data/manifests/`, `data/splits/` | Immutable downloads, derived inputs, licenses/hashes, independent-unit splits; raw data gitignored. |
| `src/textileroute/` | Typed modules: contracts, ingestion, spectra, models, calibration, policies, evaluation, reporting; exact layout may be improved. |
| `tests/` | Unit, property/boundary, leakage, fixture, integration, reproducibility and result-consistency tests. |
| `scripts/` | Reproducible commands for fetching, auditing, fitting, evaluation, demo, documents and submission validation. |
| `results/runs/<run_id>/` | Immutable config, revision, seeds, logs, fitted model, predictions and metrics, including failures. |
| `results/verified_summary.json`, `results/claim_ledger.csv` | Only approved source of numbers/claims for public artifacts; invalidated after evidence changes. |
| `app/` | Local offline demonstration; no chemical claims from a photograph. |
| `docs/` | Architecture, setup, model card, dataset card, limitations, actual measured resources and user guide. |
| `documents/` | Source reports/abstracts/citations, generated from verified results with language-specific rendering. |
| `presentation/`, `video/` | Timed slides, honest demo sequence, English narration, captions, local assets and instructions. |
| `contribution/` | Actual student work versus AI assistance; defense workbook and learning checkpoints. |
| `submission/uk/`, `submission/international/`, `submission/supporting/` | Validated stage-specific deliverables, manifests and unresolved approval status. |
| `private/` | Gitignored personal data and consent records, never in a public/code submission bundle. |

## Bootstrap implementation constraints
Create a minimal importable package and test harness, not empty placeholders claiming tests passed. Prefer a small, pinned Python environment; choose the dependency manager after local and official-doc inspection. Use standard library first for control scripts. No dependence on a hosted experiment dashboard, paid LLM API, Docker or system administrator privileges unless truly necessary and explicitly authorized. Plain local structured logs are enough.

Add nested AGENTS.md only where a scoped rule is genuinely needed (data, results, documents). They must not negate root scientific honesty. Keep root concise and below the client's instruction budget. Preserve the immutable prompt pack; record necessary changes as versioned local adaptations rather than silently modifying the original source plan.
