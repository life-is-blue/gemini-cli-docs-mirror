### API key (`apiKey`)

Sends an API key as an HTTP header on every request.

| Field  | Type   | Required | Description                                           |
| :----- | :----- | :------- | :---------------------------------------------------- |
| `type` | string | Yes      | Must be `apiKey`.                                     |
| `key`  | string | Yes      | The API key value. Supports dynamic values.           |
| `name` | string | No       | Header name to send the key in. Default: `X-API-Key`. |

```yaml
---
kind: remote
name: my-agent
agent_card_url: https://example.com/agent-card
auth:
  type: apiKey
  key: $MY_API_KEY
---
```