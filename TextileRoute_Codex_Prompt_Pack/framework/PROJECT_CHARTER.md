# Project charter — TextileRoute (working name, not a novelty claim)

## User objective
Develop an honest, reproducible GENIUS Olympiad AI research project and a working local demonstration that help route end-of-life textiles toward an appropriate recycling process. Minimize routine human intervention while preserving real student contribution and all required permissions. Working horizon: roughly 4–6 weeks on an existing RTX 2060-class personal computer; inspect actual hardware and operating system rather than assuming them.

## Candidate research question
Under a specified and sourced recycler fibre-composition requirement, can a decision system increase useful automatic routing while limiting incorrectly accepted items and the burden of manual review, compared with strong, simple existing methods?

This is a candidate, not a conclusion or a fixed architecture. A web-research challenger must question the target, data, baselines, uncertainty method and claimed contribution. Generic rejection, conformal prediction, composition regression and NIR sorting already exist. A different application or a recent dataset alone is not methodological novelty.

## Intended inputs and outputs
Input: a measured NIR spectrum, acquisition metadata, and an explicitly defined recycler profile. Optional spatial spectra and photographs only if justified. A photograph must never be presented as a chemical assay. Output: ACCEPT, REVIEW, or NOT ELIGIBLE FOR THIS PROFILE, with the scope of the decision, uncertainty, missing requirements and evidence. UI wording may use REJECT internally but must not imply that a rejected item should be landfilled.

Fibre eligibility is only one part of actual recyclability: dyes, finishes, buttons, layers, elastane, moisture, degradation and equipment matter. Report which variables were and were not observed. The software is a research prototype, not an industrial safety or quality certificate.

## Candidate starting point
Inspect OpenTextile-NIR metadata and mean spectra first. Start with grouped, low-compute baselines such as PLS regression, ridge/SVR, direct binary eligibility classification, and confidence-based rejection. Consider risk-control or conformal methods only with appropriate assumptions and sample sizes. A small neural model is optional, not a requirement. Decide after the data audit and independent alternatives research.

## Boundaries
No custom spectrometer purchase, cloud GPU rental, paid API subscription, public deployment, automatic submission, or outreach is pre-authorized. Local reproducible experiments and public-source reading are in scope. No claim of guaranteed acceptance risk, saved tonnes, emissions reductions or industrial validation without appropriate evidence.

## Definition of success
A defensible question; licensed and audited data; leakage-resistant evaluation; a direct comparison with existing methods; honest positive, negative or inconclusive findings; working offline demonstration; verified report and submission materials; a truthful statement of student and AI contributions. A failed novelty hypothesis must change the claim, not the evidence.
