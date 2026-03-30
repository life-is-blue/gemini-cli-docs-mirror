### Agent-Specific Parameter Injection

Enforce extended thinking budgets for a specific agent without altering the
global default, e.g. for the `codebaseInvestigator`.

```json
"modelConfigs": {
  "overrides": [
    {
      "match": {
        "overrideScope": "codebaseInvestigator"
      },
      "modelConfig": {
        "generateContentConfig": {
          "thinkingConfig": { "thinkingBudget": 4096 }
        }
      }
    }
  ]
}
```