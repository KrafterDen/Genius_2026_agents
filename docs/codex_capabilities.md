# B00 Codex capability record

Observed on 2026-09-25 with installed `codex-cli 0.149.0`, official OpenAI documentation, and bounded desktop subagents.

| Surface | Requested role | Observed result |
|---|---|---|
| Current desktop task | GPT-6 Sol High orchestrator | Requested by pack; this task does not expose a reliable self-model/effort identifier to the repository. Record as unverified, not asserted. |
| Desktop native subagent | GPT-6 Sol Medium | Explicit spawn accepted and read-only official-doc review returned. |
| Desktop native subagent | GPT-6 Luna Xhigh | Explicit spawn accepted for read-only template audit; result recorded in B00 report. |
| Desktop native subagent | GPT-6 Astra High | Not invoked; availability unverified. |
| CLI with ChatGPT account | GPT-6 Sol High | Rejected with HTTP 400: model not supported through this CLI/account path. |
| CLI with ChatGPT account | GPT-5.6 Sol High/Medium | Both harmless invocations succeeded. Used as explicit CLI fallback. |
| CLI with ChatGPT account | GPT-5.6 Luna Xhigh | Harmless invocation succeeded. Used as explicit CLI fallback. |
| CLI with ChatGPT account | GPT-6 Astra High | Not tested; inactive `.toml.example` retained. |

The project `.codex/config.toml` and active `.codex/agents/*.toml` use the tested CLI fallback models and explicit efforts. The native desktop collaboration tools worked in this task. A strict no-model-override CLI invocation selected the project config model `gpt-5.6-sol`. Project-local role files were present during strict CLI execution, but a CLI subagent spawn was not independently exercised; `.agent/runtime/runner_config.json` records `native_subagents_verified=false`. The optional runner uses Codex's native machinery and does not implement its own multi-agent platform.

[Official OpenAI documentation on subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) supports project `.codex/agents/*.toml` roles and the `[agents]` settings used here. [Configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic) describes project configuration loading and precedence. [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) documents `codex exec` and its read-only default. [Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees) requires a Git repository for isolated checkout workflows. Local CLI help and invocation evidence are in `docs/validation/cli_checks.txt`; documentation alone did not establish account availability.

No administrator install, paid API key, global Codex edit or permissions bypass was used. The local runner configuration is valid only for this installed CLI version; the runner checks the version before execution.
