### `validateImportPath(importPath, basePath, allowedDirectories)`

Validates import paths to ensure they are safe and within allowed directories.

**Parameters:**

- `importPath` (string): The import path to validate
- `basePath` (string): The base directory for resolving relative paths
- `allowedDirectories` (string[]): Array of allowed directory paths

**Returns:** boolean - Whether the import path is valid