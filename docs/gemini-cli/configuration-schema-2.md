### Configuration schema

| Field             | Type   | Required | Description                                                                                                    |
| :---------------- | :----- | :------- | :------------------------------------------------------------------------------------------------------------- |
| `kind`            | string | Yes      | Must be `remote`.                                                                                              |
| `name`            | string | Yes      | A unique name for the agent. Must be a valid slug (lowercase letters, numbers, hyphens, and underscores only). |
| `agent_card_url`  | string | Yes\*    | The URL to the agent's A2A card endpoint. Required if `agent_card_json` is not provided.                       |
| `agent_card_json` | string | Yes\*    | The inline JSON string of the agent's A2A card. Required if `agent_card_url` is not provided.                  |
| `auth`            | object | No       | Authentication configuration. See [Authentication](#authentication).                                           |