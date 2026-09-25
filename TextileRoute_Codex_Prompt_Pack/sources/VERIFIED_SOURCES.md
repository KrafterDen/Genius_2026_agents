# Starting evidence register

Sources were checked on 25 September 2026. This is not an exhaustive prior-art review. Claims below are deliberately scoped. In particular, the dataset files/license remain unverified. Open current primary sources before implementation choices and submissions.

## S01 — GENIUS Olympiad Ukraine — home and season announcement
https://ukraine.geniusolympiad.org/

**Supports:** Ukraine 2027 announcement and dated schedule; category information updating.

**Status:** opened. **Limit:** Do not reuse old 2020/2021 sections; final format is unresolved.

## S02 — GENIUS Olympiad Ukraine — categories, AI section
https://ukraine.geniusolympiad.org/categories.html

**Supports:** Published national AI report/video requirements and assessment headings.

**Status:** opened. **Limit:** Working baseline: page still contains a 2026 final reference; recheck 2027.

## S03 — GENIUS Olympiad Ukraine — participants
https://ukraine.geniusolympiad.org/participants.html

**Supports:** Ukrainian-school/age eligibility, language and registration routes.

**Status:** opened. **Limit:** Residence abroad does not by itself establish or disprove school eligibility.

## S04 — GENIUS Olympiad — disciplines, AI section
https://geniusolympiad.org/disciplines.html

**Supports:** AI: English report, video, final presentation, meaningful student work, rubric.

**Status:** opened. **Limit:** Do not import adjacent Coding hackathon or Speech topic requirements.

## S05 — GENIUS AI Research Paper template
https://geniuscountries.s3.us-east-2.amazonaws.com/GENIUS_AI_ResearchPaper.pdf

**Supports:** Six-page template; formatting, sections, abstract, student roles and external contributions.

**Status:** opened_and_page_images_inspected. **Limit:** Re-download before final build; count total international pages including references.

## S06 — Introducing OpenTextile-NIR — article and data description
https://cris.vtt.fi/en/publications/introducing-opentextile-nir-near-infrared-hyperspectral-imaging-a/

**Supports:** 71 physical samples, millions of spectra, supplier composition information, mean spectra and file types; April 2026 article.

**Status:** opened. **Limit:** Article DOI 10.1016/j.dib.2026.112559. Data files and data license not inspected here. Description uses both post-industrial and end-of-life terminology; verify provenance.

## S07 — Tuomas Sormunen — creator research and dataset record
https://cris.vtt.fi/en/persons/tuomas-sormunen/

**Supports:** Creator record identifies OpenTextile-NIR dataset DOI 10.5281/zenodo.18269172, January 2026.

**Status:** opened. **Limit:** This verifies a locator, not data contents or a license.

## S08 — OpenTextile-NIR — dataset DOI/Zenodo landing
https://doi.org/10.5281/zenodo.18269172

**Supports:** Candidate raw-data source; resolve metadata, mean spectra, manifest and license first.

**Status:** locator_verified_files_not_retrieved. **Limit:** Zenodo direct record/API could not be opened in this research session. Runtime access is an explicit gate, not an assumed success.

## S09 — JRC141441 report — textile recyclability and feedstock requirements
https://publications.jrc.ec.europa.eu/repository/bitstream/JRC141441/JRC141441_01.pdf

**Supports:** Table 5, printed page26 / physical PDF page30, contains process-specific fibre thresholds based on WRAP information.

**Status:** opened_and_table_image_inspected. **Limit:** Table is a 2024 snapshot, not a universal current industrial standard. Other requirements also apply. Includes >=95% polyester among several profiles.

## S10 — Feedstock Activation Europe case study
https://www.fashionforgood.com/case-study/feedstock-activation-europe/

**Supports:** Heterogeneous post-consumer feedstock and recycler specifications; examples of composition-based sorting.

**Status:** opened. **Limit:** Industrial need evidence; not evidence of our algorithm or environmental savings.

## S11 — T-REX project reporting
https://cordis.europa.eu/project/id/101060343/reporting

**Supports:** Textile-to-textile value chain, quality feedstock and sorting challenges.

**Status:** opened. **Limit:** Use exact reporting period and verified text for quantitative claims.

## S12 — Automatisierte Textilsortierung — Status quo, Herausforderungen und Perspektiven
https://link.springer.com/article/10.1007/s00506-023-01004-5

