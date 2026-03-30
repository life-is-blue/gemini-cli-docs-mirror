### Sandboxing

For maximum security, especially when running untrusted code or exploring new
projects, we strongly recommend enabling Sandboxing. This runs all shell
commands inside a secure Docker container.

**Enable sandboxing:** Use the `--sandbox` flag when starting the CLI:
`gemini --sandbox`.