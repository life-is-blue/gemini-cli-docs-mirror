### 1. Server iteration and connection

For each configured server in `mcpServers`:

1. **Status tracking begins:** Server status is set to `CONNECTING`
2. **Transport selection:** Based on configuration properties:
   - `httpUrl` → `StreamableHTTPClientTransport`
   - `url` → `SSEClientTransport`
   - `command` → `StdioClientTransport`
3. **Connection establishment:** The MCP client attempts to connect with the
   configured timeout
4. **Error handling:** Connection failures are logged and the server status is
   set to `DISCONNECTED`