## Step 3: Add extension settings

Some extensions need configuration, such as API keys or user preferences. Let's
add a setting for an API key.

1.  Open `gemini-extension.json`.
2.  Add a `settings` array to the configuration:

    ```json
    {
      "name": "mcp-server-example",
      "version": "1.0.0",
      "settings": [
        {
          "name": "API Key",
          "description": "The API key for the service.",
          "envVar": "MY_SERVICE_API_KEY",
          "sensitive": true
        }
      ],
      "mcpServers": {
        // ...
      }
    }
    ```

When a user installs this extension, Gemini CLI will prompt them to enter the
"API Key". The value will be stored securely in the system keychain (because
`sensitive` is true) and injected into the MCP server's process as the
`MY_SERVICE_API_KEY` environment variable.