### Agent card fetching and auth

When connecting to a remote agent, Gemini CLI first fetches the agent card
**without** authentication. If the card endpoint returns a `401` or `403`, it
retries the fetch **with** the configured auth headers. This lets agents have
publicly accessible cards while protecting their task endpoints, or to protect
both behind auth.