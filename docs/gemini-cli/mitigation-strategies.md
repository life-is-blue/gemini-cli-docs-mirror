### Mitigation Strategies

#### Verify the source

**Verify the source** of any project hooks or extensions before enabling them.

- For open-source projects, a quick review of the hook scripts is recommended.
- For extensions, ensure you trust the author or publisher (e.g., verified
  publishers, well-known community members).
- Be cautious with obfuscated scripts or compiled binaries from unknown sources.

#### Sanitize environment

Hooks inherit the environment of the Gemini CLI process, which may include
sensitive API keys. Gemini CLI provides a
[redaction system](/docs/reference/configuration#environment-variable-redaction)
that automatically filters variables matching sensitive patterns (e.g., `KEY`,
`TOKEN`).

> **Disabled by Default**: Environment redaction is currently **OFF by
> default**. We strongly recommend enabling it if you are running third-party
> hooks or working in sensitive environments.

**Impact on hooks:**

- **Security**: Prevents your hook scripts from accidentally leaking secrets.
- **Troubleshooting**: If your hook depends on a specific environment variable
  that is being blocked, you must explicitly allow it in `settings.json`.

```json
{
  "security": {
    "environmentVariableRedaction": {
      "enabled": true,
      "allowed": ["MY_REQUIRED_TOOL_KEY"]
    }
  }
}
```

**System administrators:** You can enforce redaction for all users in the system
configuration.