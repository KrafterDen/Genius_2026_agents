# Research protocol — browse before material external claims

Search when a decision depends on current requirements, software/API behaviour, dataset availability/licensing, recycler criteria, performance comparisons or unfamiliar scientific facts. Do not substitute model memory for research. Basic arithmetic and reasoning from inspected data do not need a web query. Use current verified primary material: organizer pages, original papers/data records, authors' implementations and official documentation. Search snippets are discovery aids, not sufficient proof of a quantitative claim.

## Evidence record
Store source ID, title, authors/organization, publication/update date if known, access date, URL/DOI, exact page/section/table, claim supported, limitations, and retrieval status. Distinguish `opened`, `metadata_only`, `inaccessible`, `superseded`. A creator page can verify a DOI without proving the dataset license or contents. For PDFs inspect the actual page image for tables and formatting; record physical and printed page numbering. Do not invent citations or use citation placeholders as references.

Use `research/search_log.jsonl` for query, search tool, timestamp, selected/excluded results and unresolved issue. Maintain `research/claims.csv`: claim text, source IDs, measured/derived/assumed, quantitative basis, status, allowed wording. A failed search is recorded as inconclusive, not "no prior art".

## Initial prior-art search families
Search combinations of textile/NIR/SWIR sorting, fibre blends, feedstock specifications, open-set rejection, selective classification, calibrated probability, prediction intervals, conformity/risk control, review allocation, supplier label uncertainty and grouped validation. Search relevant non-English textile terms when useful. Follow references backward and citing work forward. Identify the closest methods, not merely a large bibliography; aim for 10–20 genuinely relevant works if available, record a smaller result honestly.

For each near neighbour compare problem, measurement, labels, independence unit, baseline, metric, uncertainty target, code/license and overlap with our contribution. Classical spectroscopy and older chemometrics are valid competitors. A recent model is not automatically better. An industry case study establishes a practical need, not a causal emissions saving.

## Freshness and deduplication
Recheck the organizer at blocks 01, 16/17 and 19, plus immediately before real submission. Recheck version-specific APIs before first integration or after an upgrade; store a lockfile. Recheck a recycler threshold before calling it current. Reuse valid source records for unchanged facts instead of making each subagent browse identically. Source retrieval is not authorization to upload the user's files to that service.

## Resolving disagreement
Prefer the rule for the exact category, stage and season. Log conflicts between generic pages and category templates. Ukrainian and international requirements are separate. Where an organizer must clarify, prepare an unsent question with source quotations kept short and actual contact details verified online. Continue draft preparation with a conservative layout; do not assert unresolved eligibility or compliance.

## Challenger output
Give at least one serious simpler alternative and the closest published method. Specify what evidence would make our candidate unnecessary, a minimal comparison, limitations of source relevance, and whether the proposed result is new method, new evaluation, integration or reproduction. The orchestrator must respond in a decision record. No novelty badge without evidence.
