### Overrides (`overrides`)

Overrides are conditional rules that inject configuration based on the runtime
context. They are evaluated dynamically for each model request.

- **Match Criteria**: Overrides apply when the request context matches the
  specified `match` properties.
  - `model`: Matches the requested model name or alias.
  - `overrideScope`: Matches the distinct scope of the request (typically the
    agent name, e.g., `codebaseInvestigator`).

**Example Override**:

```json
"modelConfigs": {
  "overrides": [
    {
      "match": {
        "overrideScope": "codebaseInvestigator"
      },
      "modelConfig": {
        "generateContentConfig": { "temperature": 0.1 }
      }
    }
  ]
}
```