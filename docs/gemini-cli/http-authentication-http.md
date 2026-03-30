### HTTP authentication (`http`)

Supports Bearer tokens, Basic auth, and arbitrary IANA-registered HTTP
authentication schemes.

#### Bearer token

Use the following fields to configure a Bearer token:

| Field    | Type   | Required | Description                                |
| :------- | :----- | :------- | :----------------------------------------- |
| `type`   | string | Yes      | Must be `http`.                            |
| `scheme` | string | Yes      | Must be `Bearer`.                          |
| `token`  | string | Yes      | The bearer token. Supports dynamic values. |

```yaml
auth:
  type: http
  scheme: Bearer
  token: $MY_BEARER_TOKEN
```

#### Basic authentication

Use the following fields to configure Basic authentication:

| Field      | Type   | Required | Description                            |
| :--------- | :----- | :------- | :------------------------------------- |
| `type`     | string | Yes      | Must be `http`.                        |
| `scheme`   | string | Yes      | Must be `Basic`.                       |
| `username` | string | Yes      | The username. Supports dynamic values. |
| `password` | string | Yes      | The password. Supports dynamic values. |

```yaml
auth:
  type: http
  scheme: Basic
  username: $MY_USERNAME
  password: $MY_PASSWORD
```

#### Raw scheme

For any other IANA-registered scheme (for example, Digest, HOBA), provide the
raw authorization value.

| Field    | Type   | Required | Description                                                                   |
| :------- | :----- | :------- | :---------------------------------------------------------------------------- |
| `type`   | string | Yes      | Must be `http`.                                                               |
| `scheme` | string | Yes      | The scheme name (for example, `Digest`).                                      |
| `value`  | string | Yes      | Raw value sent as `Authorization: <scheme> <value>`. Supports dynamic values. |

```yaml
auth:
  type: http
  scheme: Digest
  value: $MY_DIGEST_VALUE
```