## Telemetry and auditing

For auditing and monitoring purposes, you can configure Gemini CLI to send
telemetry data to a central location. This allows you to track tool usage and
other events. For more information, see the
[telemetry documentation](/docs/cli/telemetry).

**Example:** Enable telemetry and send it to a local OTLP collector. If
`otlpEndpoint` is not specified, it defaults to `http://localhost:4317`.

```json
{
  "telemetry": {
    "enabled": true,
    "target": "gcp",
    "logPrompts": false
  }
}
```

<!-- prettier-ignore -->
> [!NOTE]
> Ensure that `logPrompts` is set to `false` in an enterprise setting to
> avoid collecting potentially sensitive information from user prompts.