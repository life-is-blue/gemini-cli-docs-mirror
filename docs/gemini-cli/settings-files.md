## Settings files

Gemini CLI uses JSON settings files for persistent configuration. There are four
locations for these files:

<!-- prettier-ignore -->
> [!TIP]
> JSON-aware editors can use autocomplete and validation by pointing to
> the generated schema at `schemas/settings.schema.json` in this repository.
> When working outside the repo, reference the hosted schema at
> `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/schemas/settings.schema.json`.

- **System defaults file:**
  - **Location:** `/etc/gemini-cli/system-defaults.json` (Linux),
    `C:\ProgramData\gemini-cli\system-defaults.json` (Windows) or
    `/Library/Application Support/GeminiCli/system-defaults.json` (macOS). The
    path can be overridden using the `GEMINI_CLI_SYSTEM_DEFAULTS_PATH`
    environment variable.
  - **Scope:** Provides a base layer of system-wide default settings. These
    settings have the lowest precedence and are intended to be overridden by
    user, project, or system override settings.
- **User settings file:**
  - **Location:** `~/.gemini/settings.json` (where `~` is your home directory).
  - **Scope:** Applies to all Gemini CLI sessions for the current user. User
    settings override system defaults.
- **Project settings file:**
  - **Location:** `.gemini/settings.json` within your project's root directory.
  - **Scope:** Applies only when running Gemini CLI from that specific project.
    Project settings override user settings and system defaults.
- **System settings file:**
  - **Location:** `/etc/gemini-cli/settings.json` (Linux),
    `C:\ProgramData\gemini-cli\settings.json` (Windows) or
    `/Library/Application Support/GeminiCli/settings.json` (macOS). The path can
    be overridden using the `GEMINI_CLI_SYSTEM_SETTINGS_PATH` environment
    variable.
  - **Scope:** Applies to all Gemini CLI sessions on the system, for all users.
    System settings act as overrides, taking precedence over all other settings
    files. May be useful for system administrators at enterprises to have
    controls over users' Gemini CLI setups.

**Note on environment variables in settings:** String values within your
`settings.json` and `gemini-extension.json` files can reference environment
variables using either `$VAR_NAME` or `${VAR_NAME}` syntax. These variables will
be automatically resolved when the settings are loaded. For example, if you have
an environment variable `MY_API_TOKEN`, you could use it in `settings.json` like
this: `"apiKey": "$MY_API_TOKEN"`. Additionally, each extension can have its own
`.env` file in its directory, which will be loaded automatically.

**Note for Enterprise Users:** For guidance on deploying and managing Gemini CLI
in a corporate environment, please see the
[Enterprise Configuration](/docs/cli/enterprise) documentation.