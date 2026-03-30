### Configuration properties

Each server configuration supports the following properties:

#### Required (one of the following)

- **`command`** (string): Path to the executable for Stdio transport
- **`url`** (string): SSE endpoint URL (e.g., `"http://localhost:8080/sse"`)
- **`httpUrl`** (string): HTTP streaming endpoint URL

#### Optional

- **`args`** (string[]): Command-line arguments for Stdio transport
- **`headers`** (object): Custom HTTP headers when using `url` or `httpUrl`
- **`env`** (object): Environment variables for the server process. Values can
  reference environment variables using `$VAR_NAME` or `${VAR_NAME}` syntax (all
  platforms), or `%VAR_NAME%` (Windows only).
- **`cwd`** (string): Working directory for Stdio transport
- **`timeout`** (number): Request timeout in milliseconds (default: 600,000ms =
  10 minutes)
- **`trust`** (boolean): When `true`, bypasses all tool call confirmations for
  this server (default: `false`)
- **`includeTools`** (string[]): List of tool names to include from this MCP
  server. When specified, only the tools listed here will be available from this
  server (allowlist behavior). If not specified, all tools from the server are
  enabled by default.
- **`excludeTools`** (string[]): List of tool names to exclude from this MCP
  server. Tools listed here will not be available to the model, even if they are
  exposed by the server. `excludeTools` takes precedence over `includeTools`. If
  a tool is in both lists, it will be excluded.
- **`targetAudience`** (string): The OAuth Client ID allowlisted on the
  IAP-protected application you are trying to access. Used with
  `authProviderType: 'service_account_impersonation'`.
- **`targetServiceAccount`** (string): The email address of the Google Cloud
  Service Account to impersonate. Used with
  `authProviderType: 'service_account_impersonation'`.