### Allowlisting with `coreTools`

The most secure approach is to explicitly add the tools and commands that users
are permitted to execute to an allowlist. This prevents the use of any tool not
on the approved list.

**Example:** Allow only safe, read-only file operations and listing files.

```json
{
  "tools": {
    "core": ["ReadFileTool", "GlobTool", "ShellTool(ls)"]
  }
}
```