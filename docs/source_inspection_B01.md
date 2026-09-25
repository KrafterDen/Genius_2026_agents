# B01 source inspection record

Accessed 2026-09-25. Public source PDFs were fetched into gitignored `.agent/runtime/` for read-only inspection; no source PDF or dataset was added to the repository. Exact locators and metadata here make the inspection reproducible.

| Source | Local inspection | Locator and limit |
|---|---|---|
| [S09 JRC141441](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC141441/JRC141441_01.pdf) | 106 A4 pages, 3,133,155 bytes, SHA-256 `69bc7db8506092ef698233f7b41293e0bdc159c84d6552d9d066593d811f22b3`; physical PDF page 30 rendered and visually inspected | Printed p. 26 §2.4.1.1 Table 5 and printed p. 27 §§2.4.1.2–5. The text calls the criteria a 2024 snapshot. Table 5's polyester item omits a printed percent sign after 95; interpret cautiously in composition-percent context. |
| [S05 GENIUS AI paper template](https://geniuscountries.s3.us-east-2.amazonaws.com/GENIUS_AI_ResearchPaper.pdf) | 6 US-Letter pages, 269,287 bytes, SHA-256 `50ccb544ad3a43e5185e4b8c5a46d180546d4a7411c4ddeb9637e7089a0a1ee3`; text extracted, page 1 rendered and visually inspected by integrator; read-only reviewer reports visual inspection of all 6 pages | Template is six pages of instructions, not a six-page limit. P. 1 states 20 pages total for the submitted paper, <=250-word abstract, fonts/margins; pp. 2–6 list required sections and authentic roles/external assistance. PDF metadata creation date: 2026-08-30. |

The official international AI category links the template. The web fetch tool timed out on S05, while direct HTTPS retrieval succeeded. No rule was inferred from a search snippet alone. Organizer and operator HTML source locators appear in `docs/requirements_current.json` and `research/sources.jsonl`.
