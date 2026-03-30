## Security considerations

The core plays a vital role in security:

- **API key management:** It handles the `GEMINI_API_KEY` and ensures it's used
  securely when communicating with the Gemini API.
- **Tool execution:** When tools interact with the local system (e.g.,
  `run_shell_command`), the core (and its underlying tool implementations) must
  do so with appropriate caution, often involving sandboxing mechanisms to
  prevent unintended modifications.