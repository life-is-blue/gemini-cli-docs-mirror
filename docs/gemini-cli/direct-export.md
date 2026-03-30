### Direct export

We recommend using direct export to send telemetry directly to Google Cloud
services.

1.  Enable telemetry in `.gemini/settings.json`:
    ```json
    {
      "telemetry": {
        "enabled": true,
        "target": "gcp"
      }
    }
    ```
2.  Run Gemini CLI and send prompts.
3.  View logs, metrics, and traces in the Google Cloud Console. See
    [View Google Cloud telemetry](#view-google-cloud-telemetry) for details.