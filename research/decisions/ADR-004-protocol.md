# ADR-004 — Exploratory grouped composition protocol, no formal risk claim

**Date:** 2026-09-25  
**Status:** accepted as a frozen analysis plan; no analysis executed

## Decision

Primary endpoint is parent-group-equal MAE for the OpenTextile authors' nominal cotton+wool+lyocell share across all 68 composition-labeled pieces in 67 conservative groups. Compare a source-informed PLS workflow against a training-fold constant median with one frozen five-fold outer group allocation and four-fold inner group tuning. Keep 11 source outlier flags in the primary population; three unknown rows are unscored. Polyester and cotton percentage estimates and historical composition-proxy decisions are secondary, descriptive analyses. No independent confirmatory final set, risk-controller calibration or ≤5% false-acceptance claim exists in the current data.

## Why this choice

The [source paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC12925456/) already models the same author-defined sum, providing a concrete PLS workflow to interrogate. Its outlier exclusion and complexity selection prevent its reported RMSE from serving as a like-for-like target. An independent Astra High challenger showed that the nominal threshold positives cannot support meaningful strict selected-set bounds, while a Sol Medium evaluation reviewer independently favored grouped nested comparison of all nominal labels. Original [grouped-CV documentation](https://scikit-learn.org/stable/modules/cross_validation.html), [LTT](https://arxiv.org/html/2110.01052v5) and [selection-specific conformal work](https://www.jmlr.org/papers/v24/22-1176.html) were checked for the different assumptions and estimands.

Alternative primary polyester-share MAE would be closer to the historical chemical-polyester proxy and has 34 distinct nominal values, but would not reproduce the source's exact outcome. It remains a predeclared secondary outcome. A dedicated train/tune/calibration/final allocation would leave very few positive groups and falsely imply an untouched final set despite B03's complete label inspection. A direct LTT/MAPIE precision controller requires independent credible calibration labels and exchangeability that are not established. A trivial review-all result yields no automatic coverage. No algorithmic novelty, mass purity or chemical truth is claimed.

## Consequences

The registered result may be positive, negative or inconclusive against supplier labels only. Every fit and preprocessing choice must remain inside group boundaries; all three listed methods, flags and failures must be reported. Selecting an advertised winner, threshold or data subset after seeing outer predictions makes that claim exploratory and requires new evidence for confirmation. Source hash, protocol hash, model environment, action definitions and any future access are logged separately. The current request bars tests, so the expected B04 metric-test artifact is intentionally omitted and cannot be cited as validation.
