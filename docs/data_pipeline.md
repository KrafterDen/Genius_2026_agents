# B05 OpenTextile local data path — implementation draft

**Status on 2026-09-25:** code and schemas have been reviewed statically. The preparation command, leakage tests, real-data smoke and runtime/memory measurement have **not** been executed under the current no-tests instruction. B05 remains `needs_revision`; none of the paths below implies a validated output or model result.

## Source and scope

The only accepted input is the [OpenTextile-NIR v1.0 Zenodo record](https://zenodo.org/records/18269172), DOI `10.5281/zenodo.18269172`, CC BY 4.0, with four small tables at `data/raw/open_textile_zenodo_18269172/`. B03 retrieved and independently audited the source files. The local ignored `data/manifests/dataset_manifest.json` and tracked `configs/open_textile_v1_sources.json` must agree on published MD5, local SHA-256 and sizes; the loader hashes every source byte before parsing. No download, cube read, pickle, executable source script or model fit occurs in the preparation code. The two other small source files remain available to audit but are not inputs to this pipeline.

The [source article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12925456/) describes corrected mean SWIR reflectance for each cut textile piece. The release's numeric headers are interpreted as nanometres from that source account and the B03 audit, not from a unit printed in the CSV. The fixed v1.0 contract requires 288 increasing wavelengths beginning at 953.04 nm and ending at 2547.64 nm, 71 unique `Label` IDs, matching keyed IDs in all four tables, finite fractional reflectance in `[0,1]`, valid SWIR ROI bounds and RGB means in `[0,255]`. It rejects another release, scale, column order or incomplete row rather than silently rescaling. Source hashes also pin the entire wavelength grid. A source with scientifically meaningful negative calibration excursions needs a documented new contract, not clipping here.

## Data boundaries

`src/textileroute/data/open_textile.py` produces immutable `Piece` records. `spectrum_reflectance` is the **only** spectral feature vector. `reported_percent`, author-defined cotton+wool+lyocell share, `Label`, `label_status`, parent group, fold ID, source residual flag, ROI, RGB, colour and texture are context or targets, never appended to that vector. The 11 whole-dataset model-residual source flags remain in the 68 nominally labeled primary rows. Three wholly unknown composition rows remain missing targets, not zeros or negative examples. Blank fibre cells become conditional zeros only when a nominal row's reported shares sum to 100. Supplier reports are not chemical assays.

`src/textileroute/data/splits.py` reads the exact B04 allocation in `protocol/split_plan.json`; it first requires the frozen file SHA-256 `f39f304523ffecb130541de7194a2bdfb3e3f0564313ab0c137b427aad1196c7`, then verifies all observed parent groups occur once across five folds. Both `sample_45` pieces map to parent `45`. No allocator reads labels or recomputes a favorable split. There is no sealed final set; these are exploratory internal folds.

`src/textileroute/spectra/transforms.py` preserves the provided mean reflectance as the identity candidate. The optional preregistered source-informed PLS transform takes `−log10(max(R, 10⁻⁶))`, applies Savitzky–Golay smoothing with window 9, degree 2, `mode="interp"`, retains 1411–2536 nm bands, then performs per-piece SNV with population standard deviation. It reports how many values met the reflectance floor. This transform has no fitted cross-piece state. A separate feature standardizer requires explicit training and held-out parent IDs, rejects overlap and fits means/scales on training rows only. Later estimator fitting and inner tuning still need their own group-boundary implementation; this module alone does not certify absence of leakage.

## Prepared output contract

The unexecuted command is:

```sh
python scripts/prepare_data.py
```

If successfully run under a future request that authorizes the B05 checks, it is designed to write `data/processed/open_textile_v1/wavelengths_nm.json`, `spectra.jsonl`, `metadata.jsonl` and `provenance.json`, plus `data/splits/open_textile_v1_frozen_outer_folds.json`. These are gitignored derived files. Each `spectra.jsonl` record has only `piece_id` and the 288-value `spectrum_reflectance`; target, residual flag, group, fold, ROI, RGB and text reside in `metadata.jsonl` and join only by `piece_id`. Future estimator code must select the spectral vector explicitly and apply the frozen group mapping. Canonical JSON serialization and content-hash comparison reject a different existing artifact. The same-directory temporary file is flushed before a hard-link publication attempt, which avoids `os.replace` silently overwriting a destination another writer created; same-content preexisting files may be reused. An unsupported hard-link operation stops preparation without replacing a destination. The split output uses a repository-relative protocol locator, so an absolute checkout path cannot change its bytes. Provenance records input hashes, B04 protocol hash, B04 split-plan hash through the split file, tracked pin hash, implementation hashes keyed by repository-relative paths, derived hashes, source DOI/license and counts. A partial failure can leave already-written matching artifacts; inspect the error and rerun only after correcting the source or destination, never edit the source data silently. This is code intent, not observed command behavior.

The raw numeric matrix has `71 × 288 × 8 = 163,584` bytes if later represented as float64; this is arithmetic for the spectra alone, not a process memory measurement. CSV strings, objects and JSON increase actual resident memory. No measured runtime, peak RSS or fresh-environment reconstruction exists yet.

## Acceptance ledger and limits

| B05 gate | Current evidence | State |
| --- | --- | --- |
| Clean command reconstructs from verified inputs | Source and pin are available; command written, not run | Unverified |
| Independent groups do not cross splits and deliberate violations are caught | Frozen map and rejecting code reviewed statically; tests prohibited | Unverified |
| Units, missing labels and preprocessing state are checked | Explicit code paths and source schema reviewed statically | Partially evidenced; executable gate unverified |
| Real smoke and memory measurement fit machine | Neither executed nor measured | Unverified |

The standardizer's caller-provided group IDs are checked for disjointness, but the method does not independently prove they came from the frozen split or correspond to the supplied spectrum rows. B06 integration must build those arrays from the validated piece-ID map, and deliberate violation checks are still required for B05's leakage gate. A static claim that the function alone prevents all leakage would be false.

The B04 exploratory method, source-label uncertainty, unknown supplier dependence and absent whole-item truth still apply. No result or risk guarantee follows from preparing data.
