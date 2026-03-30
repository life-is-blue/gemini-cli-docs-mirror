### Automatic execution and security

When the model wants to use a tool, Gemini CLI evaluates the request against its
security policies.

- **User confirmation:** You must manually approve tools that modify files or
  execute shell commands (mutators). The CLI shows you a diff or the exact
  command before you confirm.
- **Sandboxing:** You can run tool executions in secure, containerized
  environments to isolate changes from your host system. For more details, see
  the [Sandboxing](/docs/cli/sandbox) guide.
- **Trusted folders:** You can configure which directories allow the model to
  use system tools. For more details, see the
  [Trusted folders](/docs/cli/trusted-folders) guide.

Review confirmation prompts carefully before allowing a tool to execute.