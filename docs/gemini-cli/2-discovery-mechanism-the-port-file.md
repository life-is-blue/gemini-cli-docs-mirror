### 2. Discovery mechanism: The port file

For Gemini CLI to connect, it needs to discover which IDE instance it's running
in and what port your server is using. The plugin **MUST** facilitate this by
creating a "discovery file."

- **How the CLI finds the file:** The CLI determines the Process ID (PID) of the
  IDE it's running in by traversing the process tree. It then looks for a
  discovery file that contains this PID in its name.
- **File location:** The file must be created in a specific directory:
  `os.tmpdir()/gemini/ide/`. Your plugin must create this directory if it
  doesn't exist.
- **File naming convention:** The filename is critical and **MUST** follow the
  pattern: `gemini-ide-server-${PID}-${PORT}.json`
  - `${PID}`: The process ID of the parent IDE process. Your plugin must
    determine this PID and include it in the filename.
  - `${PORT}`: The port your MCP server is listening on.
- **File content and workspace validation:** The file **MUST** contain a JSON
  object with the following structure:

  ```json
  {
    "port": 12345,
    "workspacePath": "/path/to/project1:/path/to/project2",
    "authToken": "a-very-secret-token",
    "ideInfo": {
      "name": "vscode",
      "displayName": "VS Code"
    }
  }
  ```
  - `port` (number, required): The port of the MCP server.
  - `workspacePath` (string, required): A list of all open workspace root paths,
    delimited by the OS-specific path separator (`:` for Linux/macOS, `;` for
    Windows). The CLI uses this path to ensure it's running in the same project
    folder that's open in the IDE. If the CLI's current working directory is not
    a sub-directory of `workspacePath`, the connection will be rejected. Your
    plugin **MUST** provide the correct, absolute path(s) to the root of the
    open workspace(s).
  - `authToken` (string, required): A secret token for securing the connection.
    The CLI will include this token in an `Authorization: Bearer <token>` header
    on all requests.
  - `ideInfo` (object, required): Information about the IDE.
    - `name` (string, required): A short, lowercase identifier for the IDE
      (e.g., `vscode`, `jetbrains`).
    - `displayName` (string, required): A user-friendly name for the IDE (e.g.,
      `VS Code`, `JetBrains IDE`).

- **Authentication:** To secure the connection, the plugin **MUST** generate a
  unique, secret token and include it in the discovery file. The CLI will then
  include this token in the `Authorization` header for all requests to the MCP
  server (e.g., `Authorization: Bearer a-very-secret-token`). Your server
  **MUST** validate this token on every request and reject any that are
  unauthorized.
- **Tie-breaking with environment variables (recommended):** For the most
  reliable experience, your plugin **SHOULD** both create the discovery file and
  set the `GEMINI_CLI_IDE_SERVER_PORT` environment variable in the integrated
  terminal. The file serves as the primary discovery mechanism, but the
  environment variable is crucial for tie-breaking. If a user has multiple IDE
  windows open for the same workspace, the CLI uses the
  `GEMINI_CLI_IDE_SERVER_PORT` variable to identify and connect to the correct
  window's server.