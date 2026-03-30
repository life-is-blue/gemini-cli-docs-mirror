## MCP server management

| Command                                                       | Description                     | Example                                                                                              |
| ------------------------------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `gemini mcp add <name> <command>`                             | Add stdio-based MCP server      | `gemini mcp add github npx -y @modelcontextprotocol/server-github`                                   |
| `gemini mcp add <name> <url> --transport http`                | Add HTTP-based MCP server       | `gemini mcp add api-server http://localhost:3000 --transport http`                                   |
| `gemini mcp add <name> <command> --env KEY=value`             | Add with environment variables  | `gemini mcp add slack node server.js --env SLACK_TOKEN=xoxb-xxx`                                     |
| `gemini mcp add <name> <command> --scope user`                | Add with user scope             | `gemini mcp add db node db-server.js --scope user`                                                   |
| `gemini mcp add <name> <command> --include-tools tool1,tool2` | Add with specific tools         | `gemini mcp add github npx -y @modelcontextprotocol/server-github --include-tools list_repos,get_pr` |
| `gemini mcp remove <name>`                                    | Remove an MCP server            | `gemini mcp remove github`                                                                           |
| `gemini mcp list`                                             | List all configured MCP servers | `gemini mcp list`                                                                                    |

See [MCP Server Integration](/docs/tools/mcp-server) for more details.