### How it works

To return rich content, your tool's response must adhere to the MCP
specification for a
[`CallToolResult`](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool-result).
The `content` field of the result should be an array of `ContentBlock` objects.
The Gemini CLI will correctly process this array, separating text from binary
data and packaging it for the model.

You can mix and match different content block types in the `content` array. The
supported block types include:

- `text`
- `image`
- `audio`
- `resource` (embedded content)
- `resource_link`