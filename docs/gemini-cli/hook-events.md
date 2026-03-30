### Hook events

Hooks are triggered by specific events in Gemini CLI's lifecycle.

| Event                 | When It Fires                                  | Impact                 | Common Use Cases                             |
| --------------------- | ---------------------------------------------- | ---------------------- | -------------------------------------------- |
| `SessionStart`        | When a session begins (startup, resume, clear) | Inject Context         | Initialize resources, load context           |
| `SessionEnd`          | When a session ends (exit, clear)              | Advisory               | Clean up, save state                         |
| `BeforeAgent`         | After user submits prompt, before planning     | Block Turn / Context   | Add context, validate prompts, block turns   |
| `AfterAgent`          | When agent loop ends                           | Retry / Halt           | Review output, force retry or halt execution |
| `BeforeModel`         | Before sending request to LLM                  | Block Turn / Mock      | Modify prompts, swap models, mock responses  |
| `AfterModel`          | After receiving LLM response                   | Block Turn / Redact    | Filter/redact responses, log interactions    |
| `BeforeToolSelection` | Before LLM selects tools                       | Filter Tools           | Filter available tools, optimize selection   |
| `BeforeTool`          | Before a tool executes                         | Block Tool / Rewrite   | Validate arguments, block dangerous ops      |
| `AfterTool`           | After a tool executes                          | Block Result / Context | Process results, run tests, hide results     |
| `PreCompress`         | Before context compression                     | Advisory               | Save state, notify user                      |
| `Notification`        | When a system notification occurs              | Advisory               | Forward to desktop alerts, logging           |