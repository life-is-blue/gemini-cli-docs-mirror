## Use Vertex AI <a id="vertex-ai"></a>

To use Gemini CLI with Google Cloud's Vertex AI platform, choose from the
following authentication options:

- A. Application Default Credentials (ADC) using `gcloud`.
- B. Service account JSON key.
- C. Google Cloud API key.

Regardless of your authentication method for Vertex AI, you'll need to set
`GOOGLE_CLOUD_PROJECT` to your Google Cloud project ID with the Vertex AI API
enabled, and `GOOGLE_CLOUD_LOCATION` to the location of your Vertex AI resources
or the location where you want to run your jobs.

For example:

**macOS/Linux**

```bash