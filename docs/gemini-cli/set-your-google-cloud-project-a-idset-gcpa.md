## Set your Google Cloud project <a id="set-gcp"></a>

<!-- prettier-ignore -->
> [!IMPORTANT]
> Most individual Google accounts (free and paid) don't require a
> Google Cloud project for authentication.

When you sign in using your Google account, you may need to configure a Google
Cloud project for Gemini CLI to use. This applies when you meet at least one of
the following conditions:

- You are using a Company, School, or Google Workspace account.
- You are using a Gemini Code Assist license from the Google Developer Program.
- You are using a license from a Gemini Code Assist subscription.

To configure Gemini CLI to use a Google Cloud project, do the following:

1.  [Find your Google Cloud Project ID](https://support.google.com/googleapi/answer/7014113).

2.  [Enable the Gemini for Cloud API](https://cloud.google.com/gemini/docs/discover/set-up-gemini#enable-api).

3.  [Configure necessary IAM access permissions](https://cloud.google.com/gemini/docs/discover/set-up-gemini#grant-iam).

4.  Configure your environment variables. Set either the `GOOGLE_CLOUD_PROJECT`
    or `GOOGLE_CLOUD_PROJECT_ID` variable to the project ID to use with Gemini
    CLI. Gemini CLI checks for `GOOGLE_CLOUD_PROJECT` first, then falls back to
    `GOOGLE_CLOUD_PROJECT_ID`.

    For example, to set the `GOOGLE_CLOUD_PROJECT_ID` variable:

    **macOS/Linux**

    ```bash
    # Replace YOUR_PROJECT_ID with your actual Google Cloud project ID
    export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
    ```

    **Windows (PowerShell)**

    ```powershell
    # Replace YOUR_PROJECT_ID with your actual Google Cloud project ID
    $env:GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
    ```

    To make this setting persistent, see
    [Persisting Environment Variables](#persisting-vars).