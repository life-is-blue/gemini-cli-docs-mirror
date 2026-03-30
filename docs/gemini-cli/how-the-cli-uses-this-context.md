### How the CLI uses this context

After receiving the `IdeContext` object, the CLI performs several normalization
and truncation steps before sending the information to the model.

- **File ordering:** The CLI uses the `timestamp` field to determine the most
  recently used files. It sorts the `openFiles` list based on this value.
  Therefore, your plugin **MUST** provide an accurate Unix timestamp for when a
  file was last focused.
- **Active file:** The CLI considers only the most recent file (after sorting)
  to be the "active" file. It will ignore the `isActive` flag on all other files
  and clear their `cursor` and `selectedText` fields. Your plugin should focus
  on setting `isActive: true` and providing cursor/selection details only for
  the currently focused file.
- **Truncation:** To manage token limits, the CLI truncates both the file list
  (to 10 files) and the `selectedText` (to 16KB).

While the CLI handles the final truncation, it is highly recommended that your
plugin also limits the amount of context it sends.