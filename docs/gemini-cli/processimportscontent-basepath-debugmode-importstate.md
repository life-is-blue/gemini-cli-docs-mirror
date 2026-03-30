### `processImports(content, basePath, debugMode?, importState?)`

Processes import statements in GEMINI.md content.

**Parameters:**

- `content` (string): The content to process for imports
- `basePath` (string): The directory path where the current file is located
- `debugMode` (boolean, optional): Whether to enable debug logging (default:
  false)
- `importState` (ImportState, optional): State tracking for circular import
  prevention

**Returns:** Promise&lt;ProcessImportsResult&gt; - Object containing processed
content and import tree