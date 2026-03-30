# Example: Adding an HTTP server with an authentication header
gemini mcp add --transport http --header "Authorization: Bearer abc123" secure-http https://api.example.com/mcp/
```

#### Adding an SSE server

This transport is for servers that use Server-Sent Events (SSE).

```bash