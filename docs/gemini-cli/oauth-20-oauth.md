### OAuth 2.0 (`oauth`)

Performs an interactive OAuth 2.0 Authorization Code flow with PKCE. On first
use, Gemini CLI opens your browser for sign-in and persists the resulting tokens
for subsequent requests.

| Field               | Type     | Required | Description                                                                                                                                        |
| :------------------ | :------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`              | string   | Yes      | Must be `oauth`.                                                                                                                                   |
| `client_id`         | string   | Yes\*    | OAuth client ID. Required for interactive auth.                                                                                                    |
| `client_secret`     | string   | No\*     | OAuth client secret. Required by most authorization servers (confidential clients). Can be omitted for public clients that don't require a secret. |
| `scopes`            | string[] | No       | Requested scopes. Can also be discovered from the agent card.                                                                                      |
| `authorization_url` | string   | No       | Authorization endpoint. Discovered from the agent card if omitted.                                                                                 |
| `token_url`         | string   | No       | Token endpoint. Discovered from the agent card if omitted.                                                                                         |

```yaml
---
kind: remote
name: oauth-agent
agent_card_url: https://example.com/.well-known/agent.json
auth:
  type: oauth
  client_id: my-client-id.apps.example.com
---
```

If the agent card advertises an `oauth2` security scheme with
`authorizationCode` flow, the `authorization_url`, `token_url`, and `scopes` are
automatically discovered. You only need to provide `client_id` (and
`client_secret` if required).

Tokens are persisted to disk and refreshed automatically when they expire.