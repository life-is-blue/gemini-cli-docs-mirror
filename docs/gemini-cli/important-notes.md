## Important notes

- **Security:** Be cautious when executing commands, especially those
  constructed from user input, to prevent security vulnerabilities.
- **Error handling:** Check the `Stderr`, `Error`, and `Exit Code` fields to
  determine if a command executed successfully.
- **Background processes:** When a command is run in the background with `&`,
  the tool will return immediately and the process will continue to run in the
  background. The `Background PIDs` field will contain the process ID of the
  background process.