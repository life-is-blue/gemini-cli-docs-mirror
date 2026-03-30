## Architecture and protocol basics

ACP mode establishes a client-server relationship between your tool (the client)
and Gemini CLI (the server).

- **Communication:** The entire communication happens over standard input/output
  (stdio) using the JSON-RPC 2.0 protocol.
- **Client's role:** The client is responsible for sending requests (e.g.,
  prompts) and handling responses and notifications from Gemini CLI.
- **Gemini CLI's role:** In ACP mode, Gemini CLI listens for incoming JSON-RPC
  requests, processes them, and sends back responses.

The core of the ACP implementation can be found in
`packages/cli/src/acp/acpClient.ts`.