## Sandboxing

The Gemini CLI can execute potentially unsafe operations (like shell commands
and file modifications) within a sandboxed environment to protect your system.

Sandboxing is disabled by default, but you can enable it in a few ways:

- Using `--sandbox` or `-s` flag.
- Setting `GEMINI_SANDBOX` environment variable.
- Sandbox is enabled when using `--yolo` or `--approval-mode=yolo` by default.

By default, it uses a pre-built `gemini-cli-sandbox` Docker image.

For project-specific sandboxing needs, you can create a custom Dockerfile at
`.gemini/sandbox.Dockerfile` in your project's root directory. This Dockerfile
can be based on the base sandbox image:

```dockerfile
FROM gemini-cli-sandbox