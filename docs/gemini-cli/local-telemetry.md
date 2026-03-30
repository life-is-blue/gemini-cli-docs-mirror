## Local telemetry

You can capture telemetry data locally for development and debugging. We
recommend using file-based output for local development.

1.  Enable telemetry in `.gemini/settings.json`:
    ```json
    {
      "telemetry": {
        "enabled": true,
        "target": "local",
        "outfile": ".gemini/telemetry.log"
      }
    }
    ```
2.  Run Gemini CLI and send prompts.
3.  View logs and metrics in `.gemini/telemetry.log`.

For advanced local telemetry setups (such as Jaeger or Genkit), see the
[Local development guide](/docs/local-development#viewing-traces).