### `ide/diffAccepted` notification

When the user accepts the changes in a diff view (e.g., by clicking an "Apply"
or "Save" button), the plugin **MUST** send an `ide/diffAccepted` notification
to the CLI.

- **Payload:** The notification parameters **MUST** include the file path and
  the final content of the file. The content may differ from the original
  `newContent` if the user made manual edits in the diff view.

  ```typescript
  {
    // The absolute path to the file that was diffed.
    filePath: string;
    // The full content of the file after acceptance.
    content: string;
  }
  ```