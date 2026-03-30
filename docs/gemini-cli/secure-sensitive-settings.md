### Secure sensitive settings

If your extension requires API keys or other secrets, use the `sensitive: true`
option in your manifest. This ensures keys are stored in the system keychain and
obfuscated in the CLI output.

```json
"settings": [
  {
    "name": "API Key",
    "envVar": "MY_API_KEY",
    "sensitive": true
  }
]
```