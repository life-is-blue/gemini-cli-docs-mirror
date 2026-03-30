## What are subagents?

Subagents are "specialists" that the main Gemini agent can hire for a specific
job.

- **Focused context:** Each subagent has its own system prompt and persona.
- **Specialized tools:** Subagents can have a restricted or specialized set of
  tools.
- **Independent context window:** Interactions with a subagent happen in a
  separate context loop, which saves tokens in your main conversation history.

Subagents are exposed to the main agent as a tool of the same name. When the
main agent calls the tool, it delegates the task to the subagent. Once the
subagent completes its task, it reports back to the main agent with its
findings.