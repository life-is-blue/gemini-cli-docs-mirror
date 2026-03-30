### Prerequisites

You must complete several setup steps before enabling Google Cloud telemetry.

1.  Set your Google Cloud project ID:
    - To send telemetry to a separate project:

      **macOS/Linux**

      ```bash
      export OTLP_GOOGLE_CLOUD_PROJECT="your-telemetry-project-id"
      ```

      **Windows (PowerShell)**

      ```powershell
      $env:OTLP_GOOGLE_CLOUD_PROJECT="your-telemetry-project-id"
      ```

    - To send telemetry to the same project as inference:

      **macOS/Linux**

      ```bash
      export GOOGLE_CLOUD_PROJECT="your-project-id"
      ```

      **Windows (PowerShell)**

      ```powershell
      $env:GOOGLE_CLOUD_PROJECT="your-project-id"
      ```

2.  Authenticate with Google Cloud using one of these methods:
    - **Method A: Application Default Credentials (ADC)**: Use this method for
      service accounts or standard `gcloud` authentication.
      - For user accounts:
        ```bash
        gcloud auth application-default login
        ```
      - For service accounts:

        **macOS/Linux**

        ```bash
        export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account.json"
        ```

        **Windows (PowerShell)**

        ```powershell
        $env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\service-account.json"
        ```
    * **Method B: CLI Auth** (Direct export only): Simplest method for local
      users. Gemini CLI uses the same OAuth credentials you used for login. To
      enable this, set `useCliAuth: true` in your `.gemini/settings.json`:

      ```json
      {
        "telemetry": {
          "enabled": true,
          "target": "gcp",
          "useCliAuth": true
        }
      }
      ```

<!-- prettier-ignore -->
> [!NOTE]
> This setting requires **Direct export** (in-process exporters)
> and cannot be used when `useCollector` is `true`. If both are enabled,
> telemetry will be disabled.

3.  Ensure your account or service account has these IAM roles:
    - Cloud Trace Agent
    - Monitoring Metric Writer
    - Logs Writer

4.  Enable the required Google Cloud APIs:
    ```bash
    gcloud services enable \
      cloudtrace.googleapis.com \
      monitoring.googleapis.com \
      logging.googleapis.com \
      --project="$OTLP_GOOGLE_CLOUD_PROJECT"
    ```