### Execution layer (`mcp-tool.ts`)

Each discovered MCP tool is wrapped in a `DiscoveredMCPTool` instance that:

- **Handles confirmation logic** based on server trust settings and user
  preferences
- **Manages tool execution** by calling the MCP server with proper parameters
- **Processes responses** for both the LLM context and user display
- **Maintains connection state** and handles timeouts