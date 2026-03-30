### Environment variable expansion

Gemini CLI automatically expands environment variables in the `env` block of
your MCP server configuration. This allows you to securely reference variables
defined in your shell or environment without hardcoding sensitive information
directly in your `settings.json` file.

The expansion utility supports:

- **POSIX/Bash syntax:** `$VARIABLE_NAME` or `${VARIABLE_NAME}` (supported on
  all platforms)
- **Windows syntax:** `%VARIABLE_NAME%` (supported only when running on Windows)

If a variable is not defined in the current environment, it resolves to an empty
string.

**Example:**

```json
"env": {
  "API_KEY": "$MY_EXTERNAL_TOKEN",
  "LOG_LEVEL": "$LOG_LEVEL",
  "TEMP_DIR": "%TEMP%"
}
```