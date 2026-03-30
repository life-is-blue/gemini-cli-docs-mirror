# [Model steering (experimental)](http://geminicli.com/docs/cli/model-steering.md)


Model steering lets you provide real-time guidance and feedback to Gemini CLI
while it is actively executing a task. This lets you correct course, add missing
context, or skip unnecessary steps without having to stop and restart the agent.

<!-- prettier-ignore -->
> [!NOTE]
> This is an experimental feature currently under active development and
> may need to be enabled under `/settings`.

Model steering is particularly useful during complex [Plan Mode](/docs/cli/plan-mode)
workflows or long-running subagent executions where you want to ensure the agent
stays on the right track.