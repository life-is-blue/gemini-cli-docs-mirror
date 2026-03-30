## Using with sandboxing

If you are using Gemini CLI within a sandbox, please be aware of the following:

- **On macOS:** The IDE integration requires network access to communicate with
  the IDE companion extension. You must use a Seatbelt profile that allows
  network access.
- **In a Docker container:** If you run Gemini CLI inside a Docker (or Podman)
  container, the IDE integration can still connect to the VS Code extension
  running on your host machine. The CLI is configured to automatically find the
  IDE server on `host.docker.internal`. No special configuration is usually
  required, but you may need to ensure your Docker networking setup allows
  connections from the container to the host.