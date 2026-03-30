### Supported auth types

Gemini CLI supports the following authentication types:

| Type                 | Description                                                                                    |
| :------------------- | :--------------------------------------------------------------------------------------------- |
| `apiKey`             | Send a static API key as an HTTP header.                                                       |
| `http`               | HTTP authentication (Bearer token, Basic credentials, or any IANA-registered scheme).          |
| `google-credentials` | Google Application Default Credentials (ADC). Automatically selects access or identity tokens. |
| `oauth`              | OAuth 2.0 Authorization Code flow with PKCE. Opens a browser for interactive sign-in.          |