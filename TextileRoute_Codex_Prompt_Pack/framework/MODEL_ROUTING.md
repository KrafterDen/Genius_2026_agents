# Model routing and context economy

## Preferences requested by the user
| Role | Model | Reasoning effort | Typical work |
|---|---|---|---|
| Orchestrator / integrator | `gpt-6-sol` | `high` | Own the plan, synthesis, acceptance gates, integration and decisions. |
| Bounded executor | `gpt-6-luna` | `xhigh` | Mechanical extraction from known sources, tests against a fixed contract, formatting, adapters, manifest checks, translations after scientific content is frozen. |
| Researcher / method engineer | `gpt-6-sol` | `medium` | Ambiguous literature search, modelling choices, implementation involving statistical judgement, debugging across components. |
| Scientific red team | `gpt-6-astra` | `high` | Selective-risk validity, tiny-sample inference, strongest novelty objection, contamination/leakage audit, final high-stakes claims. |

Model IDs are documented in the current Codex model guide, but availability and accepted efforts depend on the installed client, plan and session. Bootstrap must verify them. Display names are not a license to invent tool arguments. Always specify both model and effort. Do not silently execute every worker on the orchestrator model. If a model is unavailable, record the actual substitute and why. If native delegation is unavailable, use a sequential, explicitly labelled role pass; never pretend another model ran.

## Economy rules
The orchestrator reads compact state, relevant source records and artifact summaries, not every full paper or child transcript. Pass a scoped task packet, exact file paths, known facts versus hypotheses, and acceptance tests. Default worker return: 400–800 words maximum plus artifact paths, source IDs, commands/results and unresolved issues. Long evidence belongs in files. Do not ask for hidden reasoning or chain-of-thought; request conclusions, assumptions and verifiable calculations.

Default at most 3 live subagents, normally 2; one GPU experiment and at most one heavy CPU job. Close completed agents. Use Luna for an unambiguous patch even if the whole project is complex. Use Sol Medium when a literature comparison requires judgement. Escalate to Astra for a concrete unresolved scientific question, not general browsing or report polishing. One Astra audit per relevant gate is usually sufficient. No recursive spawning unless the orchestrator records a specific need and bounds it.

Before spawning, ask whether a short command or an already indexed source answers the question. Do not send the entire pack or all 250 old ideas. Maintain a source cache and decisions ledger. Reopen sources when facts are time-sensitive or a new choice depends on them; do not repeat identical searches merely because a new worker starts.

## Suggested escalation triggers
Escalate when a claimed guarantee has unclear conditioning, the same item may cross splits, label uncertainty changes the target, the closest paper appears to subsume the contribution, or two independent implementations disagree. Downgrade after the uncertainty is resolved. Roles and worker allocation in each block are suggestions; change them with a short recorded rationale, preserving independent review.

## Budget controls
Record actual tool/model usage when the client exposes it; otherwise write `unknown`. Do not infer billed token counts or cost from elapsed time. Start with a soft ceiling of six scoped child dispatches per block and one Astra dispatch in audit blocks; exceed only for a recorded blocker, not unbounded brainstorming. The user may set stricter limits in `configs/resource_budget.json`. Never buy more credits or turn on paid services. Resource-limit failures produce a resumable checkpoint, not claims of completion.
