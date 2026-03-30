### Security and environment sanitization

To protect your credentials, Gemini CLI performs environment sanitization when
spawning MCP server processes.

#### Automatic redaction

By default, the CLI redacts sensitive environment variables from the base
environment (inherited from the host process) to prevent unintended exposure to
third-party MCP servers. This includes:

- Core project keys: `GEMINI_API_KEY`, `GOOGLE_API_KEY`, etc.
- Variables matching sensitive patterns: `*TOKEN*`, `*SECRET*`, `*PASSWORD*`,
  `*KEY*`, `*AUTH*`, `*CREDENTIAL*`.
- Certificates and private key patterns.

#### Explicit overrides

If an environment variable must be passed to an MCP server, you must explicitly
state it in the `env` property of the server configuration in `settings.json`.
Explicitly defined variables (including those from extensions) are trusted and
are **not** subjected to the automatic redaction process.

This follows the security principle that if a variable is explicitly configured
by the user for a specific server, it constitutes informed consent to share that
specific data with that server.

<!-- prettier-ignore -->
> [!NOTE]
> Even when explicitly defined, you should avoid hardcoding secrets.
> Instead, use environment variable expansion (e.g., `"MY_KEY": "$MY_KEY"`) to
> securely pull the value from your host environment at runtime.