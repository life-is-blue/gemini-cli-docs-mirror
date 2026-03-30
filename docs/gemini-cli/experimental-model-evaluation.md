### Experimental Model Evaluation

Route traffic for a specific alias to a preview model for A/B testing, without
changing client code.

```json
"modelConfigs": {
  "overrides": [
    {
      "match": {
        "model": "gemini-2.5-pro"
      },
      "modelConfig": {
        "model": "gemini-2.5-pro-experimental-001"
      }
    }
  ]
}
```