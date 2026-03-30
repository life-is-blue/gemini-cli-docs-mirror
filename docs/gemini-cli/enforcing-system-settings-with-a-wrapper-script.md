### Enforcing system settings with a wrapper script

While the `GEMINI_CLI_SYSTEM_SETTINGS_PATH` environment variable provides
flexibility, a user could potentially override it to point to a different
settings file, bypassing the centrally managed configuration. To mitigate this,
enterprises can deploy a wrapper script or alias that ensures the environment
variable is always set to the corporate-controlled path.

This approach ensures that no matter how the user calls the `gemini` command,
the enterprise settings are always loaded with the highest precedence.

**Example wrapper script:**

Administrators can create a script named `gemini` and place it in a directory
that appears earlier in the user's `PATH` than the actual Gemini CLI binary
(e.g., `/usr/local/bin/gemini`).

```bash
#!/bin/bash