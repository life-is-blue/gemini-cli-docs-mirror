### `closeDiff` tool

The plugin **MUST** register a `closeDiff` tool on its MCP server.

- **Description:** This tool instructs the IDE to close an open diff view for a
  specific file.
- **Request (`CloseDiffRequest`):** The tool is invoked via a `tools/call`
  request. The `arguments` field within the request's `params` **MUST** be an
  `CloseDiffRequest` object.

  ```typescript
  interface CloseDiffRequest {
    // The absolute path to the file whose diff view should be closed.
    filePath: string;
  }
  ```

- **Response (`CallToolResult`):** The tool **MUST** return a `CallToolResult`.
  - On Success: If the diff view was closed successfully, the response **MUST**
    include a single **TextContent** block in the content array containing the
    file's final content before closing.
  - On Failure: If an error prevented the diff view from closing, the response
    **MUST** have `isError: true` and include a `TextContent` block in the
    `content` array describing the error.