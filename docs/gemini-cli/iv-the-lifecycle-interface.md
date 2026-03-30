## IV. The lifecycle interface

The plugin **MUST** manage its resources and the discovery file correctly based
on the IDE's lifecycle.

- **On activation (IDE startup/plugin enabled):**
  1.  Start the MCP server.
  2.  Create the discovery file.
- **On deactivation (IDE shutdown/plugin disabled):**
  1.  Stop the MCP server.
  2.  Delete the discovery file.