# Replace with your project ID and desired location (for example, us-central1)
$env:GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
$env:GOOGLE_CLOUD_LOCATION="YOUR_PROJECT_LOCATION"
```

To make any Vertex AI environment variable settings persistent, see
[Persisting Environment Variables](#persisting-vars).

#### A. Vertex AI - application default credentials (ADC) using `gcloud`

Consider this authentication method if you have Google Cloud CLI installed.

If you have previously set `GOOGLE_API_KEY` or `GEMINI_API_KEY`, you must unset
them to use ADC.

**macOS/Linux**

```bash
unset GOOGLE_API_KEY GEMINI_API_KEY
```

**Windows (PowerShell)**

```powershell
Remove-Item Env:\GOOGLE_API_KEY, Env:\GEMINI_API_KEY -ErrorAction Ignore
```

1. Verify you have a Google Cloud project and Vertex AI API is enabled.

2. Log in to Google Cloud:

   ```bash
   gcloud auth application-default login
   ```

3. [Configure your Google Cloud Project](#set-gcp).

4. Start the CLI:

   ```bash
   gemini
   ```

5. Select **Vertex AI**.

#### B. Vertex AI - service account JSON key

Consider this method of authentication in non-interactive environments, CI/CD
pipelines, or if your organization restricts user-based ADC or API key creation.

If you have previously set `GOOGLE_API_KEY` or `GEMINI_API_KEY`, you must unset
them:

**macOS/Linux**

```bash
unset GOOGLE_API_KEY GEMINI_API_KEY
```

**Windows (PowerShell)**

```powershell
Remove-Item Env:\GOOGLE_API_KEY, Env:\GEMINI_API_KEY -ErrorAction Ignore
```

1.  [Create a service account and key](https://cloud.google.com/iam/docs/keys-create-delete)
    and download the provided JSON file. Assign the "Vertex AI User" role to the
    service account.

2.  Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the JSON
    file's absolute path. For example:

    **macOS/Linux**

    ```bash
    # Replace /path/to/your/keyfile.json with the actual path
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/keyfile.json"
    ```

    **Windows (PowerShell)**

    ```powershell
    # Replace C:\path\to\your\keyfile.json with the actual path
    $env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\keyfile.json"
    ```

3.  [Configure your Google Cloud Project](#set-gcp).

4.  Start the CLI:

    ```bash
    gemini
    ```

5.  Select **Vertex AI**.

<!-- prettier-ignore -->
> [!WARNING]
> Protect your service account key file as it gives access to
> your resources.

#### C. Vertex AI - Google Cloud API key

1.  Obtain a Google Cloud API key:
    [Get an API Key](https://cloud.google.com/vertex-ai/generative-ai/docs/start/api-keys?usertype=newuser).

2.  Set the `GOOGLE_API_KEY` environment variable:

    **macOS/Linux**

    ```bash
    # Replace YOUR_GOOGLE_API_KEY with your Vertex AI API key
    export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    ```

    **Windows (PowerShell)**

    ```powershell
    # Replace YOUR_GOOGLE_API_KEY with your Vertex AI API key
    $env:GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
    ```

    If you see errors like `"API keys are not supported by this API..."`, your
    organization might restrict API key usage for this service. Try the other
    Vertex AI authentication methods instead.

3.  [Configure your Google Cloud Project](#set-gcp).

4.  Start the CLI:

    ```bash
    gemini
    ```

5.  Select **Vertex AI**.