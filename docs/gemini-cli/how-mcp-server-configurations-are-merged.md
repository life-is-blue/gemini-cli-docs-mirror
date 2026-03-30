### How MCP server configurations are merged

Gemini CLI loads `settings.json` files from three levels: System, Workspace, and
User. When it comes to the `mcpServers` object, these configurations are
**merged**:

1.  **Merging:** The lists of servers from all three levels are combined into a
    single list.
2.  **Precedence:** If a server with the **same name** is defined at multiple
    levels (e.g., a server named `corp-api` exists in both system and user
    settings), the definition from the highest-precedence level is used. The
    order of precedence is: **System > Workspace > User**.

This means a user **cannot** override the definition of a server that is already
defined in the system-level settings. However, they **can** add new servers with
unique names.