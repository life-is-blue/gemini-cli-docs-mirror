## Debugging tips

- **CLI debugging:**
  - Use the `--debug` flag for more detailed output. In interactive mode, press
    F12 to view the debug console.
  - Check the CLI logs, often found in a user-specific configuration or cache
    directory.

- **Core debugging:**
  - Check the server console output for error messages or stack traces.
  - Increase log verbosity if configurable. For example, set the `DEBUG_MODE`
    environment variable to `true` or `1`.
  - Use Node.js debugging tools (e.g., `node --inspect`) if you need to step
    through server-side code.

- **Tool issues:**
  - If a specific tool is failing, try to isolate the issue by running the
    simplest possible version of the command or operation the tool performs.
  - For `run_shell_command`, check that the command works directly in your shell
    first.
  - For _file system tools_, verify that paths are correct and check the
    permissions.

- **Pre-flight checks:**
  - Always run `npm run preflight` before committing code. This can catch many
    common issues related to formatting, linting, and type errors.