## Centralized configuration: The system settings file

The most powerful tools for enterprise administration are the system-wide
settings files. These files allow you to define a baseline configuration
(`system-defaults.json`) and a set of overrides (`settings.json`) that apply to
all users on a machine. For a complete overview of configuration options, see
the [Configuration documentation](/docs/reference/configuration).

Settings are merged from four files. The precedence order for single-value
settings (like `theme`) is:

1. System Defaults (`system-defaults.json`)
2. User Settings (`~/.gemini/settings.json`)
3. Workspace Settings (`<project>/.gemini/settings.json`)
4. System Overrides (`settings.json`)

This means the System Overrides file has the final say. For settings that are
arrays (`includeDirectories`) or objects (`mcpServers`), the values are merged.

**Example of merging and precedence:**

Here is how settings from different levels are combined.

- **System defaults `system-defaults.json`:**

  ```json
  {
    "ui": {
      "theme": "default-corporate-theme"
    },
    "context": {
      "includeDirectories": ["/etc/gemini-cli/common-context"]
    }
  }
  ```

- **User `settings.json` (`~/.gemini/settings.json`):**

  ```json
  {
    "ui": {
      "theme": "user-preferred-dark-theme"
    },
    "mcpServers": {
      "corp-server": {
        "command": "/usr/local/bin/corp-server-dev"
      },
      "user-tool": {
        "command": "npm start --prefix ~/tools/my-tool"
      }
    },
    "context": {
      "includeDirectories": ["~/gemini-context"]
    }
  }
  ```

- **Workspace `settings.json` (`<project>/.gemini/settings.json`):**

  ```json
  {
    "ui": {
      "theme": "project-specific-light-theme"
    },
    "mcpServers": {
      "project-tool": {
        "command": "npm start"
      }
    },
    "context": {
      "includeDirectories": ["./project-context"]
    }
  }
  ```

- **System overrides `settings.json`:**
  ```json
  {
    "ui": {
      "theme": "system-enforced-theme"
    },
    "mcpServers": {
      "corp-server": {
        "command": "/usr/local/bin/corp-server-prod"
      }
    },
    "context": {
      "includeDirectories": ["/etc/gemini-cli/global-context"]
    }
  }
  ```

This results in the following merged configuration:

- **Final merged configuration:**
  ```json
  {
    "ui": {
      "theme": "system-enforced-theme"
    },
    "mcpServers": {
      "corp-server": {
        "command": "/usr/local/bin/corp-server-prod"
      },
      "user-tool": {
        "command": "npm start --prefix ~/tools/my-tool"
      },
      "project-tool": {
        "command": "npm start"
      }
    },
    "context": {
      "includeDirectories": [
        "/etc/gemini-cli/common-context",
        "~/gemini-context",
        "./project-context",
        "/etc/gemini-cli/global-context"
      ]
    }
  }
  ```

**Why:**

- **`theme`**: The value from the system overrides (`system-enforced-theme`) is
  used, as it has the highest precedence.
- **`mcpServers`**: The objects are merged. The `corp-server` definition from
  the system overrides takes precedence over the user's definition. The unique
  `user-tool` and `project-tool` are included.
- **`includeDirectories`**: The arrays are concatenated in the order of System
  Defaults, User, Workspace, and then System Overrides.

- **Location**:
  - **Linux**: `/etc/gemini-cli/settings.json`
  - **Windows**: `C:\ProgramData\gemini-cli\settings.json`
  - **macOS**: `/Library/Application Support/GeminiCli/settings.json`
  - The path can be overridden using the `GEMINI_CLI_SYSTEM_SETTINGS_PATH`
    environment variable.
- **Control**: This file should be managed by system administrators and
  protected with appropriate file permissions to prevent unauthorized
  modification by users.

By using the system settings file, you can enforce the security and
configuration patterns described below.