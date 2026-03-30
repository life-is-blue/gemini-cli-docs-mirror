### Configuration (`.gemini/settings.json`)

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "name": "init",
            "type": "command",
            "command": "node .gemini/hooks/init.js"
          }
        ]
      }
    ],
    "BeforeAgent": [
      {
        "matcher": "*",
        "hooks": [
          {
            "name": "memory",
            "type": "command",
            "command": "node .gemini/hooks/inject-memories.js"
          }
        ]
      }
    ],
    "BeforeToolSelection": [
      {
        "matcher": "*",
        "hooks": [
          {
            "name": "filter",
            "type": "command",
            "command": "node .gemini/hooks/rag-filter.js"
          }
        ]
      }
    ],
    "BeforeTool": [
      {
        "matcher": "write_file",
        "hooks": [
          {
            "name": "security",
            "type": "command",
            "command": "node .gemini/hooks/security.js"
          }
        ]
      }
    ],
    "AfterModel": [
      {
        "matcher": "*",
        "hooks": [
          {
            "name": "record",
            "type": "command",
            "command": "node .gemini/hooks/record.js"
          }
        ]
      }
    ],
    "AfterAgent": [
      {
        "matcher": "*",
        "hooks": [
          {
            "name": "validate",
            "type": "command",
            "command": "node .gemini/hooks/validate.js"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "matcher": "exit",
        "hooks": [
          {
            "name": "save",
            "type": "command",
            "command": "node .gemini/hooks/consolidate.js"
          }
        ]
      }
    ]
  }
}
```