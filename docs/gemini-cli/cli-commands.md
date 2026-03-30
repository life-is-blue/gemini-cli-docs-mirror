## CLI commands

| Command                            | Description                        | Example                                                      |
| ---------------------------------- | ---------------------------------- | ------------------------------------------------------------ |
| `gemini`                           | Start interactive REPL             | `gemini`                                                     |
| `gemini -p "query"`                | Query non-interactively            | `gemini -p "summarize README.md"`                            |
| `gemini "query"`                   | Query and continue interactively   | `gemini "explain this project"`                              |
| `cat file \| gemini`               | Process piped content              | `cat logs.txt \| gemini`<br>`Get-Content logs.txt \| gemini` |
| `gemini -i "query"`                | Execute and continue interactively | `gemini -i "What is the purpose of this project?"`           |
| `gemini -r "latest"`               | Continue most recent session       | `gemini -r "latest"`                                         |
| `gemini -r "latest" "query"`       | Continue session with a new prompt | `gemini -r "latest" "Check for type errors"`                 |
| `gemini -r "<session-id>" "query"` | Resume session by ID               | `gemini -r "abc123" "Finish this PR"`                        |
| `gemini update`                    | Update to latest version           | `gemini update`                                              |
| `gemini extensions`                | Manage extensions                  | See [Extensions Management](#extensions-management)          |
| `gemini mcp`                       | Configure MCP servers              | See [MCP Server Management](#mcp-server-management)          |