# [Remote Subagents (experimental)](http://geminicli.com/docs/core/remote-agents.md)


Gemini CLI supports connecting to remote subagents using the Agent-to-Agent
(A2A) protocol. This allows Gemini CLI to interact with other agents, expanding
its capabilities by delegating tasks to remote services.

Gemini CLI can connect to any compliant A2A agent. You can find samples of A2A
agents in the following repositories:

- [ADK Samples (Python)](https://github.com/google/adk-samples/tree/main/python)
- [ADK Python Contributing Samples](https://github.com/google/adk-python/tree/main/contributing/samples)

<!-- prettier-ignore -->
> [!NOTE]
> Remote subagents are currently an experimental feature.