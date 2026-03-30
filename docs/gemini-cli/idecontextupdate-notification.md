### `ide/contextUpdate` notification

The plugin **MAY** send an `ide/contextUpdate`
[notification](https://modelcontextprotocol.io/specification/2025-06-18/basic/index#notifications)
to the CLI whenever the user's context changes.

- **Triggering events:** This notification should be sent (with a recommended
  debounce of 50ms) when:
  - A file is opened, closed, or focused.
  - The user's cursor position or text selection changes in the active file.
- **Payload (`IdeContext`):** The notification parameters **MUST** be an
  `IdeContext` object:

  ```typescript
  interface IdeContext {
    workspaceState?: {
      openFiles?: File[];
      isTrusted?: boolean;
    };
  }

  interface File {
    // Absolute path to the file
    path: string;
    // Last focused Unix timestamp (for ordering)
    timestamp: number;
    // True if this is the currently focused file
    isActive?: boolean;
    cursor?: {
      // 1-based line number
      line: number;
      // 1-based character number
      character: number;
    };
    // The text currently selected by the user
    selectedText?: string;
  }
  ```

<!-- prettier-ignore -->
> [!NOTE]
> The `openFiles` list should only include files that exist on disk.
> Virtual files (e.g., unsaved files without a path, editor settings pages)
> **MUST** be excluded.