### Security considerations

- **Trust settings:** The `trust` option bypasses all confirmation dialogs. Use
  cautiously and only for servers you completely control
- **Access tokens:** Be security-aware when configuring environment variables
  containing API keys or tokens. See
  [Security and environment sanitization](#security-and-environment-sanitization)
  for details on how Gemini CLI protects your credentials.
- **Sandbox compatibility:** When using sandboxing, ensure MCP servers are
  available within the sandbox environment
- **Private data:** Using broadly scoped personal access tokens can lead to
  information leakage between repositories.