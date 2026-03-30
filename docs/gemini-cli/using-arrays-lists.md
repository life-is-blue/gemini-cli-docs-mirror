### Using arrays (lists)

To apply the same rule to multiple tools or command prefixes, you can provide an
array of strings for the `toolName` and `commandPrefix` fields.

**Example:**

This single rule will apply to both the `write_file` and `replace` tools.

```toml
[[rule]]
toolName = ["write_file", "replace"]
decision = "ask_user"
priority = 10
```