### Error handling for `@` commands

- If the path specified after `@` is not found or is invalid, an error message
  will be displayed, and the query might not be sent to the Gemini model, or it
  will be sent without the file content.
- If the `read_many_files` tool encounters an error (e.g., permission issues),
  this will also be reported.