## Common error messages and solutions

- **Error: `EADDRINUSE` (Address already in use) when starting an MCP server.**
  - **Cause:** Another process is already using the port that the MCP server is
    trying to bind to.
  - **Solution:** Either stop the other process that is using the port or
    configure the MCP server to use a different port.

- **Error: Command not found (when attempting to run Gemini CLI with
  `gemini`).**
  - **Cause:** Gemini CLI is not correctly installed or it is not in your
    system's `PATH`.
  - **Solution:** The update depends on how you installed Gemini CLI:
    - If you installed `gemini` globally, check that your `npm` global binary
      directory is in your `PATH`. You can update Gemini CLI using the command
      `npm install -g @google/gemini-cli@latest`.
    - If you are running `gemini` from source, ensure you are using the correct
      command to invoke it (e.g., `node packages/cli/dist/index.js ...`). To
      update Gemini CLI, pull the latest changes from the repository, and then
      rebuild using the command `npm run build`.

- **Error: `MODULE_NOT_FOUND` or import errors.**
  - **Cause:** Dependencies are not installed correctly, or the project hasn't
    been built.
  - **Solution:**
    1.  Run `npm install` to ensure all dependencies are present.
    2.  Run `npm run build` to compile the project.
    3.  Verify that the build completed successfully with `npm run start`.

- **Error: "Operation not permitted", "Permission denied", or similar.**
  - **Cause:** When sandboxing is enabled, Gemini CLI may attempt operations
    that are restricted by your sandbox configuration, such as writing outside
    the project directory or system temp directory.
  - **Solution:** Refer to the [Configuration: Sandboxing](/docs/cli/sandbox)
    documentation for more information, including how to customize your sandbox
    configuration.

- **Gemini CLI is not running in interactive mode in "CI" environments**
  - **Issue:** The Gemini CLI does not enter interactive mode (no prompt
    appears) if an environment variable starting with `CI_` (e.g., `CI_TOKEN`)
    is set. This is because the `is-in-ci` package, used by the underlying UI
    framework, detects these variables and assumes a non-interactive CI
    environment.
  - **Cause:** The `is-in-ci` package checks for the presence of `CI`,
    `CONTINUOUS_INTEGRATION`, or any environment variable with a `CI_` prefix.
    When any of these are found, it signals that the environment is
    non-interactive, which prevents the Gemini CLI from starting in its
    interactive mode.
  - **Solution:** If the `CI_` prefixed variable is not needed for the CLI to
    function, you can temporarily unset it for the command. e.g.,
    `env -u CI_TOKEN gemini`

- **DEBUG mode not working from project .env file**
  - **Issue:** Setting `DEBUG=true` in a project's `.env` file doesn't enable
    debug mode for gemini-cli.
  - **Cause:** The `DEBUG` and `DEBUG_MODE` variables are automatically excluded
    from project `.env` files to prevent interference with gemini-cli behavior.
  - **Solution:** Use a `.gemini/.env` file instead, or configure the
    `advanced.excludedEnvVars` setting in your `settings.json` to exclude fewer
    variables.

- **Warning: `npm WARN deprecated node-domexception@1.0.0` or
  `npm WARN deprecated glob` during install/update**
  - **Issue:** When installing or updating the Gemini CLI globally via
    `npm install -g @google/gemini-cli` or `npm update -g @google/gemini-cli`,
    you might see deprecation warnings regarding `node-domexception` or old
    versions of `glob`.
  - **Cause:** These warnings occur because some dependencies (or their
    sub-dependencies, like `google-auth-library`) rely on older package
    versions. Since Gemini CLI requires Node.js 20 or higher, the platform's
    native features (like the native `DOMException`) are used, making these
    warnings purely informational.
  - **Solution:** These warnings are harmless and can be safely ignored. Your
    installation or update will complete successfully and function properly
    without any action required.