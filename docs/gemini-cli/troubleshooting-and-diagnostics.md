## Troubleshooting and Diagnostics

To minimize noise during startup, MCP connection errors for background servers
are "silent by default." If issues are detected during startup, a single
informational hint will be shown: _"MCP issues detected. Run /mcp list for
status."_

Detailed, actionable diagnostics for a specific server are automatically
re-enabled when:

1.  You run an interactive command like `/mcp list`, `/mcp auth`, etc.
2.  The model attempts to execute a tool from that server.
3.  You invoke an MCP prompt from that server.

You can also use `gemini mcp list` from your shell to see connection errors for
all configured servers.