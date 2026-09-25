# B01 problem evidence and conditional research question

As of 2026-09-25, this is a **candidate research problem**, not a demonstrated environmental solution.

## User decision and measurement
A textile sorter considering **non-rewearable feedstock** wants to know whether a measured region appears to meet a named recycler *fibre-composition* criterion. Input would be an NIR spectrum, acquisition metadata and a dated criterion. The research output would be **ACCEPT composition proxy**, **REVIEW** or **NOT ELIGIBLE FOR THIS PROFILE**, with an explicit statement of missing conditions. ACCEPT must never be presented as full-garment purity, an operator purchase decision or a disposal recommendation. Rewearable garments should be considered for reuse first; the JRC separates reuse streams from its recyclability assessment ([S09, §§2.3.2 and 2.4.3](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC141441/JRC141441_01.pdf)).

The prospective evaluation unit is the highest identifiable independent physical garment/specimen group. [OpenTextile-NIR's article (S06)](https://cris.vtt.fi/en/publications/introducing-opentextile-nir-near-infrared-hyperspectral-imaging-a/) describes 71 samples, millions of pixels and supplier-provided composition labels. It calls the collection post-industrial while also describing used garments from an end-of-life partner. The actual file manifest, group IDs, label intervals and license have not been audited. B03 must resolve whether an item-level, threshold-relevant evaluation is possible. Pixel count cannot increase the independent sample count.

**Conditional question:** On those audited independent sample groups for which a source-labelled composition target is identifiable, can a spectrum-based review policy improve automatic coverage at a stated false-acceptance rate *against supplier-label proxy eligibility* over simple spectral baselines, for a named historical profile? The supplier-label threshold defines the target, not a deployable comparator unless labels are available during sorting. An operator public preference can be explored only as a sensitivity case. The result may be inconclusive or the target may be abandoned if classes/boundaries are too sparse. No finite-sample industrial guarantee is promised.

## Why this decision is worth studying, and what is already done
[JRC141441 (S09), Table 5](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC141441/JRC141441_01.pdf) gives a 2024 WRAP-derived snapshot with distinct mechanical and chemical composition criteria, including >=80% cotton and >=95% polyester examples. The same report says disruptors, colour, layers and structure also determine suitability (§2.4.1). [Fashion for Good's FAE case (S10)](https://www.fashionforgood.com/case-study/feedstock-activation-europe/) describes heterogeneous post-consumer inputs and process-specific requirements, including elastane and pre-processing. [T-REX period-2 reporting (S11)](https://cordis.europa.eu/project/id/101060343/reporting) describes feedstock quality and pre-processing as challenges; it does not validate this prototype.

NIR composition routing itself is established: [Valvan (S30)](https://www.valvan.com/en/solutions/textile-sorting-recycling) describes fibre-concentration prediction and colour sorting, and [Matoha (S32)](https://matoha.com/configuring-the-material-indicator-led-fabritell) describes configurable composition thresholds. [Recover (S31)](https://recoverfiber.com/faqs) says blends and elastane need case-specific review. Thus 'NIR plus threshold' is **not** a novelty claim. The possible research contribution must come from a well-specified comparison, limitations analysis or demonstrably useful review policy, and B02 must challenge even that.

## Environmental causal chain and evidence boundary
1. NIR surface signal may help estimate a fibre-composition proxy. **Not measured yet by this project.**
2. A policy may label some audited specimens as composition-eligible with a review option. **No experiment yet; B03–B11 required.**
3. Real sorters would still assess reuse priority, colour, trims, layers, finishes, moisture and recycler-specific terms. **Not observed in the candidate dataset.**
4. Suitable feedstock would need real acceptance and processing. **No operator trial or contract.**
5. An environmental benefit would depend on displaced virgin production, process energy, transport and actual fate. **No mass flow, LCA or saved-emissions measurement.**

No stage beyond source-grounded problem definition has been verified. A photograph is not a chemical assay.

## Two illustrative traces, not measured samples or tests
- **Hypothetical A:** a declared 90% cotton / 10% polyester single-layer-looking item passes the JRC-2024 >=80% cotton *composition proxy* and is near Infinited's public ~88% cotton preference, but fails the JRC >=95% polyester proxy. It remains **REVIEW** for real acceptance until reuse priority, colour, hidden layers, trims, finishes and actual operator terms are checked.
- **Hypothetical B:** a declared 97% polyester / 3% elastane item passes the JRC-2024 >=95% polyester *composition proxy* and fails both cotton proxies. Real acceptance remains **REVIEW**: the source thresholds alone do not resolve elastane tolerance, coatings, trims, moisture or process-specific limits.

These traces illustrate how profile choice and unobserved requirements affect wording. They are not dataset observations, pipeline tests or evidence of performance.
