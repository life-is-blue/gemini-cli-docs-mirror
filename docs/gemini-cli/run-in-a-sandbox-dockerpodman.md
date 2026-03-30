### Run in a sandbox (Docker/Podman)

For security and isolation, Gemini CLI can be run inside a container. This is
the default way that the CLI executes tools that might have side effects.

- **Directly from the registry:** You can run the published sandbox image
  directly. This is useful for environments where you only have Docker and want
  to run the CLI.
  ```bash
  # Run the published sandbox image
  docker run --rm -it us-docker.pkg.dev/gemini-code-dev/gemini-cli/sandbox:0.1.1
  ```
- **Using the `--sandbox` flag:** If you have Gemini CLI installed locally
  (using the standard installation described above), you can instruct it to run
  inside the sandbox container.
  ```bash
  gemini --sandbox -y -p "your prompt here"
  ```