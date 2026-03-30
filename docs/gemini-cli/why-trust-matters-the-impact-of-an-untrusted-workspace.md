## Why trust matters: The impact of an untrusted workspace

When a folder is **untrusted**, the Gemini CLI runs in a restricted "safe mode"
to protect you. In this mode, the following features are disabled:

1.  **Workspace settings are ignored**: The CLI will **not** load the
    `.gemini/settings.json` file from the project. This prevents the loading of
    custom tools and other potentially dangerous configurations.

2.  **Environment variables are ignored**: The CLI will **not** load any `.env`
    files from the project.

3.  **Extension management is restricted**: You **cannot install, update, or
    uninstall** extensions.

4.  **Tool auto-acceptance is disabled**: You will always be prompted before any
    tool is run, even if you have auto-acceptance enabled globally.

5.  **Automatic memory loading is disabled**: The CLI will not automatically
    load files into context from directories specified in local settings.

6.  **MCP servers do not connect**: The CLI will not attempt to connect to any
    [Model Context Protocol (MCP)](/docs/tools/mcp-server) servers.

7.  **Custom commands are not loaded**: The CLI will not load any custom
    commands from .toml files, including both project-specific and global user
    commands.

Granting trust to a folder unlocks the full functionality of the Gemini CLI for
that workspace.