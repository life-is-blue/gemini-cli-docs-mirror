## What are hooks?

Hooks run synchronously as part of the agent loop—when a hook event fires,
Gemini CLI waits for all matching hooks to complete before continuing.

With hooks, you can:

- **Add context:** Inject relevant information (like git history) before the
  model processes a request.
- **Validate actions:** Review tool arguments and block potentially dangerous
  operations.
- **Enforce policies:** Implement security scanners and compliance checks.
- **Log interactions:** Track tool usage and model responses for auditing.
- **Optimize behavior:** Dynamically filter available tools or adjust model
  parameters.