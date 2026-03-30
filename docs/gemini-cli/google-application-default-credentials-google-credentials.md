### Google Application Default Credentials (`google-credentials`)

Uses
[Google Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/application-default-credentials)
to authenticate with Google Cloud services and Cloud Run endpoints. This is the
recommended auth method for agents hosted on Google Cloud infrastructure.

| Field    | Type     | Required | Description                                                                 |
| :------- | :------- | :------- | :-------------------------------------------------------------------------- |
| `type`   | string   | Yes      | Must be `google-credentials`.                                               |
| `scopes` | string[] | No       | OAuth scopes. Defaults to `https://www.googleapis.com/auth/cloud-platform`. |

```yaml
---
kind: remote
name: my-gcp-agent
agent_card_url: https://my-agent-xyz.run.app/.well-known/agent.json
auth:
  type: google-credentials
---
```

#### How token selection works

The provider automatically selects the correct token type based on the agent's
host:

| Host pattern       | Token type         | Use case                                    |
| :----------------- | :----------------- | :------------------------------------------ |
| `*.googleapis.com` | **Access token**   | Google APIs (Agent Engine, Vertex AI, etc.) |
| `*.run.app`        | **Identity token** | Cloud Run services                          |

- **Access tokens** authorize API calls to Google services. They are scoped
  (default: `cloud-platform`) and fetched via `GoogleAuth.getClient()`.
- **Identity tokens** prove the caller's identity to a service that validates
  the token's audience. The audience is set to the target host. These are
  fetched via `GoogleAuth.getIdTokenClient()`.

Both token types are cached and automatically refreshed before expiry.

#### Setup

`google-credentials` relies on ADC, which means your environment must have
credentials configured. Common setups:

- **Local development:** Run `gcloud auth application-default login` to
  authenticate with your Google account.
- **CI / Cloud environments:** Use a service account. Set the
  `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your
  service account key file, or use workload identity on GKE / Cloud Run.

#### Allowed hosts

For security, `google-credentials` only sends tokens to known Google-owned
hosts:

- `*.googleapis.com`
- `*.run.app`

Requests to any other host will be rejected with an error. If your agent is
hosted on a different domain, use one of the other auth types (`apiKey`, `http`,
or `oauth`).

#### Examples

The following examples demonstrate how to configure Google Application Default
Credentials.

**Cloud Run agent:**

```yaml
---
kind: remote
name: cloud-run-agent
agent_card_url: https://my-agent-xyz.run.app/.well-known/agent.json
auth:
  type: google-credentials
---
```

**Google API with custom scopes:**

```yaml
---
kind: remote
name: vertex-agent
agent_card_url: https://us-central1-aiplatform.googleapis.com/.well-known/agent.json
auth:
  type: google-credentials
  scopes:
    - https://www.googleapis.com/auth/cloud-platform
    - https://www.googleapis.com/auth/compute
---
```