**Supports:** Existing automated textile sorting, composition, contaminants and limitations.

**Status:** opened. **Limit:** Prior art seed; not a completed survey of selective routing.

## S13 — scikit-learn — cross decomposition
https://scikit-learn.org/stable/modules/cross_decomposition.html

**Supports:** PLS and related low-compute candidate baselines.

**Status:** opened. **Limit:** Candidate, not a predetermined best algorithm. Check pinned version APIs.

## S14 — scikit-learn — cross-validation
https://scikit-learn.org/stable/modules/cross_validation.html

**Supports:** Grouped splitting and evaluation methods.

**Status:** opened. **Limit:** An API choice does not prove this dataset satisfies independence assumptions.

## S15 — Learn then Test: Calibrating Predictive Algorithms to Achieve Risk Control
https://arxiv.org/abs/2110.01052

**Supports:** Existing statistical risk-control framework and assumptions.

**Status:** opened. **Limit:** Read full methods before implementation; not an automatic industrial risk guarantee.

## S16 — Conformal Risk Control
https://arxiv.org/abs/2208.02814

**Supports:** Existing conformal risk methodology.

**Status:** opened. **Limit:** Clarify the exact risk and expectation/probability statement; not interchangeable with accepted-set precision.

## S17 — Conformalized Quantile Regression
https://arxiv.org/abs/1905.03222

**Supports:** Candidate prediction-interval approach.

**Status:** opened. **Limit:** Marginal interval coverage is not selective precision or batch purity.

## S18 — MAPIE — official documentation
https://mapie.readthedocs.io/en/stable/

**Supports:** Current uncertainty, calibration and risk-control tools.

**Status:** opened. **Limit:** Version-specific API; toolkit use alone is not a contribution.

## S19 — MAPIE — precision control for a binary classifier
https://mapie.readthedocs.io/en/stable/generated/risk_control/1-quickstart/plot_risk_control_binary_classification/

**Supports:** Direct existing comparator for a selective eligibility system.

**Status:** opened. **Limit:** Follow statistical assumptions and data-split requirements; apply only if data supports it.

## S20 — Codex / ChatGPT models
https://learn.chatgpt.com/docs/models

**Supports:** Model IDs gpt-6-sol, gpt-6-luna, gpt-6-astra; availability must be checked locally.

**Status:** opened. **Limit:** Plan/client/account may differ; explicit effort values still require local verification.

## S21 — Codex — subagents
https://learn.chatgpt.com/docs/agent-configuration/subagents

**Supports:** Project agent TOML format, model/effort override, concurrency and inherited approvals.

**Status:** opened. **Limit:** Configuration format can evolve. Native available tooling, not fictitious tool calls, is authoritative.

## S22 — Codex — AGENTS.md
https://learn.chatgpt.com/docs/agent-configuration/agents-md

**Supports:** Path-scoped instructions and bounded instruction context.

**Status:** opened. **Limit:** Keep root concise and do not overwrite pre-existing/global instructions.

## S23 — Codex — non-interactive mode
https://learn.chatgpt.com/docs/non-interactive-mode

**Supports:** codex exec, output artifacts, scriptable sessions and failure handling.

**Status:** opened. **Limit:** Runner flags must be checked with installed --help; no permission bypass.

## S24 — Codex — git worktrees
https://learn.chatgpt.com/docs/environments/git-worktrees

**Supports:** Isolated changes and integration workflow.

**Status:** opened. **Limit:** Worktrees are optional for a small local project; one writer per file still matters.

## S25 — Codex ExecPlans for long-running tasks
https://developers.openai.com/cookbook/articles/codex_exec_plans

**Supports:** Living self-contained plans, milestones and validation.

**Status:** opened. **Limit:** Adapt the pattern; do not copy unnecessary long templates into every agent context.

## S26 — Effective harnesses for long-running agents
https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents

**Supports:** Initializer plus incremental sessions, persistent progress, explicit tests and end-to-end checks.

**Status:** opened. **Limit:** Practice report, not a guarantee of elapsed time or research correctness.

## S27 — How we built our multi-agent research system
https://www.anthropic.com/engineering/multi-agent-research-system

**Supports:** Bounded delegation, tool use, evaluation and context tradeoffs.

**Status:** opened. **Limit:** Different product/workload; borrow principles, not performance estimates.
