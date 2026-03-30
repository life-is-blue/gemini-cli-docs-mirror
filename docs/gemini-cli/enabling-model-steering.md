## Enabling model steering

Model steering is an experimental feature and is disabled by default. You can
enable it using the `/settings` command or by updating your `settings.json`
file.

1.  Type `/settings` in the Gemini CLI.
2.  Search for **Model Steering**.
3.  Set the value to **true**.

Alternatively, add the following to your `settings.json`:

```json
{
  "experimental": {
    "modelSteering": true
  }
}
```