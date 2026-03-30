### Using hooks with Plan Mode

You can use the [hook system](/docs/hooks/writing-hooks) to automate parts of
the planning workflow or enforce additional checks when Gemini CLI transitions
into or out of Plan Mode.

Hooks such as `BeforeTool` or `AfterTool` can be configured to intercept the
`enter_plan_mode` and `exit_plan_mode` tool calls.

> [!WARNING] When hooks are triggered by **tool executions**, they do **not**
> run when you manually toggle Plan Mode using the `/plan` command or the
> `Shift+Tab` keyboard shortcut. If you need hooks to execute on mode changes,
> ensure the transition is initiated by the agent (e.g., by asking "start a plan
> for...").

#### Example: Archive approved plans to GCS (`AfterTool`)

If your organizational policy requires a record of all execution plans, you can
use an `AfterTool` hook to securely copy the plan artifact to Google Cloud
Storage whenever Gemini CLI exits Plan Mode to start the implementation.

**`.gemini/hooks/archive-plan.sh`:**

```bash
#!/usr/bin/env bash