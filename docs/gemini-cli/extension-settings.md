### Extension settings

Extensions can define settings that users provide during installation, such as
API keys or URLs. These values are stored in a `.env` file within the extension
directory.

To define settings, add a `settings` array to your manifest:

```json
{
  "name": "my-api-extension",
  "version": "1.0.0",
  "settings": [
    {
      "name": "API Key",
      "description": "Your API key for the service.",
      "envVar": "MY_API_KEY",
      "sensitive": true
    }
  ]
}
```

- `name`: The setting's display name.
- `description`: A clear explanation of the setting.
- `envVar`: The environment variable name where the value is stored.
- `sensitive`: If `true`, the value is stored in the system keychain and
  obfuscated in the UI.

To update an extension's settings:

```bash
gemini extensions config <name> [setting] [--scope <scope>]
```