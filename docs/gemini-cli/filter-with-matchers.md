### Filter with matchers

Use specific matchers to avoid unnecessary hook execution. Instead of matching
all tools with `*`, specify only the tools you need. This saves the overhead of
spawning a process for irrelevant events.

```json
{
  "matcher": "write_file|replace",
  "hooks": [
    {
      "name": "validate-writes",
      "type": "command",
      "command": "./validate.sh"
    }
  ]
}
```