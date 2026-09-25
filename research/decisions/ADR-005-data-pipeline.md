# ADR-005 — Source-verified piece-level means and frozen groups

**Date:** 2026-09-25  
**Status:** provisional implementation choice; B05 acceptance blocked by unrun gates

Use the four verified OpenTextile v1.0 small tables, keyed by `Label`, with the 288-band mean SWIR reflectance vector as the only model input. Parse with stdlib CSV/JSON, verify bytes against both ignored B03 manifest and tracked source pin, carry 71 physical pieces and their original missing/flag status, and load B04's exact parent-group fold map. Persist canonical JSON/JSONL locally with source, protocol and implementation hashes. Preserve an identity spectrum option and isolate the fixed per-piece source-informed PLS transform from any fitted cross-piece standardization.

Independent alternative search is recorded in `research/challenges/05_pipeline.md`. Cube or pixel expansion might study spatial heterogeneity but would add many correlated observations and unverified acquisition complexity without answering B04's piece-level supplier-label question. RGB fusion has a different ROI and no demonstrated fibre-specific gain, so it is context only. A binary array cache is unnecessary at 71 × 288 and would create an extra hash/schema boundary. Recomputing folds with a generic group splitter would violate the frozen B04 assignment. These choices follow the source article, B03 audit and official Python/SciPy/scikit-learn behavior, not an assumption of measured model performance.

Consequence: this path is small and auditable, but the source nominal labels, missing true chemistry, hidden supplier grouping and absent final set still limit any future result. Current testing prohibition prevents B05's clean reconstruction, leakage-violation and real smoke/memory gates; B05 remains `needs_revision` with no claim that implementation works in execution.
