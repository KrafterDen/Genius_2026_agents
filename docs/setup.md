# Local bootstrap commands

From the repository root:

```sh
PYTHONPATH=src:. .venv/bin/python scripts/smoke.py
PYTHONPATH=src:. .venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_repository.py --repo . --require-block 00
```

B00 command output is saved in `docs/validation/`. Test fixtures are synthetic and exercise controls only. The optional sequential Codex runner remains an external, explicit `--execute` operation; do not launch it from inside a Codex block. Its local config is `.agent/runtime/runner_config.json`. Inspect the prompt pack's `tools/README.md` before using it in a separate session.
When refreshing the saved B00 validator log, do not redirect the validator directly into `docs/validation/validator.txt`: B00 lists that file as its own evidence. Capture to a separate temporary path, confirm exit 0, then copy the output into the tracked log.
