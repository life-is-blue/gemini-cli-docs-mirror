### VS Code companion extension errors

#### Connection errors

- **Message:**
  `🔴 Disconnected: Failed to connect to IDE companion extension in [IDE Name]. Please ensure the extension is running. To install the extension, run /ide install.`
  - **Cause:** Gemini CLI could not find the necessary environment variables
    (`GEMINI_CLI_IDE_WORKSPACE_PATH` or `GEMINI_CLI_IDE_SERVER_PORT`) to connect
    to the IDE. This usually means the IDE companion extension is not running or
    did not initialize correctly.
  - **Solution:**
    1.  Make sure you have installed the **Gemini CLI Companion** extension in
        your IDE and that it is enabled.
    2.  Open a new terminal window in your IDE to ensure it picks up the correct
        environment.

- **Message:**
  `🔴 Disconnected: IDE connection error. The connection was lost unexpectedly. Please try reconnecting by running /ide enable`
  - **Cause:** The connection to the IDE companion was lost.
  - **Solution:** Run `/ide enable` to try and reconnect. If the issue
    continues, open a new terminal window or restart your IDE.

#### Manual PID override

If automatic IDE detection fails, or if you are running Gemini CLI in a
standalone terminal and want to manually associate it with a specific IDE
instance, you can set the `GEMINI_CLI_IDE_PID` environment variable to the
process ID (PID) of your IDE.

**macOS/Linux**

```bash
export GEMINI_CLI_IDE_PID=12345
```

**Windows (PowerShell)**

```powershell
$env:GEMINI_CLI_IDE_PID=12345
```

When this variable is set, Gemini CLI will skip automatic detection and attempt
to connect using the provided PID.

#### Configuration errors

- **Message:**
  `🔴 Disconnected: Directory mismatch. Gemini CLI is running in a different location than the open workspace in [IDE Name]. Please run the CLI from one of the following directories: [List of directories]`
  - **Cause:** The CLI's current working directory is outside the workspace you
    have open in your IDE.
  - **Solution:** `cd` into the same directory that is open in your IDE and
    restart the CLI.

- **Message:**
  `🔴 Disconnected: To use this feature, please open a workspace folder in [IDE Name] and try again.`
  - **Cause:** You have no workspace open in your IDE.
  - **Solution:** Open a workspace in your IDE and restart the CLI.

#### General errors

- **Message:**
  `IDE integration is not supported in your current environment. To use this feature, run Gemini CLI in one of these supported IDEs: [List of IDEs]`
  - **Cause:** You are running Gemini CLI in a terminal or environment that is
    not a supported IDE.
  - **Solution:** Run Gemini CLI from the integrated terminal of a supported
    IDE, like Antigravity or VS Code.

- **Message:**
  `No installer is available for IDE. Please install Gemini CLI Companion extension manually from the marketplace.`
  - **Cause:** You ran `/ide install`, but the CLI does not have an automated
    installer for your specific IDE.
  - **Solution:** Open your IDE's extension marketplace, search for "Gemini CLI
    Companion", and
    [install it manually](#3-manual-installation-from-a-marketplace).