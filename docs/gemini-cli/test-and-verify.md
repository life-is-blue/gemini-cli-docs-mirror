## Test and verify

Test your extension thoroughly before releasing it to users.

- **Manual verification:** Use `gemini extensions link` to test your extension
  in a live CLI session. Verify that tools appear in the debug console (F12) and
  that custom commands resolve correctly.
- **Automated testing:** If your extension includes an MCP server, write unit
  tests for your tool logic using a framework like Vitest or Jest. You can test
  MCP tools in isolation by mocking the transport layer.