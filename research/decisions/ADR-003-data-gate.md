# ADR-003 — Narrow the data target after the real-file audit

**Date:** 2026-09-25  
**Status:** accepted for current local work; reopen if stronger source files become accessible

## Decision

Proceed with the verified small OpenTextile-NIR v1.0 files as an **exploratory, grouped dataset and reproduction study** (H02-2). Do not advertise H02-1's selective false-acceptance guarantee or any industrial routing result from this dataset. The profile counts in `protocol/target_feasibility.csv` remain descriptive, supplier-label composition proxies. The final title and external claims must reflect the narrowed question. NIST NIR-SORT Source A/B is the priority replacement candidate once its sample table, rights and spectra are actually retrieved and specimen-level threshold counts pass inspection.

## Alternatives and decisive evidence

1. **Keep proposed risk-controlled 2024 recycler proxy on OpenTextile.** Rejected as a confirmatory claim. The real files provide only 6 unflagged nominal ≥80% cotton positives and 10 nominal ≥95% polyester positives. At 80%, two report the boundary exactly; at 95%, 94–95% examples are absent and most positives are 100%. Labels are supplier/manufacturer metadata, not assays. Train, selection, calibration and final evaluation cannot all have adequate independent positive groups. A zero-error observation in all 10 nominal polyester positives would still have a one-sided 95% risk upper bound near 25.9%, before any partitioning. This does not rule out a clearly labeled descriptive demonstration.
2. **Use NIST NIR-SORT 2.0 now.** Potentially better controlled source A/B and 113 physical fabrics, but specimen metadata and the small actual license file have not yet been retrieved from the NIST data distribution endpoint. The metadata API and public license link are available. The official data.gov mirror pointer is recorded. The headline fabric count cannot replace profile-specific independent positive/negative counts. No NIST model or target decision is made until the files are audited.
3. **Wait for HyperTex.** Its files are embargoed until 2026-09-30 and its stated captures are not proven independent items. Waiting would not advance the current local audit. Recheck later if available.
4. **Pure-versus-blend or published PLS reproduction on OpenTextile.** Supported as a narrowly scoped exploratory question if a later authorized scientific execution stage is reached. Prior art already covers PLS natural-fibre prediction on this dataset, so the contribution is protocol, provenance and limits, not a new estimator. A negative reproduction remains a valid outcome.
5. **Switch to FasTEX/KCL v3.** Its 137 pure-fibre specimens and CC BY 4.0 terms provide a useful reference library, but its ATR-FTIR modality and lack of mixture percentages do not answer this NIR blend-composition question. Do not pool it with SWIR without a separate transfer question.

## Consequences and gates

OpenTextile files and CC BY 4.0 rights were verified by source checksum. Count physical pieces and conservative parent groups, never pixels. Unknown and model-derived outlier labels stay explicit. No blank component becomes a laboratory-confirmed zero. Keep all listed non-composition acceptance conditions unknown. Do not fit, tune or inspect any final evaluation here; B03 has no performance result. Next design work may describe a future grouped protocol but must respect the current no-tests instruction and may not imply tests were run.

The decision is revisited only with new auditable data or a narrowed scientific question. No paid acquisition, account creation, author contact, dataset fabrication or unauthorized model execution is implied.

## References

Primary [OpenTextile dataset record](https://zenodo.org/records/18269172) and [article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12925456/); [NIST dataset](https://data.nist.gov/od/id/mds2-3325), [NIST descriptor](https://www.nature.com/articles/s41597-026-07434-6) and [data.gov mirror pointer](https://catalog.data.gov/dataset/near-infrared-spectra-of-origin-defined-and-real-world-textiles-nir-sort-a-spectroscopic-a); [HyperTex record](https://zenodo.org/records/21489250). Full command/output trace and hashes are in `protocol/data_audit.md`, `protocol/data_audit.json` and `data/manifests/dataset_manifest.json`.
