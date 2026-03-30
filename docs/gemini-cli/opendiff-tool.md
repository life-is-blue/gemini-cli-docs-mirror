### `openDiff` tool

The plugin **MUST** register an `openDiff` tool on its MCP server.

- **Description:** This tool instructs the IDE to open a modifiable diff view
  for a specific file.
- **Request (`OpenDiffRequest`):** The tool is invoked via a `tools/call`
  request. The `arguments` field within the request's `params` **MUST** be an
  `OpenDiffRequest` object.

  ```typescript
  interface OpenDiffRequest {
    // The absolute path to the file to be diffed.
    filePath: string;
    // The proposed new content for the file.
    newContent: string;
  }
  ```

- **Response (`CallToolResult`):** The tool **MUST** immediately return a
  `CallToolResult` to acknowledge the request and report whether the diff view
  was successfully opened.
  - On Success: If the diff view was opened successfully, the response **MUST**
    contain empty content (i.e., `content: []`).
  - On Failure: If an error prevented the diff view from opening, the response
    **MUST** have `isError: true` and include a `TextContent` block in the
    `content` array describing the error.

  The actual outcome of the diff (acceptance or rejection) is communicated
  asynchronously via notifications.