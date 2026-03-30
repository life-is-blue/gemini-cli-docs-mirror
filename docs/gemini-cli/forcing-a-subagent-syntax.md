### Forcing a subagent (@ syntax)

You can explicitly direct a task to a specific subagent by using the `@` symbol
followed by the subagent's name at the beginning of your prompt. This is useful
when you want to bypass the main agent's decision-making and go straight to a
specialist.

**Example:**

```bash
@codebase_investigator Map out the relationship between the AgentRegistry and the LocalAgentExecutor.
```

When you use the `@` syntax, the CLI injects a system note that nudges the
primary model to use that specific subagent tool immediately.