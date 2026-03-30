### Persistent configuration (settings.json)

While the `/agents` command and agent definition files provide a starting point,
you can use `settings.json` for global, persistent overrides. This is useful for
enforcing specific models or execution limits across all sessions.

#### `agents.overrides`

Use this to enable or disable specific agents or override their run
configurations.

```json
{
  "agents": {
    "overrides": {
      "security-auditor": {
        "enabled": false,
        "runConfig": {
          "maxTurns": 20,
          "maxTimeMinutes": 10
        }
      }
    }
  }
}
```

#### `modelConfigs.overrides`

You can target specific subagents with custom model settings (like system
instruction prefixes or specific safety settings) using the `overrideScope`
field.

```json
{
  "modelConfigs": {
    "overrides": [
      {
        "match": { "overrideScope": "security-auditor" },
        "modelConfig": {
          "generateContentConfig": {
            "temperature": 0.1
          }
        }
      }
    ]
  }
}
```