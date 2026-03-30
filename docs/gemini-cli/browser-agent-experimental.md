### Browser Agent (experimental)

- **Name:** `browser_agent`
- **Purpose:** Automate web browser tasks — navigating websites, filling forms,
  clicking buttons, and extracting information from web pages — using the
  accessibility tree.
- **When to use:** "Go to example.com and fill out the contact form," "Extract
  the pricing table from this page," "Click the login button and enter my
  credentials."

<!-- prettier-ignore -->
> [!NOTE]
> This is a preview feature currently under active development.

#### Prerequisites

The browser agent requires:

- **Chrome** version 144 or later (any recent stable release will work).
- **Node.js** with `npx` available (used to launch the
  [`chrome-devtools-mcp`](https://www.npmjs.com/package/chrome-devtools-mcp)
  server).

#### Enabling the browser agent

The browser agent is disabled by default. Enable it in your `settings.json`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    }
  }
}
```

#### Session modes

The `sessionMode` setting controls how Chrome is launched and managed. Set it
under `agents.browser`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "sessionMode": "persistent"
    }
  }
}
```

The available modes are:

| Mode         | Description                                                                                                                                                                                 |
| :----------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `persistent` | **(Default)** Launches Chrome with a persistent profile stored at `~/.gemini/cli-browser-profile/`. Cookies, history, and settings are preserved between sessions.                          |
| `isolated`   | Launches Chrome with a temporary profile that is deleted after each session. Use this for clean-state automation.                                                                           |
| `existing`   | Attaches to an already-running Chrome instance. You must enable remote debugging first by navigating to `chrome://inspect/#remote-debugging` in Chrome. No new browser process is launched. |

#### Configuration reference

All browser-specific settings go under `agents.browser` in your `settings.json`.

| Setting       | Type      | Default        | Description                                                                                     |
| :------------ | :-------- | :------------- | :---------------------------------------------------------------------------------------------- |
| `sessionMode` | `string`  | `"persistent"` | How Chrome is managed: `"persistent"`, `"isolated"`, or `"existing"`.                           |
| `headless`    | `boolean` | `false`        | Run Chrome in headless mode (no visible window).                                                |
| `profilePath` | `string`  | —              | Custom path to a browser profile directory.                                                     |
| `visualModel` | `string`  | —              | Model override for the visual agent (for example, `"gemini-2.5-computer-use-preview-10-2025"`). |

#### Security

The browser agent enforces the following security restrictions:

- **Blocked URL patterns:** `file://`, `javascript:`, `data:text/html`,
  `chrome://extensions`, and `chrome://settings/passwords` are always blocked.
- **Sensitive action confirmation:** Actions like form filling, file uploads,
  and form submissions require user confirmation through the standard policy
  engine.

#### Visual agent

By default, the browser agent interacts with pages through the accessibility
tree using element `uid` values. For tasks that require visual identification
(for example, "click the yellow button" or "find the red error message"), you
can enable the visual agent by setting a `visualModel`:

```json
{
  "agents": {
    "overrides": {
      "browser_agent": {
        "enabled": true
      }
    },
    "browser": {
      "visualModel": "gemini-2.5-computer-use-preview-10-2025"
    }
  }
}
```

When enabled, the agent gains access to the `analyze_screenshot` tool, which
captures a screenshot and sends it to the vision model for analysis. The model
returns coordinates and element descriptions that the browser agent uses with
the `click_at` tool for precise, coordinate-based interactions.

<!-- prettier-ignore -->
> [!NOTE]
> The visual agent requires API key or Vertex AI authentication. It is
> not available when using "Sign in with Google".