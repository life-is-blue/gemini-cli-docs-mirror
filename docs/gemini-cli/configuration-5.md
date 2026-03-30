## Configuration

To use a local Gemma model for routing, you must explicitly enable it in your
`settings.json`:

```json
{
  "experimental": {
    "gemmaModelRouter": {
      "enabled": true,
      "classifier": {
        "host": "http://localhost:9379",
        "model": "gemma3-1b-gpu-custom"
      }
    }
  }
}
```

> Use the port you started your LiteRT-LM runtime on in the setup steps.