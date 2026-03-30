### Defining a Deterministic Baseline

Create an alias for tasks requiring high precision, extending the standard chat
configuration but enforcing zero temperature.

```json
"modelConfigs": {
  "customAliases": {
    "precise-mode": {
      "extends": "chat-base",
      "modelConfig": {
        "generateContentConfig": {
          "temperature": 0.0,
          "topP": 1.0
        }
      }
    }
  }
}
```