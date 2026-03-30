# [Subagents (experimental)](http://geminicli.com/docs/core/subagents.md)


Subagents are specialized agents that operate within your main Gemini CLI
session. They are designed to handle specific, complex tasks—like deep codebase
analysis, documentation lookup, or domain-specific reasoning—without cluttering
the main agent's context or toolset.

<!-- prettier-ignore -->
> [!NOTE]
> Subagents are currently an experimental feature.
> 
To use custom subagents, you must ensure they are enabled in your
`settings.json` (enabled by default):

```json
{
  "experimental": { "enableAgents": true }
}
```