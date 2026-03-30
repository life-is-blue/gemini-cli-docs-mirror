### OAuth support for remote MCP servers

The Gemini CLI supports OAuth 2.0 authentication for remote MCP servers using
SSE or HTTP transports. This enables secure access to MCP servers that require
authentication.

#### Automatic OAuth discovery

For servers that support OAuth discovery, you can omit the OAuth configuration
and let the CLI discover it automatically:

```json
{
  "mcpServers": {
    "discoveredServer": {
      "url": "https://api.example.com/sse"
    }
  }
}
```

The CLI will automatically:

- Detect when a server requires OAuth authentication (401 responses)
- Discover OAuth endpoints from server metadata
- Perform dynamic client registration if supported
- Handle the OAuth flow and token management

#### Authentication flow

When connecting to an OAuth-enabled server:

1. **Initial connection attempt** fails with 401 Unauthorized
2. **OAuth discovery** finds authorization and token endpoints
3. **Browser opens** for user authentication (requires local browser access)
4. **Authorization code** is exchanged for access tokens
5. **Tokens are stored** securely for future use
6. **Connection retry** succeeds with valid tokens

#### Browser redirect requirements

<!-- prettier-ignore -->
> [!IMPORTANT]
> OAuth authentication requires that your local machine can:
>
> - Open a web browser for authentication
> - Receive redirects on `http://localhost:7777/oauth/callback`

This feature will not work in:

- Headless environments without browser access
- Remote SSH sessions without X11 forwarding
- Containerized environments without browser support

#### Managing OAuth authentication

Use the `/mcp auth` command to manage OAuth authentication:

```bash