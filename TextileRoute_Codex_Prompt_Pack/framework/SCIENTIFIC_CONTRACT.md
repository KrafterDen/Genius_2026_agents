# Scientific contract

## Measurement and population
The starting source describes 71 physical textile samples, not millions of independent garments. Inspect whether several specimens originate from the same garment or acquisition batch, and group at the highest identifiable dependent unit. Repeated pixels, spectra, views and augmented versions stay with that unit in every split. Supplier composition labels are reference metadata, not independently validated chemistry. Describe precisely what predictions are evaluated against.

NIR mainly measures the scanned region/surface; unknown backing, layers, trims and other unobserved requirements remain unknown. Do not infer a whole garment's chemical purity from RGB. Do not convert incomplete or rounded composition labels into exact zeroes. Preserve unknown fractions, label intervals and label provenance. Synthetic spectra or synthetic label perturbations may support explicitly labelled stress tests, never stand in for real held-out garments.

## Separate target quantities
1. Composition estimation error, per fibre and independent item.
2. Eligibility for a stated fibre-composition profile, relative to audited labels.
3. Selective false-acceptance risk: ineligible accepted items divided by accepted items.
4. Automatic acceptance coverage, review rate, false rejection and the review budget.
5. Mass contamination of a stream: a different quantity requiring item masses and material fractions.

If no items are accepted, precision/risk is undefined; coverage is zero. Reject-all is not a successful solution. Item counts do not become kilograms. Declared contamination tolerance depends on a specific process and source, not a universal 95% threshold.

## Statistical guarantees
Marginal 95% conformal coverage is NOT 95% precision among accepted items, an individual-item confidence certificate, or a batch-purity guarantee. Use an appropriate selective-risk method and state the exact finite-sample assumptions. Learn-then-test, binary precision control and calibrated reject baselines already exist and must be considered. Merely installing MAPIE is not a contribution.

As a sanity check, with zero failures in n genuinely independent accepted test items, a one-sided 95% binomial upper bound is `1 - 0.05**(1/n)`. It takes at least 59 such items to put that bound below 5%, and 299 below 1%. These numbers are a mathematical illustration, not evidence that a selected, shifted or repeated-fold sample satisfies the assumptions. Repeated folds do not multiply the number of independent samples. Never promise strong industrial bounds from a tiny benchmark. "Inconclusive with this sample size" is an acceptable finding.

## Evaluation design
Before final testing, freeze the hypotheses, independent units, metrics, recycler profiles, split strategy, model families, tuning bounds, calibration method, review budget, robustness analyses and decision criteria. Separate training, model/threshold selection, calibration and final evaluation without data reuse that invalidates the chosen method. With very few samples, justify a conservative grouped nested evaluation and explicitly downgrade claims; do not invent a large held-out test set.

Scalers, imputation, derivative settings if tuned, feature selection, PCA and hyperparameters fit only where allowed. A calibration set used to tune a rule cannot silently remain an untouched validation set. Account for multiple attempted risk thresholds when necessary. Log every run, including failure and negative findings. Final test results may diagnose a limitation but cannot select the advertised winner. Exploratory post-test work is separately labelled and needs new independent evidence for confirmation.

## Baselines and contribution
Mandatory serious candidates: no-AI/simple rule where possible; standard spectrum preprocessing plus PLS/Ridge/SVR or another justified classical learner; direct eligibility classifier with calibrated reject option; composition estimate plus process threshold; an existing risk-control approach when feasible. Compare using the same admissible data and budget. A small neural network is optional and must earn its complexity. The custom component must be ablated. Compare risk/coverage/review curves, not accuracy alone.

Do not select only convenient pure materials and then advertise blended-fabric threshold performance. Publish unsupported profile/mixture cases. If labels cannot support the main task, narrow within textile routing (for example pure-versus-blended identification or an explicitly exploratory decision benchmark), document the changed research question, and do not claim the original goal is achieved.

## Reproducibility and environmental claims
Save data/license manifests, group splits, environment lock, seeds, source code revision, configuration, fitted artifacts, actual runtime/memory and metric definitions. All official numbers must flow from a verified result ledger into reports, app and slides. Hypothetical scenarios are separate. No fabricated CO2 savings, tonnes recycled, endorsements, industrial trials or external expert reviews. Report the causal chain from better sorting to potential environmental benefit and which link was actually measured.
