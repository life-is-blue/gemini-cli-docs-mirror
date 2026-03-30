### `ide/diffRejected` notification

When the user rejects the changes (e.g., by closing the diff view without
accepting), the plugin **MUST** send an `ide/diffRejected` notification to the
CLI.

- **Payload:** The notification parameters **MUST** include the file path of the
  rejected diff.

  ```typescript
  {
    // The absolute path to the file that was diffed.
    filePath: string;
  }
  ```