### Extending with MCP

ACP can be used with the Model Context Protocol (MCP). This lets an ACP client
(like an IDE) expose its own functionality as "tools" that the Gemini model can
use.

1.  The client implements an **MCP server** that advertises its tools.
2.  During the ACP `initialize` handshake, the client provides the connection
    details for its MCP server.
3.  Gemini CLI connects to the MCP server, discovers the available tools, and
    makes them available to the AI model.
4.  When the model decides to use one of these tools, Gemini CLI sends a tool
    call request to the MCP server.

This mechanism lets for a powerful, two-way integration where the agent can
leverage the IDE's capabilities to perform tasks. The MCP client logic is in
`packages/core/src/tools/mcp-client.ts`.