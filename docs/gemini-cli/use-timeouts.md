### Use timeouts

Prevent denial-of-service (hanging agents) by enforcing timeouts. Gemini CLI
defaults to 60 seconds, but you should set stricter limits for fast hooks.

```json
{
  "hooks": {
    "BeforeTool": [
      {
        "matcher": "*",
        "hooks": [
          {
            "name": "fast-validator",
            "type": "command",
            "command": "./hooks/validate.sh",
            "timeout": 5000 // 5 seconds
          }
        ]
      }
    ]
  }
}
```