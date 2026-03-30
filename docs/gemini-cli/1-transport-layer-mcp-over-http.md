### 1. Transport layer: MCP over HTTP

The plugin **MUST** run a local HTTP server that implements the **Model Context
Protocol (MCP)**.

- **Protocol:** The server must be a valid MCP server. We recommend using an
  existing MCP SDK for your language of choice if available.
- **Endpoint:** The server should expose a single endpoint (e.g., `/mcp`) for
  all MCP communication.
- **Port:** The server **MUST** listen on a dynamically assigned port (i.e.,
  listen on port `0`).