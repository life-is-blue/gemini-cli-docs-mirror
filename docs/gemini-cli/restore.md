### `/restore`

- **Description:** Restores the project files to the state they were in just
  before a tool was executed. This is particularly useful for undoing file edits
  made by a tool. If run without a tool call ID, it will list available
  checkpoints to restore from.
- **Usage:** `/restore [tool_call_id]`
- **Note:** Only available if checkpointing is configured via
  [settings](/docs/reference/configuration). See
  [Checkpointing documentation](/docs/cli/checkpointing) for more details.