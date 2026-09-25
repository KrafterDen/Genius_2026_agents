# Next action — B05 audited data pipeline

B00–B04 passed. B04 froze an **exploratory grouped protocol** for 68 nominally labeled OpenTextile pieces in 67 conservative groups. Its primary endpoint is parent-group-equal MAE for the authors' cotton+wool+lyocell sum. No model was fit, no test was run, no untouched final set exists, and no formal selective-risk guarantee is claimed. The protocol SHA-256 and actual source access are in `.agent/block_reports/B04.md`. `submission_ready=false`.

From this repository root, run this exact read command before continuing in Codex:

```sh
cat STATUS.json NEXT.md TextileRoute_Codex_Prompt_Pack/prompts/05_DATA_PIPELINE.md
```

Then create `.agent/execplans/B05.md` and implement the data ingestion and grouping code within the frozen B04 protocol. Do not execute downloaded example scripts. Keep raw data gitignored and one writer per file. **Do not create, modify or run tests** under the current user/root AGENTS.md instruction, despite B05's expected test files and smoke gate. Record the gate as unverified or blocked rather than claiming B05 passed. Do not run the external runner recursively. If interrupted, B04's plan/report, protocol files and B03 manifest/raw files form the checkpoint.
