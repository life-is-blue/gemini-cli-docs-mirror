### Discovery Layer (`mcp-client.ts`)

The discovery process is orchestrated by `discoverMcpTools()`, which:

1. **Iterates through configured servers** from your `settings.json`
   `mcpServers` configuration
2. **Establishes connections** using appropriate transport mechanisms (Stdio,
   SSE, or Streamable HTTP)
3. **Fetches tool definitions** from each server using the MCP protocol
4. **Sanitizes and validates** tool schemas for compatibility with the Gemini
   API
5. **Registers tools** in the global tool registry with conflict resolution
6. **Fetches and registers resources** if the server exposes any