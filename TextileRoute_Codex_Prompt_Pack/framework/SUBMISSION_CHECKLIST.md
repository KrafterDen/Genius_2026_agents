# Deliverables: distinguish required, supporting and unresolved

Refresh the rules in `framework/GENIUS_REQUIREMENTS.md`; this is a preparation inventory, not a claim of guaranteed 2027 compliance. Every artifact has status `not_started/draft/validated/needs_human/blocked`, destination, rule source, validator and checksum.

## A. Ukrainian national application — published AI baseline, recheck 2027
- Ukrainian written report in DOCX and PDF, same content; PDF no more than 5 MB. Published limit: 15 pages including appendices, excluding title/references; Calibri or Arial 11/12, 2.5 cm margins. User explicitly requests Ukrainian. Count sections from the rendered PDF, not estimated word count.
- Report sections covering environmental problem and literature, question and contribution, audited data, methods/AI, experiments and results, cost/scalability, environmental scope, limitations, conclusion and actual references. Add truthful contributions/AI assistance even if the national template does not explicitly list the international section.
- English narrated working-model screen demonstration no more than 5 minutes. Prepare a <=180-second master suitable for the shorter international limit as well, with separate national YouTube-title metadata `GENIUS AI Ukraine_YEAR_TITLE`. Verify current punctuation/format when submitting.
- Real video URL reachable under current organizer rules; publishing requires user consent. Until published, keep a tested MP4 and an explicit `URL_PENDING` release blocker, not a fake link.
- Current application fields and project abstract/title, actual participant/school/mentor information, affiliation or self-registration route, declarations/consents only as actually required in the portal. Record exact requirements rather than inventing a universal form. Age/school eligibility and duplicate-registration prohibition verified separately.
- A national final presentation package prepared provisionally; the latest home page leaves the final format undecided. Do not apply old in-person 2026 instructions as confirmed 2027 rules.

## B. International-ready package — not all national requirements
- English research PDF <=20 pages TOTAL, including cover and references; follow current official AI paper template. Editable DOCX is a useful companion, not the international required upload.
- Title/actual student school metadata; abstract <=250 words; introduction; research goal/question; AI system and data; results/evaluation; cost/scalability; conclusion; optional acknowledgments; mandatory truthful student roles and external contributions; verified references.
- Current template baseline: Calibri/Arial/Helvetica 10/11 pt, margins >=2 cm, single or 1.15 spacing; references may be 9 pt, title 14 pt bold. Every figure has an explanatory caption and source/tool attribution. Recheck downloaded template.
- English narrated video <=180 seconds, problem + actual technology/AI contribution + working model; YouTube link after approval.
- Finals presentation <=5 minutes plus a 4–5 minute Q&A preparation; PPTX and PDF backup, local demonstration/video backup. Current AI category says **no posters**. A poster is not a mandatory deliverable here. Do not import Coding's separate hackathon rules.

## C. Supporting research assets — recommended, not invented organizer mandates
- Source-code archive with license notices, installation/reproduction instructions, pinned dependencies and small legal smoke fixtures.
- Dataset card, model card, acquisition/license manifest, split manifest, configuration, exact result ledger, environment and actual resource measurements.
- Legally shareable fitted models and representative sample outputs; do not redistribute restricted raw data.
- Bibliography/BibTeX and claim-to-source index; closest-work comparison and novelty scope.
- Ukrainian/English short and extended abstract drafts, a glossary, 30–60-second pitch and one-paragraph plain-language problem statement.
- Timed English narration, shot list, SRT subtitles, demo capture script, video provenance and encoding/duration verification.
- Defense workbook: explain NIR versus photos, weak labels, grouping, baselines, selective risk, sample size, economic/environmental limits, personal contribution; anticipated critical questions and evidence-based answers.
- Actual student/AI contribution logs, unsent clarification emails if necessary, private final application checklist.

## D. Automated release checks
Build both PDFs from frozen numbers; render every page and inspect for clipping, missing Cyrillic, figure readability and page-limit interpretation. Check DOCX/PDF content agreement and PDF byte size. Check references exist and support the statement, all citations resolve, no unfilled result placeholders, and no numeric disagreements among report/app/slides. Check video duration using a real media probe, subtitles and voice status. Remove private data from public/supporting archives. Verify license scope, checksums, fresh-install smoke test and offline demo. Save `submission/manifest.json` and `submission/readiness.json` with specific remaining human actions. Never automatically mark `submitted=true`.
