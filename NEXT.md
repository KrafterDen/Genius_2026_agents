# Next action — B05 acceptance gates

B00–B04 are passed. B05 is **`needs_revision`**: source-verified piece-level ingestion, transforms, exact B04 group-map reading, a prepare CLI and documentation have been written, but no B05 command or tests have been run. The current user/root `AGENTS.md` prohibits creating, modifying or running all tests unless this request explicitly asks for them. That includes the B05 leakage checks and real-data smoke execution. Do not convert static review into a passed gate or proceed to dependent B06–B19. No model was fit, no predictions were inspected, no final-test information was consumed, and `submission_ready=false`.

From the repository root, the exact recovery read command is:

```sh
cat STATUS.json NEXT.md .agent/execplans/B05.md TextileRoute_Codex_Prompt_Pack/prompts/05_DATA_PIPELINE.md
```

Review `.agent/block_reports/B05.md`, `docs/data_pipeline.md`, `research/challenges/05_pipeline.md` and ADR-005. The unexecuted future preparation command is `python scripts/prepare_data.py`; it is **not** an instruction to run a test under the present request. B05 gates require a new explicit user request for tests before real reconstruction, deliberate leakage checks and memory measurement can be recorded. Until then, preserve the checkpoint and original ignored raw files. The release still needs authentic student work, narration and publication approval; do not impersonate or publish.
