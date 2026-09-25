# Next action — B01 rules and problem

B00 is complete. No dataset has been downloaded or model trained; `submission_ready=false`. B01 is the active, unstarted block.

From this repository root, run this exact read command before continuing in Codex:

```sh
cat STATUS.json .agent/execplans/B01.md TextileRoute_Codex_Prompt_Pack/prompts/01_RULES_AND_PROBLEM.md
```

Then execute that prompt in the current Codex task. In a **separate future CLI session**, the optional sequential runner can execute B01 with this exact command after inspecting its config and the pack README:

```sh
.venv/bin/python TextileRoute_Codex_Prompt_Pack/tools/run_blocks.py --repo . --from-block 1 --to-block 1 --max-blocks 1 --execute
```

Do not run the optional runner recursively inside an active Codex block. Recheck the CLI version/model config if the installed Codex or account changes. B01 should first verify current contest rules and target wording, then leave evidence and its own block state.
