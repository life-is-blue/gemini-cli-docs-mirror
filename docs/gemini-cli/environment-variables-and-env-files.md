## Environment variables and `.env` files

Environment variables are a common way to configure applications, especially for
sensitive information like API keys or for settings that might change between
environments. For authentication setup, see the
[Authentication documentation](/docs/get-started/authentication) which covers
all available authentication methods.

The CLI automatically loads environment variables from an `.env` file. The
loading order is:

1.  `.env` file in the current working directory.
2.  If not found, it searches upwards in parent directories until it finds an
    `.env` file or reaches the project root (identified by a `.git` folder) or
    the home directory.
3.  If still not found, it looks for `~/.env` (in the user's home directory).

**Environment variable exclusion:** Some environment variables (like `DEBUG` and
`DEBUG_MODE`) are automatically excluded from being loaded from project `.env`
files to prevent interference with gemini-cli behavior. Variables from
`.gemini/.env` files are never excluded. You can customize this behavior using
the `advanced.excludedEnvVars` setting in your `settings.json` file.

- **`GEMINI_API_KEY`**:
  - Your API key for the Gemini API.
  - One of several available
    [authentication methods](/docs/get-started/authentication).
  - Set this in your shell profile (e.g., `~/.bashrc`, `~/.zshrc`) or an `.env`
    file.
- **`GEMINI_MODEL`**:
  - Specifies the default Gemini model to use.
  - Overrides the hardcoded default
  - Example: `export GEMINI_MODEL="gemini-3-flash-preview"` (Windows PowerShell:
    `$env:GEMINI_MODEL="gemini-3-flash-preview"`)
- **`GEMINI_CLI_IDE_PID`**:
  - Manually specifies the PID of the IDE process to use for integration. This
    is useful when running Gemini CLI in a standalone terminal while still
    wanting to associate it with a specific IDE instance.
  - Overrides the automatic IDE detection logic.
- **`GEMINI_CLI_HOME`**:
  - Specifies the root directory for Gemini CLI's user-level configuration and
    storage.
  - By default, this is the user's system home directory. The CLI will create a
    `.gemini` folder inside this directory.
  - Useful for shared compute environments or keeping CLI state isolated.
  - Example: `export GEMINI_CLI_HOME="/path/to/user/config"` (Windows
    PowerShell: `$env:GEMINI_CLI_HOME="C:\path\to\user\config"`)
- **`GEMINI_CLI_SURFACE`**:
  - Specifies a custom label to include in the `User-Agent` header for API
    traffic reporting.
  - This is useful for tracking specific internal tools or distribution
    channels.
  - Example: `export GEMINI_CLI_SURFACE="my-custom-tool"` (Windows PowerShell:
    `$env:GEMINI_CLI_SURFACE="my-custom-tool"`)
- **`GOOGLE_API_KEY`**:
  - Your Google Cloud API key.
  - Required for using Vertex AI in express mode.
  - Ensure you have the necessary permissions.
  - Example: `export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"` (Windows PowerShell:
    `$env:GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"`).
- **`GOOGLE_CLOUD_PROJECT`**:
  - Your Google Cloud Project ID.
  - Required for using Code Assist or Vertex AI.
  - If using Vertex AI, ensure you have the necessary permissions in this
    project.
  - **Cloud Shell note:** When running in a Cloud Shell environment, this
    variable defaults to a special project allocated for Cloud Shell users. If
    you have `GOOGLE_CLOUD_PROJECT` set in your global environment in Cloud
    Shell, it will be overridden by this default. To use a different project in
    Cloud Shell, you must define `GOOGLE_CLOUD_PROJECT` in a `.env` file.
  - Example: `export GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"` (Windows
    PowerShell: `$env:GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"`).
- **`GOOGLE_APPLICATION_CREDENTIALS`** (string):
  - **Description:** The path to your Google Application Credentials JSON file.
  - **Example:**
    `export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"`
    (Windows PowerShell:
    `$env:GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\credentials.json"`)
- **`GOOGLE_GENAI_API_VERSION`**:
  - Specifies the API version to use for Gemini API requests.
  - When set, overrides the default API version used by the SDK.
  - Example: `export GOOGLE_GENAI_API_VERSION="v1"` (Windows PowerShell:
    `$env:GOOGLE_GENAI_API_VERSION="v1"`)
- **`OTLP_GOOGLE_CLOUD_PROJECT`**:
  - Your Google Cloud Project ID for Telemetry in Google Cloud
  - Example: `export OTLP_GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"` (Windows
    PowerShell: `$env:OTLP_GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"`).
- **`GEMINI_TELEMETRY_ENABLED`**:
  - Set to `true` or `1` to enable telemetry. Any other value is treated as
    disabling it.
  - Overrides the `telemetry.enabled` setting.
- **`GEMINI_TELEMETRY_TARGET`**:
  - Sets the telemetry target (`local` or `gcp`).
  - Overrides the `telemetry.target` setting.
- **`GEMINI_TELEMETRY_OTLP_ENDPOINT`**:
  - Sets the OTLP endpoint for telemetry.
  - Overrides the `telemetry.otlpEndpoint` setting.
- **`GEMINI_TELEMETRY_OTLP_PROTOCOL`**:
  - Sets the OTLP protocol (`grpc` or `http`).
  - Overrides the `telemetry.otlpProtocol` setting.
- **`GEMINI_TELEMETRY_LOG_PROMPTS`**:
  - Set to `true` or `1` to enable or disable logging of user prompts. Any other
    value is treated as disabling it.
  - Overrides the `telemetry.logPrompts` setting.
- **`GEMINI_TELEMETRY_OUTFILE`**:
  - Sets the file path to write telemetry to when the target is `local`.
  - Overrides the `telemetry.outfile` setting.
- **`GEMINI_TELEMETRY_USE_COLLECTOR`**:
  - Set to `true` or `1` to enable or disable using an external OTLP collector.
    Any other value is treated as disabling it.
  - Overrides the `telemetry.useCollector` setting.
- **`GOOGLE_CLOUD_LOCATION`**:
  - Your Google Cloud Project Location (e.g., us-central1).
  - Required for using Vertex AI in non-express mode.
  - Example: `export GOOGLE_CLOUD_LOCATION="YOUR_PROJECT_LOCATION"` (Windows
    PowerShell: `$env:GOOGLE_CLOUD_LOCATION="YOUR_PROJECT_LOCATION"`).
- **`GEMINI_SANDBOX`**:
  - Alternative to the `sandbox` setting in `settings.json`.
  - Accepts `true`, `false`, `docker`, `podman`, or a custom command string.
- **`GEMINI_SYSTEM_MD`**:
  - Replaces the built‑in system prompt with content from a Markdown file.
  - `true`/`1`: Use project default path `./.gemini/system.md`.
  - Any other string: Treat as a path (relative/absolute supported, `~`
    expands).
  - `false`/`0` or unset: Use the built‑in prompt. See
    [System Prompt Override](/docs/cli/system-prompt).
- **`GEMINI_WRITE_SYSTEM_MD`**:
  - Writes the current built‑in system prompt to a file for review.
  - `true`/`1`: Write to `./.gemini/system.md`. Otherwise treat the value as a
    path.
  - Run the CLI once with this set to generate the file.
- **`SEATBELT_PROFILE`** (macOS specific):
  - Switches the Seatbelt (`sandbox-exec`) profile on macOS.
  - `permissive-open`: (Default) Restricts writes to the project folder (and a
    few other folders, see
    `packages/cli/src/utils/sandbox-macos-permissive-open.sb`) but allows other
    operations.
  - `restrictive-open`: Declines operations by default, allows network.
  - `strict-open`: Restricts both reads and writes to the working directory,
    allows network.
  - `strict-proxied`: Same as `strict-open` but routes network through proxy.
  - `<profile_name>`: Uses a custom profile. To define a custom profile, create
    a file named `sandbox-macos-<profile_name>.sb` in your project's `.gemini/`
    directory (e.g., `my-project/.gemini/sandbox-macos-custom.sb`).
- **`DEBUG` or `DEBUG_MODE`** (often used by underlying libraries or the CLI
  itself):
  - Set to `true` or `1` to enable verbose debug logging, which can be helpful
    for troubleshooting.
  - **Note:** These variables are automatically excluded from project `.env`
    files by default to prevent interference with gemini-cli behavior. Use
    `.gemini/.env` files if you need to set these for gemini-cli specifically.
- **`NO_COLOR`**:
  - Set to any value to disable all color output in the CLI.
- **`CLI_TITLE`**:
  - Set to a string to customize the title of the CLI.
- **`CODE_ASSIST_ENDPOINT`**:
  - Specifies the endpoint for the code assist server.
  - This is useful for development and testing.