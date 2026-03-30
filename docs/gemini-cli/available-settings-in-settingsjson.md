### Available settings in `settings.json`

Settings are organized into categories. All settings should be placed within
their corresponding top-level category object in your `settings.json` file.

<!-- SETTINGS-AUTOGEN:START -->

#### `policyPaths`

- **`policyPaths`** (array):
  - **Description:** Additional policy files or directories to load.
  - **Default:** `[]`
  - **Requires restart:** Yes

#### `adminPolicyPaths`

- **`adminPolicyPaths`** (array):
  - **Description:** Additional admin policy files or directories to load.
  - **Default:** `[]`
  - **Requires restart:** Yes

#### `general`

- **`general.preferredEditor`** (string):
  - **Description:** The preferred editor to open files in.
  - **Default:** `undefined`

- **`general.vimMode`** (boolean):
  - **Description:** Enable Vim keybindings
  - **Default:** `false`

- **`general.defaultApprovalMode`** (enum):
  - **Description:** The default approval mode for tool execution. 'default'
    prompts for approval, 'auto_edit' auto-approves edit tools, and 'plan' is
    read-only mode. YOLO mode (auto-approve all actions) can only be enabled via
    command line (--yolo or --approval-mode=yolo).
  - **Default:** `"default"`
  - **Values:** `"default"`, `"auto_edit"`, `"plan"`

- **`general.devtools`** (boolean):
  - **Description:** Enable DevTools inspector on launch.
  - **Default:** `false`

- **`general.enableAutoUpdate`** (boolean):
  - **Description:** Enable automatic updates.
  - **Default:** `true`

- **`general.enableAutoUpdateNotification`** (boolean):
  - **Description:** Enable update notification prompts.
  - **Default:** `true`

- **`general.enableNotifications`** (boolean):
  - **Description:** Enable run-event notifications for action-required prompts
    and session completion.
  - **Default:** `false`

- **`general.checkpointing.enabled`** (boolean):
  - **Description:** Enable session checkpointing for recovery
  - **Default:** `false`
  - **Requires restart:** Yes

- **`general.plan.directory`** (string):
  - **Description:** The directory where planning artifacts are stored. If not
    specified, defaults to the system temporary directory. A custom directory
    requires a policy to allow write access in Plan Mode.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`general.plan.modelRouting`** (boolean):
  - **Description:** Automatically switch between Pro and Flash models based on
    Plan Mode status. Uses Pro for the planning phase and Flash for the
    implementation phase.
  - **Default:** `true`

- **`general.retryFetchErrors`** (boolean):
  - **Description:** Retry on "exception TypeError: fetch failed sending
    request" errors.
  - **Default:** `true`

- **`general.maxAttempts`** (number):
  - **Description:** Maximum number of attempts for requests to the main chat
    model. Cannot exceed 10.
  - **Default:** `10`

- **`general.debugKeystrokeLogging`** (boolean):
  - **Description:** Enable debug logging of keystrokes to the console.
  - **Default:** `false`

- **`general.sessionRetention.enabled`** (boolean):
  - **Description:** Enable automatic session cleanup
  - **Default:** `true`

- **`general.sessionRetention.maxAge`** (string):
  - **Description:** Automatically delete chats older than this time period
    (e.g., "30d", "7d", "24h", "1w")
  - **Default:** `"30d"`

- **`general.sessionRetention.maxCount`** (number):
  - **Description:** Alternative: Maximum number of sessions to keep (most
    recent)
  - **Default:** `undefined`

- **`general.sessionRetention.minRetention`** (string):
  - **Description:** Minimum retention period (safety limit, defaults to "1d")
  - **Default:** `"1d"`

#### `output`

- **`output.format`** (enum):
  - **Description:** The format of the CLI output. Can be `text` or `json`.
  - **Default:** `"text"`
  - **Values:** `"text"`, `"json"`

#### `ui`

- **`ui.theme`** (string):
  - **Description:** The color theme for the UI. See the CLI themes guide for
    available options.
  - **Default:** `undefined`

- **`ui.autoThemeSwitching`** (boolean):
  - **Description:** Automatically switch between default light and dark themes
    based on terminal background color.
  - **Default:** `true`

- **`ui.terminalBackgroundPollingInterval`** (number):
  - **Description:** Interval in seconds to poll the terminal background color.
  - **Default:** `60`

- **`ui.customThemes`** (object):
  - **Description:** Custom theme definitions.
  - **Default:** `{}`

- **`ui.hideWindowTitle`** (boolean):
  - **Description:** Hide the window title bar
  - **Default:** `false`
  - **Requires restart:** Yes

- **`ui.inlineThinkingMode`** (enum):
  - **Description:** Display model thinking inline: off or full.
  - **Default:** `"off"`
  - **Values:** `"off"`, `"full"`

- **`ui.showStatusInTitle`** (boolean):
  - **Description:** Show Gemini CLI model thoughts in the terminal window title
    during the working phase
  - **Default:** `false`

- **`ui.dynamicWindowTitle`** (boolean):
  - **Description:** Update the terminal window title with current status icons
    (Ready: ◇, Action Required: ✋, Working: ✦)
  - **Default:** `true`

- **`ui.showHomeDirectoryWarning`** (boolean):
  - **Description:** Show a warning when running Gemini CLI in the home
    directory.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`ui.showCompatibilityWarnings`** (boolean):
  - **Description:** Show warnings about terminal or OS compatibility issues.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`ui.hideTips`** (boolean):
  - **Description:** Hide helpful tips in the UI
  - **Default:** `false`

- **`ui.escapePastedAtSymbols`** (boolean):
  - **Description:** When enabled, @ symbols in pasted text are escaped to
    prevent unintended @path expansion.
  - **Default:** `false`

- **`ui.showShortcutsHint`** (boolean):
  - **Description:** Show the "? for shortcuts" hint above the input.
  - **Default:** `true`

- **`ui.hideBanner`** (boolean):
  - **Description:** Hide the application banner
  - **Default:** `false`

- **`ui.hideContextSummary`** (boolean):
  - **Description:** Hide the context summary (GEMINI.md, MCP servers) above the
    input.
  - **Default:** `false`

- **`ui.footer.items`** (array):
  - **Description:** List of item IDs to display in the footer. Rendered in
    order
  - **Default:** `undefined`

- **`ui.footer.showLabels`** (boolean):
  - **Description:** Display a second line above the footer items with
    descriptive headers (e.g., /model).
  - **Default:** `true`

- **`ui.footer.hideCWD`** (boolean):
  - **Description:** Hide the current working directory in the footer.
  - **Default:** `false`

- **`ui.footer.hideSandboxStatus`** (boolean):
  - **Description:** Hide the sandbox status indicator in the footer.
  - **Default:** `false`

- **`ui.footer.hideModelInfo`** (boolean):
  - **Description:** Hide the model name and context usage in the footer.
  - **Default:** `false`

- **`ui.footer.hideContextPercentage`** (boolean):
  - **Description:** Hides the context window usage percentage.
  - **Default:** `true`

- **`ui.hideFooter`** (boolean):
  - **Description:** Hide the footer from the UI
  - **Default:** `false`

- **`ui.collapseDrawerDuringApproval`** (boolean):
  - **Description:** Whether to collapse the UI drawer when a tool is awaiting
    confirmation.
  - **Default:** `true`

- **`ui.showMemoryUsage`** (boolean):
  - **Description:** Display memory usage information in the UI
  - **Default:** `false`

- **`ui.showLineNumbers`** (boolean):
  - **Description:** Show line numbers in the chat.
  - **Default:** `true`

- **`ui.showCitations`** (boolean):
  - **Description:** Show citations for generated text in the chat.
  - **Default:** `false`

- **`ui.showModelInfoInChat`** (boolean):
  - **Description:** Show the model name in the chat for each model turn.
  - **Default:** `false`

- **`ui.showUserIdentity`** (boolean):
  - **Description:** Show the signed-in user's identity (e.g. email) in the UI.
  - **Default:** `true`

- **`ui.useAlternateBuffer`** (boolean):
  - **Description:** Use an alternate screen buffer for the UI, preserving shell
    history.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`ui.useBackgroundColor`** (boolean):
  - **Description:** Whether to use background colors in the UI.
  - **Default:** `true`

- **`ui.incrementalRendering`** (boolean):
  - **Description:** Enable incremental rendering for the UI. This option will
    reduce flickering but may cause rendering artifacts. Only supported when
    useAlternateBuffer is enabled.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`ui.showSpinner`** (boolean):
  - **Description:** Show the spinner during operations.
  - **Default:** `true`

- **`ui.loadingPhrases`** (enum):
  - **Description:** What to show while the model is working: tips, witty
    comments, both, or nothing.
  - **Default:** `"tips"`
  - **Values:** `"tips"`, `"witty"`, `"all"`, `"off"`

- **`ui.errorVerbosity`** (enum):
  - **Description:** Controls whether recoverable errors are hidden (low) or
    fully shown (full).
  - **Default:** `"low"`
  - **Values:** `"low"`, `"full"`

- **`ui.customWittyPhrases`** (array):
  - **Description:** Custom witty phrases to display during loading. When
    provided, the CLI cycles through these instead of the defaults.
  - **Default:** `[]`

- **`ui.accessibility.enableLoadingPhrases`** (boolean):
  - **Description:** @deprecated Use ui.loadingPhrases instead. Enable loading
    phrases during operations.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`ui.accessibility.screenReader`** (boolean):
  - **Description:** Render output in plain-text to be more screen reader
    accessible
  - **Default:** `false`
  - **Requires restart:** Yes

#### `ide`

- **`ide.enabled`** (boolean):
  - **Description:** Enable IDE integration mode.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`ide.hasSeenNudge`** (boolean):
  - **Description:** Whether the user has seen the IDE integration nudge.
  - **Default:** `false`

#### `privacy`

- **`privacy.usageStatisticsEnabled`** (boolean):
  - **Description:** Enable collection of usage statistics
  - **Default:** `true`
  - **Requires restart:** Yes

#### `billing`

- **`billing.overageStrategy`** (enum):
  - **Description:** How to handle quota exhaustion when AI credits are
    available. 'ask' prompts each time, 'always' automatically uses credits,
    'never' disables credit usage.
  - **Default:** `"ask"`
  - **Values:** `"ask"`, `"always"`, `"never"`

#### `model`

- **`model.name`** (string):
  - **Description:** The Gemini model to use for conversations.
  - **Default:** `undefined`

- **`model.maxSessionTurns`** (number):
  - **Description:** Maximum number of user/model/tool turns to keep in a
    session. -1 means unlimited.
  - **Default:** `-1`

- **`model.summarizeToolOutput`** (object):
  - **Description:** Enables or disables summarization of tool output. Configure
    per-tool token budgets (for example {"run_shell_command": {"tokenBudget":
    2000}}). Currently only the run_shell_command tool supports summarization.
  - **Default:** `undefined`

- **`model.compressionThreshold`** (number):
  - **Description:** The fraction of context usage at which to trigger context
    compression (e.g. 0.2, 0.3).
  - **Default:** `0.5`
  - **Requires restart:** Yes

- **`model.disableLoopDetection`** (boolean):
  - **Description:** Disable automatic detection and prevention of infinite
    loops.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`model.skipNextSpeakerCheck`** (boolean):
  - **Description:** Skip the next speaker check.
  - **Default:** `true`

#### `modelConfigs`

- **`modelConfigs.aliases`** (object):
  - **Description:** Named presets for model configs. Can be used in place of a
    model name and can inherit from other aliases using an `extends` property.
  - **Default:**

    ```json
    {
      "base": {
        "modelConfig": {
          "generateContentConfig": {
            "temperature": 0,
            "topP": 1
          }
        }
      },
      "chat-base": {
        "extends": "base",
        "modelConfig": {
          "generateContentConfig": {
            "thinkingConfig": {
              "includeThoughts": true
            },
            "temperature": 1,
            "topP": 0.95,
            "topK": 64
          }
        }
      },
      "chat-base-2.5": {
        "extends": "chat-base",
        "modelConfig": {
          "generateContentConfig": {
            "thinkingConfig": {
              "thinkingBudget": 8192
            }
          }
        }
      },
      "chat-base-3": {
        "extends": "chat-base",
        "modelConfig": {
          "generateContentConfig": {
            "thinkingConfig": {
              "thinkingLevel": "HIGH"
            }
          }
        }
      },
      "gemini-3-pro-preview": {
        "extends": "chat-base-3",
        "modelConfig": {
          "model": "gemini-3-pro-preview"
        }
      },
      "gemini-3-flash-preview": {
        "extends": "chat-base-3",
        "modelConfig": {
          "model": "gemini-3-flash-preview"
        }
      },
      "gemini-2.5-pro": {
        "extends": "chat-base-2.5",
        "modelConfig": {
          "model": "gemini-2.5-pro"
        }
      },
      "gemini-2.5-flash": {
        "extends": "chat-base-2.5",
        "modelConfig": {
          "model": "gemini-2.5-flash"
        }
      },
      "gemini-2.5-flash-lite": {
        "extends": "chat-base-2.5",
        "modelConfig": {
          "model": "gemini-2.5-flash-lite"
        }
      },
      "gemini-2.5-flash-base": {
        "extends": "base",
        "modelConfig": {
          "model": "gemini-2.5-flash"
        }
      },
      "gemini-3-flash-base": {
        "extends": "base",
        "modelConfig": {
          "model": "gemini-3-flash-preview"
        }
      },
      "classifier": {
        "extends": "base",
        "modelConfig": {
          "model": "gemini-2.5-flash-lite",
          "generateContentConfig": {
            "maxOutputTokens": 1024,
            "thinkingConfig": {
              "thinkingBudget": 512
            }
          }
        }
      },
      "prompt-completion": {
        "extends": "base",
        "modelConfig": {
          "model": "gemini-2.5-flash-lite",
          "generateContentConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 16000,
            "thinkingConfig": {
              "thinkingBudget": 0
            }
          }
        }
      },
      "fast-ack-helper": {
        "extends": "base",
        "modelConfig": {
          "model": "gemini-2.5-flash-lite",
          "generateContentConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 120,
            "thinkingConfig": {
              "thinkingBudget": 0
            }
          }
        }
      },
      "edit-corrector": {
        "extends": "base",
        "modelConfig": {
          "model": "gemini-2.5-flash-lite",
          "generateContentConfig": {
            "thinkingConfig": {
              "thinkingBudget": 0
            }
          }
        }
      },
      "summarizer-default": {
        "extends": "base",
        "modelConfig": {
          "model": "gemini-2.5-flash-lite",
          "generateContentConfig": {
            "maxOutputTokens": 2000
          }
        }
      },
      "summarizer-shell": {
        "extends": "base",
        "modelConfig": {
          "model": "gemini-2.5-flash-lite",
          "generateContentConfig": {
            "maxOutputTokens": 2000
          }
        }
      },
      "web-search": {
        "extends": "gemini-3-flash-base",
        "modelConfig": {
          "generateContentConfig": {
            "tools": [
              {
                "googleSearch": {}
              }
            ]
          }
        }
      },
      "web-fetch": {
        "extends": "gemini-3-flash-base",
        "modelConfig": {
          "generateContentConfig": {
            "tools": [
              {
                "urlContext": {}
              }
            ]
          }
        }
      },
      "web-fetch-fallback": {
        "extends": "gemini-3-flash-base",
        "modelConfig": {}
      },
      "loop-detection": {
        "extends": "gemini-3-flash-base",
        "modelConfig": {}
      },
      "loop-detection-double-check": {
        "extends": "base",
        "modelConfig": {
          "model": "gemini-3-pro-preview"
        }
      },
      "llm-edit-fixer": {
        "extends": "gemini-3-flash-base",
        "modelConfig": {}
      },
      "next-speaker-checker": {
        "extends": "gemini-3-flash-base",
        "modelConfig": {}
      },
      "chat-compression-3-pro": {
        "modelConfig": {
          "model": "gemini-3-pro-preview"
        }
      },
      "chat-compression-3-flash": {
        "modelConfig": {
          "model": "gemini-3-flash-preview"
        }
      },
      "chat-compression-3.1-flash-lite": {
        "modelConfig": {
          "model": "gemini-3.1-flash-lite-preview"
        }
      },
      "chat-compression-2.5-pro": {
        "modelConfig": {
          "model": "gemini-2.5-pro"
        }
      },
      "chat-compression-2.5-flash": {
        "modelConfig": {
          "model": "gemini-2.5-flash"
        }
      },
      "chat-compression-2.5-flash-lite": {
        "modelConfig": {
          "model": "gemini-2.5-flash-lite"
        }
      },
      "chat-compression-default": {
        "modelConfig": {
          "model": "gemini-3-pro-preview"
        }
      },
      "agent-history-provider-summarizer": {
        "modelConfig": {
          "model": "gemini-3-flash-preview"
        }
      }
    }
    ```

- **`modelConfigs.customAliases`** (object):
  - **Description:** Custom named presets for model configs. These are merged
    with (and override) the built-in aliases.
  - **Default:** `{}`

- **`modelConfigs.customOverrides`** (array):
  - **Description:** Custom model config overrides. These are merged with (and
    added to) the built-in overrides.
  - **Default:** `[]`

- **`modelConfigs.overrides`** (array):
  - **Description:** Apply specific configuration overrides based on matches,
    with a primary key of model (or alias). The most specific match will be
    used.
  - **Default:** `[]`

- **`modelConfigs.modelDefinitions`** (object):
  - **Description:** Registry of model metadata, including tier, family, and
    features.
  - **Default:**

    ```json
    {
      "gemini-3.1-flash-lite-preview": {
        "tier": "flash-lite",
        "family": "gemini-3",
        "isPreview": true,
        "isVisible": true,
        "features": {
          "thinking": false,
          "multimodalToolUse": true
        }
      },
      "gemini-3.1-pro-preview": {
        "tier": "pro",
        "family": "gemini-3",
        "isPreview": true,
        "isVisible": true,
        "features": {
          "thinking": true,
          "multimodalToolUse": true
        }
      },
      "gemini-3.1-pro-preview-customtools": {
        "tier": "pro",
        "family": "gemini-3",
        "isPreview": true,
        "isVisible": false,
        "features": {
          "thinking": true,
          "multimodalToolUse": true
        }
      },
      "gemini-3-pro-preview": {
        "tier": "pro",
        "family": "gemini-3",
        "isPreview": true,
        "isVisible": true,
        "features": {
          "thinking": true,
          "multimodalToolUse": true
        }
      },
      "gemini-3-flash-preview": {
        "tier": "flash",
        "family": "gemini-3",
        "isPreview": true,
        "isVisible": true,
        "features": {
          "thinking": false,
          "multimodalToolUse": true
        }
      },
      "gemini-2.5-pro": {
        "tier": "pro",
        "family": "gemini-2.5",
        "isPreview": false,
        "isVisible": true,
        "features": {
          "thinking": false,
          "multimodalToolUse": false
        }
      },
      "gemini-2.5-flash": {
        "tier": "flash",
        "family": "gemini-2.5",
        "isPreview": false,
        "isVisible": true,
        "features": {
          "thinking": false,
          "multimodalToolUse": false
        }
      },
      "gemini-2.5-flash-lite": {
        "tier": "flash-lite",
        "family": "gemini-2.5",
        "isPreview": false,
        "isVisible": true,
        "features": {
          "thinking": false,
          "multimodalToolUse": false
        }
      },
      "auto": {
        "tier": "auto",
        "isPreview": true,
        "isVisible": false,
        "features": {
          "thinking": true,
          "multimodalToolUse": false
        }
      },
      "pro": {
        "tier": "pro",
        "isPreview": false,
        "isVisible": false,
        "features": {
          "thinking": true,
          "multimodalToolUse": false
        }
      },
      "flash": {
        "tier": "flash",
        "isPreview": false,
        "isVisible": false,
        "features": {
          "thinking": false,
          "multimodalToolUse": false
        }
      },
      "flash-lite": {
        "tier": "flash-lite",
        "isPreview": false,
        "isVisible": false,
        "features": {
          "thinking": false,
          "multimodalToolUse": false
        }
      },
      "auto-gemini-3": {
        "displayName": "Auto (Gemini 3)",
        "tier": "auto",
        "isPreview": true,
        "isVisible": true,
        "dialogDescription": "Let Gemini CLI decide the best model for the task: gemini-3-pro, gemini-3-flash",
        "features": {
          "thinking": true,
          "multimodalToolUse": false
        }
      },
      "auto-gemini-2.5": {
        "displayName": "Auto (Gemini 2.5)",
        "tier": "auto",
        "isPreview": false,
        "isVisible": true,
        "dialogDescription": "Let Gemini CLI decide the best model for the task: gemini-2.5-pro, gemini-2.5-flash",
        "features": {
          "thinking": false,
          "multimodalToolUse": false
        }
      }
    }
    ```

  - **Requires restart:** Yes

- **`modelConfigs.modelIdResolutions`** (object):
  - **Description:** Rules for resolving requested model names to concrete model
    IDs based on context.
  - **Default:**

    ```json
    {
      "gemini-3.1-pro-preview": {
        "default": "gemini-3.1-pro-preview",
        "contexts": [
          {
            "condition": {
              "hasAccessToPreview": false
            },
            "target": "gemini-2.5-pro"
          },
          {
            "condition": {
              "useCustomTools": true
            },
            "target": "gemini-3.1-pro-preview-customtools"
          }
        ]
      },
      "gemini-3.1-pro-preview-customtools": {
        "default": "gemini-3.1-pro-preview-customtools",
        "contexts": [
          {
            "condition": {
              "hasAccessToPreview": false
            },
            "target": "gemini-2.5-pro"
          }
        ]
      },
      "gemini-3-flash-preview": {
        "default": "gemini-3-flash-preview",
        "contexts": [
          {
            "condition": {
              "hasAccessToPreview": false
            },
            "target": "gemini-2.5-flash"
          }
        ]
      },
      "gemini-3-pro-preview": {
        "default": "gemini-3-pro-preview",
        "contexts": [
          {
            "condition": {
              "hasAccessToPreview": false
            },
            "target": "gemini-2.5-pro"
          },
          {
            "condition": {
              "useGemini3_1": true,
              "useCustomTools": true
            },
            "target": "gemini-3.1-pro-preview-customtools"
          },
          {
            "condition": {
              "useGemini3_1": true
            },
            "target": "gemini-3.1-pro-preview"
          }
        ]
      },
      "auto-gemini-3": {
        "default": "gemini-3-pro-preview",
        "contexts": [
          {
            "condition": {
              "hasAccessToPreview": false
            },
            "target": "gemini-2.5-pro"
          },
          {
            "condition": {
              "useGemini3_1": true,
              "useCustomTools": true
            },
            "target": "gemini-3.1-pro-preview-customtools"
          },
          {
            "condition": {
              "useGemini3_1": true
            },
            "target": "gemini-3.1-pro-preview"
          }
        ]
      },
      "auto": {
        "default": "gemini-3-pro-preview",
        "contexts": [
          {
            "condition": {
              "hasAccessToPreview": false
            },
            "target": "gemini-2.5-pro"
          },
          {
            "condition": {
              "useGemini3_1": true,
              "useCustomTools": true
            },
            "target": "gemini-3.1-pro-preview-customtools"
          },
          {
            "condition": {
              "useGemini3_1": true
            },
            "target": "gemini-3.1-pro-preview"
          }
        ]
      },
      "pro": {
        "default": "gemini-3-pro-preview",
        "contexts": [
          {
            "condition": {
              "hasAccessToPreview": false
            },
            "target": "gemini-2.5-pro"
          },
          {
            "condition": {
              "useGemini3_1": true,
              "useCustomTools": true
            },
            "target": "gemini-3.1-pro-preview-customtools"
          },
          {
            "condition": {
              "useGemini3_1": true
            },
            "target": "gemini-3.1-pro-preview"
          }
        ]
      },
      "auto-gemini-2.5": {
        "default": "gemini-2.5-pro"
      },
      "gemini-3.1-flash-lite-preview": {
        "default": "gemini-3.1-flash-lite-preview",
        "contexts": [
          {
            "condition": {
              "useGemini3_1FlashLite": false
            },
            "target": "gemini-2.5-flash-lite"
          }
        ]
      },
      "flash": {
        "default": "gemini-3-flash-preview",
        "contexts": [
          {
            "condition": {
              "hasAccessToPreview": false
            },
            "target": "gemini-2.5-flash"
          }
        ]
      },
      "flash-lite": {
        "default": "gemini-2.5-flash-lite",
        "contexts": [
          {
            "condition": {
              "useGemini3_1FlashLite": true
            },
            "target": "gemini-3.1-flash-lite-preview"
          }
        ]
      }
    }
    ```

  - **Requires restart:** Yes

- **`modelConfigs.classifierIdResolutions`** (object):
  - **Description:** Rules for resolving classifier tiers (flash, pro) to
    concrete model IDs.
  - **Default:**

    ```json
    {
      "flash": {
        "default": "gemini-3-flash-preview",
        "contexts": [
          {
            "condition": {
              "requestedModels": ["auto-gemini-2.5", "gemini-2.5-pro"]
            },
            "target": "gemini-2.5-flash"
          },
          {
            "condition": {
              "requestedModels": ["auto-gemini-3", "gemini-3-pro-preview"]
            },
            "target": "gemini-3-flash-preview"
          }
        ]
      },
      "pro": {
        "default": "gemini-3-pro-preview",
        "contexts": [
          {
            "condition": {
              "requestedModels": ["auto-gemini-2.5", "gemini-2.5-pro"]
            },
            "target": "gemini-2.5-pro"
          },
          {
            "condition": {
              "useGemini3_1": true,
              "useCustomTools": true
            },
            "target": "gemini-3.1-pro-preview-customtools"
          },
          {
            "condition": {
              "useGemini3_1": true
            },
            "target": "gemini-3.1-pro-preview"
          }
        ]
      }
    }
    ```

  - **Requires restart:** Yes

- **`modelConfigs.modelChains`** (object):
  - **Description:** Availability policy chains defining fallback behavior for
    models.
  - **Default:**

    ```json
    {
      "preview": [
        {
          "model": "gemini-3-pro-preview",
          "actions": {
            "terminal": "prompt",
            "transient": "prompt",
            "not_found": "prompt",
            "unknown": "prompt"
          },
          "stateTransitions": {
            "terminal": "terminal",
            "transient": "terminal",
            "not_found": "terminal",
            "unknown": "terminal"
          }
        },
        {
          "model": "gemini-3-flash-preview",
          "isLastResort": true,
          "actions": {
            "terminal": "prompt",
            "transient": "prompt",
            "not_found": "prompt",
            "unknown": "prompt"
          },
          "stateTransitions": {
            "terminal": "terminal",
            "transient": "terminal",
            "not_found": "terminal",
            "unknown": "terminal"
          }
        }
      ],
      "default": [
        {
          "model": "gemini-2.5-pro",
          "actions": {
            "terminal": "prompt",
            "transient": "prompt",
            "not_found": "prompt",
            "unknown": "prompt"
          },
          "stateTransitions": {
            "terminal": "terminal",
            "transient": "terminal",
            "not_found": "terminal",
            "unknown": "terminal"
          }
        },
        {
          "model": "gemini-2.5-flash",
          "isLastResort": true,
          "actions": {
            "terminal": "prompt",
            "transient": "prompt",
            "not_found": "prompt",
            "unknown": "prompt"
          },
          "stateTransitions": {
            "terminal": "terminal",
            "transient": "terminal",
            "not_found": "terminal",
            "unknown": "terminal"
          }
        }
      ],
      "lite": [
        {
          "model": "gemini-2.5-flash-lite",
          "actions": {
            "terminal": "silent",
            "transient": "silent",
            "not_found": "silent",
            "unknown": "silent"
          },
          "stateTransitions": {
            "terminal": "terminal",
            "transient": "terminal",
            "not_found": "terminal",
            "unknown": "terminal"
          }
        },
        {
          "model": "gemini-2.5-flash",
          "actions": {
            "terminal": "silent",
            "transient": "silent",
            "not_found": "silent",
            "unknown": "silent"
          },
          "stateTransitions": {
            "terminal": "terminal",
            "transient": "terminal",
            "not_found": "terminal",
            "unknown": "terminal"
          }
        },
        {
          "model": "gemini-2.5-pro",
          "isLastResort": true,
          "actions": {
            "terminal": "silent",
            "transient": "silent",
            "not_found": "silent",
            "unknown": "silent"
          },
          "stateTransitions": {
            "terminal": "terminal",
            "transient": "terminal",
            "not_found": "terminal",
            "unknown": "terminal"
          }
        }
      ]
    }
    ```

  - **Requires restart:** Yes

#### `agents`

- **`agents.overrides`** (object):
  - **Description:** Override settings for specific agents, e.g. to disable the
    agent, set a custom model config, or run config.
  - **Default:** `{}`
  - **Requires restart:** Yes

- **`agents.browser.sessionMode`** (enum):
  - **Description:** Session mode: 'persistent', 'isolated', or 'existing'.
  - **Default:** `"persistent"`
  - **Values:** `"persistent"`, `"isolated"`, `"existing"`
  - **Requires restart:** Yes

- **`agents.browser.headless`** (boolean):
  - **Description:** Run browser in headless mode.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`agents.browser.profilePath`** (string):
  - **Description:** Path to browser profile directory for session persistence.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`agents.browser.visualModel`** (string):
  - **Description:** Model override for the visual agent.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`agents.browser.allowedDomains`** (array):
  - **Description:** A list of allowed domains for the browser agent (e.g.,
    ["github.com", "*.google.com"]).
  - **Default:**

    ```json
    ["github.com", "*.google.com", "localhost"]
    ```

  - **Requires restart:** Yes

- **`agents.browser.disableUserInput`** (boolean):
  - **Description:** Disable user input on browser window during automation.
  - **Default:** `true`

- **`agents.browser.maxActionsPerTask`** (number):
  - **Description:** The maximum number of tool calls allowed per browser task.
    Enforcement is hard: the agent will be terminated when the limit is reached.
  - **Default:** `100`

- **`agents.browser.confirmSensitiveActions`** (boolean):
  - **Description:** Require manual confirmation for sensitive browser actions
    (e.g., fill_form, evaluate_script).
  - **Default:** `false`
  - **Requires restart:** Yes

- **`agents.browser.blockFileUploads`** (boolean):
  - **Description:** Hard-block file upload requests from the browser agent.
  - **Default:** `false`
  - **Requires restart:** Yes

#### `context`

- **`context.fileName`** (string | string[]):
  - **Description:** The name of the context file or files to load into memory.
    Accepts either a single string or an array of strings.
  - **Default:** `undefined`

- **`context.importFormat`** (string):
  - **Description:** The format to use when importing memory.
  - **Default:** `undefined`

- **`context.includeDirectoryTree`** (boolean):
  - **Description:** Whether to include the directory tree of the current
    working directory in the initial request to the model.
  - **Default:** `true`

- **`context.discoveryMaxDirs`** (number):
  - **Description:** Maximum number of directories to search for memory.
  - **Default:** `200`

- **`context.memoryBoundaryMarkers`** (array):
  - **Description:** File or directory names that mark the boundary for
    GEMINI.md discovery. The upward traversal stops at the first directory
    containing any of these markers. An empty array disables parent traversal.
  - **Default:**

    ```json
    [".git"]
    ```

  - **Requires restart:** Yes

- **`context.includeDirectories`** (array):
  - **Description:** Additional directories to include in the workspace context.
    Missing directories will be skipped with a warning.
  - **Default:** `[]`

- **`context.loadMemoryFromIncludeDirectories`** (boolean):
  - **Description:** Controls how /memory reload loads GEMINI.md files. When
    true, include directories are scanned; when false, only the current
    directory is used.
  - **Default:** `false`

- **`context.fileFiltering.respectGitIgnore`** (boolean):
  - **Description:** Respect .gitignore files when searching.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`context.fileFiltering.respectGeminiIgnore`** (boolean):
  - **Description:** Respect .geminiignore files when searching.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`context.fileFiltering.enableRecursiveFileSearch`** (boolean):
  - **Description:** Enable recursive file search functionality when completing
    @ references in the prompt.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`context.fileFiltering.enableFuzzySearch`** (boolean):
  - **Description:** Enable fuzzy search when searching for files.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`context.fileFiltering.customIgnoreFilePaths`** (array):
  - **Description:** Additional ignore file paths to respect. These files take
    precedence over .geminiignore and .gitignore. Files earlier in the array
    take precedence over files later in the array, e.g. the first file takes
    precedence over the second one.
  - **Default:** `[]`
  - **Requires restart:** Yes

#### `tools`

- **`tools.sandbox`** (string):
  - **Description:** Legacy full-process sandbox execution environment. Set to a
    boolean to enable or disable the sandbox, provide a string path to a sandbox
    profile, or specify an explicit sandbox command (e.g., "docker", "podman",
    "lxc", "windows-native").
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`tools.sandboxAllowedPaths`** (array):
  - **Description:** List of additional paths that the sandbox is allowed to
    access.
  - **Default:** `[]`
  - **Requires restart:** Yes

- **`tools.sandboxNetworkAccess`** (boolean):
  - **Description:** Whether the sandbox is allowed to access the network.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`tools.shell.enableInteractiveShell`** (boolean):
  - **Description:** Use node-pty for an interactive shell experience. Fallback
    to child_process still applies.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`tools.shell.backgroundCompletionBehavior`** (enum):
  - **Description:** Controls what happens when a background shell command
    finishes. 'silent' (default): quietly exits in background. 'inject':
    automatically returns output to agent. 'notify': shows brief message in
    chat.
  - **Default:** `"silent"`
  - **Values:** `"silent"`, `"inject"`, `"notify"`

- **`tools.shell.pager`** (string):
  - **Description:** The pager command to use for shell output. Defaults to
    `cat`.
  - **Default:** `"cat"`

- **`tools.shell.showColor`** (boolean):
  - **Description:** Show color in shell output.
  - **Default:** `false`

- **`tools.shell.inactivityTimeout`** (number):
  - **Description:** The maximum time in seconds allowed without output from the
    shell command. Defaults to 5 minutes.
  - **Default:** `300`

- **`tools.shell.enableShellOutputEfficiency`** (boolean):
  - **Description:** Enable shell output efficiency optimizations for better
    performance.
  - **Default:** `true`

- **`tools.core`** (array):
  - **Description:** Restrict the set of built-in tools with an allowlist. Match
    semantics mirror tools.allowed; see the built-in tools documentation for
    available names.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`tools.allowed`** (array):
  - **Description:** Tool names that bypass the confirmation dialog. Useful for
    trusted commands (for example ["run_shell_command(git)",
    "run_shell_command(npm test)"]). See shell tool command restrictions for
    matching details.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`tools.exclude`** (array):
  - **Description:** Tool names to exclude from discovery.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`tools.discoveryCommand`** (string):
  - **Description:** Command to run for tool discovery.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`tools.callCommand`** (string):
  - **Description:** Defines a custom shell command for invoking discovered
    tools. The command must take the tool name as the first argument, read JSON
    arguments from stdin, and emit JSON results on stdout.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`tools.useRipgrep`** (boolean):
  - **Description:** Use ripgrep for file content search instead of the fallback
    implementation. Provides faster search performance.
  - **Default:** `true`

- **`tools.truncateToolOutputThreshold`** (number):
  - **Description:** Maximum characters to show when truncating large tool
    outputs. Set to 0 or negative to disable truncation.
  - **Default:** `40000`
  - **Requires restart:** Yes

- **`tools.disableLLMCorrection`** (boolean):
  - **Description:** Disable LLM-based error correction for edit tools. When
    enabled, tools will fail immediately if exact string matches are not found,
    instead of attempting to self-correct.
  - **Default:** `true`
  - **Requires restart:** Yes

#### `mcp`

- **`mcp.serverCommand`** (string):
  - **Description:** Command to start an MCP server.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`mcp.allowed`** (array):
  - **Description:** A list of MCP servers to allow.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`mcp.excluded`** (array):
  - **Description:** A list of MCP servers to exclude.
  - **Default:** `undefined`
  - **Requires restart:** Yes

#### `useWriteTodos`

- **`useWriteTodos`** (boolean):
  - **Description:** Enable the write_todos tool.
  - **Default:** `true`

#### `security`

- **`security.toolSandboxing`** (boolean):
  - **Description:** Experimental tool-level sandboxing (implementation in
    progress).
  - **Default:** `false`

- **`security.disableYoloMode`** (boolean):
  - **Description:** Disable YOLO mode, even if enabled by a flag.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`security.disableAlwaysAllow`** (boolean):
  - **Description:** Disable "Always allow" options in tool confirmation
    dialogs.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`security.enablePermanentToolApproval`** (boolean):
  - **Description:** Enable the "Allow for all future sessions" option in tool
    confirmation dialogs.
  - **Default:** `false`

- **`security.autoAddToPolicyByDefault`** (boolean):
  - **Description:** When enabled, the "Allow for all future sessions" option
    becomes the default choice for low-risk tools in trusted workspaces.
  - **Default:** `false`

- **`security.blockGitExtensions`** (boolean):
  - **Description:** Blocks installing and loading extensions from Git.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`security.allowedExtensions`** (array):
  - **Description:** List of Regex patterns for allowed extensions. If nonempty,
    only extensions that match the patterns in this list are allowed. Overrides
    the blockGitExtensions setting.
  - **Default:** `[]`
  - **Requires restart:** Yes

- **`security.folderTrust.enabled`** (boolean):
  - **Description:** Setting to track whether Folder trust is enabled.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`security.environmentVariableRedaction.allowed`** (array):
  - **Description:** Environment variables to always allow (bypass redaction).
  - **Default:** `[]`
  - **Requires restart:** Yes

- **`security.environmentVariableRedaction.blocked`** (array):
  - **Description:** Environment variables to always redact.
  - **Default:** `[]`
  - **Requires restart:** Yes

- **`security.environmentVariableRedaction.enabled`** (boolean):
  - **Description:** Enable redaction of environment variables that may contain
    secrets.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`security.auth.selectedType`** (string):
  - **Description:** The currently selected authentication type.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`security.auth.enforcedType`** (string):
  - **Description:** The required auth type. If this does not match the selected
    auth type, the user will be prompted to re-authenticate.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`security.auth.useExternal`** (boolean):
  - **Description:** Whether to use an external authentication flow.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`security.enableConseca`** (boolean):
  - **Description:** Enable the context-aware security checker. This feature
    uses an LLM to dynamically generate and enforce security policies for tool
    use based on your prompt, providing an additional layer of protection
    against unintended actions.
  - **Default:** `false`
  - **Requires restart:** Yes

#### `advanced`

- **`advanced.autoConfigureMemory`** (boolean):
  - **Description:** Automatically configure Node.js memory limits
  - **Default:** `false`
  - **Requires restart:** Yes

- **`advanced.dnsResolutionOrder`** (string):
  - **Description:** The DNS resolution order.
  - **Default:** `undefined`
  - **Requires restart:** Yes

- **`advanced.excludedEnvVars`** (array):
  - **Description:** Environment variables to exclude from project context.
  - **Default:**

    ```json
    ["DEBUG", "DEBUG_MODE"]
    ```

- **`advanced.bugCommand`** (object):
  - **Description:** Configuration for the bug report command.
  - **Default:** `undefined`

#### `experimental`

- **`experimental.toolOutputMasking.enabled`** (boolean):
  - **Description:** Enables tool output masking to save tokens.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`experimental.toolOutputMasking.toolProtectionThreshold`** (number):
  - **Description:** Minimum number of tokens to protect from masking (most
    recent tool outputs).
  - **Default:** `50000`
  - **Requires restart:** Yes

- **`experimental.toolOutputMasking.minPrunableTokensThreshold`** (number):
  - **Description:** Minimum prunable tokens required to trigger a masking pass.
  - **Default:** `30000`
  - **Requires restart:** Yes

- **`experimental.toolOutputMasking.protectLatestTurn`** (boolean):
  - **Description:** Ensures the absolute latest turn is never masked,
    regardless of token count.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`experimental.enableAgents`** (boolean):
  - **Description:** Enable local and remote subagents.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`experimental.worktrees`** (boolean):
  - **Description:** Enable automated Git worktree management for parallel work.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.extensionManagement`** (boolean):
  - **Description:** Enable extension management features.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`experimental.extensionConfig`** (boolean):
  - **Description:** Enable requesting and fetching of extension settings.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`experimental.extensionRegistry`** (boolean):
  - **Description:** Enable extension registry explore UI.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.extensionRegistryURI`** (string):
  - **Description:** The URI (web URL or local file path) of the extension
    registry.
  - **Default:** `"https://geminicli.com/extensions.json"`
  - **Requires restart:** Yes

- **`experimental.extensionReloading`** (boolean):
  - **Description:** Enables extension loading/unloading within the CLI session.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.jitContext`** (boolean):
  - **Description:** Enable Just-In-Time (JIT) context loading.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`experimental.useOSC52Paste`** (boolean):
  - **Description:** Use OSC 52 for pasting. This may be more robust than the
    default system when using remote terminal sessions (if your terminal is
    configured to allow it).
  - **Default:** `false`

- **`experimental.useOSC52Copy`** (boolean):
  - **Description:** Use OSC 52 for copying. This may be more robust than the
    default system when using remote terminal sessions (if your terminal is
    configured to allow it).
  - **Default:** `false`

- **`experimental.plan`** (boolean):
  - **Description:** Enable Plan Mode.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`experimental.taskTracker`** (boolean):
  - **Description:** Enable task tracker tools.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.modelSteering`** (boolean):
  - **Description:** Enable model steering (user hints) to guide the model
    during tool execution.
  - **Default:** `false`

- **`experimental.directWebFetch`** (boolean):
  - **Description:** Enable web fetch behavior that bypasses LLM summarization.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.dynamicModelConfiguration`** (boolean):
  - **Description:** Enable dynamic model configuration (definitions,
    resolutions, and chains) via settings.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.gemmaModelRouter.enabled`** (boolean):
  - **Description:** Enable the Gemma Model Router (experimental). Requires a
    local endpoint serving Gemma via the Gemini API using LiteRT-LM shim.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.gemmaModelRouter.classifier.host`** (string):
  - **Description:** The host of the classifier.
  - **Default:** `"http://localhost:9379"`
  - **Requires restart:** Yes

- **`experimental.gemmaModelRouter.classifier.model`** (string):
  - **Description:** The model to use for the classifier. Only tested on
    `gemma3-1b-gpu-custom`.
  - **Default:** `"gemma3-1b-gpu-custom"`
  - **Requires restart:** Yes

- **`experimental.memoryManager`** (boolean):
  - **Description:** Replace the built-in save_memory tool with a memory manager
    subagent that supports adding, removing, de-duplicating, and organizing
    memories.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.agentHistoryTruncation`** (boolean):
  - **Description:** Enable truncation window logic for the Agent History
    Provider.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.agentHistoryTruncationThreshold`** (number):
  - **Description:** The maximum number of messages before history is truncated.
  - **Default:** `30`
  - **Requires restart:** Yes

- **`experimental.agentHistoryRetainedMessages`** (number):
  - **Description:** The number of recent messages to retain after truncation.
  - **Default:** `15`
  - **Requires restart:** Yes

- **`experimental.agentHistorySummarization`** (boolean):
  - **Description:** Enable summarization of truncated content via a small model
    for the Agent History Provider.
  - **Default:** `false`
  - **Requires restart:** Yes

- **`experimental.topicUpdateNarration`** (boolean):
  - **Description:** Enable the experimental Topic & Update communication model
    for reduced chattiness and structured progress reporting.
  - **Default:** `false`

#### `skills`

- **`skills.enabled`** (boolean):
  - **Description:** Enable Agent Skills.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`skills.disabled`** (array):
  - **Description:** List of disabled skills.
  - **Default:** `[]`
  - **Requires restart:** Yes

#### `hooksConfig`

- **`hooksConfig.enabled`** (boolean):
  - **Description:** Canonical toggle for the hooks system. When disabled, no
    hooks will be executed.
  - **Default:** `true`
  - **Requires restart:** Yes

- **`hooksConfig.disabled`** (array):
  - **Description:** List of hook names (commands) that should be disabled.
    Hooks in this list will not execute even if configured.
  - **Default:** `[]`

- **`hooksConfig.notifications`** (boolean):
  - **Description:** Show visual indicators when hooks are executing.
  - **Default:** `true`

#### `hooks`

- **`hooks.BeforeTool`** (array):
  - **Description:** Hooks that execute before tool execution. Can intercept,
    validate, or modify tool calls.
  - **Default:** `[]`

- **`hooks.AfterTool`** (array):
  - **Description:** Hooks that execute after tool execution. Can process
    results, log outputs, or trigger follow-up actions.
  - **Default:** `[]`

- **`hooks.BeforeAgent`** (array):
  - **Description:** Hooks that execute before agent loop starts. Can set up
    context or initialize resources.
  - **Default:** `[]`

- **`hooks.AfterAgent`** (array):
  - **Description:** Hooks that execute after agent loop completes. Can perform
    cleanup or summarize results.
  - **Default:** `[]`

- **`hooks.Notification`** (array):
  - **Description:** Hooks that execute on notification events (errors,
    warnings, info). Can log or alert on specific conditions.
  - **Default:** `[]`

- **`hooks.SessionStart`** (array):
  - **Description:** Hooks that execute when a session starts. Can initialize
    session-specific resources or state.
  - **Default:** `[]`

- **`hooks.SessionEnd`** (array):
  - **Description:** Hooks that execute when a session ends. Can perform cleanup
    or persist session data.
  - **Default:** `[]`

- **`hooks.PreCompress`** (array):
  - **Description:** Hooks that execute before chat history compression. Can
    back up or analyze conversation before compression.
  - **Default:** `[]`

- **`hooks.BeforeModel`** (array):
  - **Description:** Hooks that execute before LLM requests. Can modify prompts,
    inject context, or control model parameters.
  - **Default:** `[]`

- **`hooks.AfterModel`** (array):
  - **Description:** Hooks that execute after LLM responses. Can process
    outputs, extract information, or log interactions.
  - **Default:** `[]`

- **`hooks.BeforeToolSelection`** (array):
  - **Description:** Hooks that execute before tool selection. Can filter or
    prioritize available tools dynamically.
  - **Default:** `[]`

#### `admin`

- **`admin.secureModeEnabled`** (boolean):
  - **Description:** If true, disallows YOLO mode and "Always allow" options
    from being used.
  - **Default:** `false`

- **`admin.extensions.enabled`** (boolean):
  - **Description:** If false, disallows extensions from being installed or
    used.
  - **Default:** `true`

- **`admin.mcp.enabled`** (boolean):
  - **Description:** If false, disallows MCP servers from being used.
  - **Default:** `true`

- **`admin.mcp.config`** (object):
  - **Description:** Admin-configured MCP servers (allowlist).
  - **Default:** `{}`

- **`admin.mcp.requiredConfig`** (object):
  - **Description:** Admin-required MCP servers that are always injected.
  - **Default:** `{}`

- **`admin.skills.enabled`** (boolean):
  - **Description:** If false, disallows agent skills from being used.
  - **Default:** `true`
  <!-- SETTINGS-AUTOGEN:END -->

#### `mcpServers`

Configures connections to one or more Model-Context Protocol (MCP) servers for
discovering and using custom tools. Gemini CLI attempts to connect to each
configured MCP server to discover available tools. Every discovered tool is
prepended with the `mcp_` prefix and its server alias to form a fully qualified
name (FQN) (e.g., `mcp_serverAlias_actualToolName`) to avoid conflicts. Note
that the system might strip certain schema properties from MCP tool definitions
for compatibility. At least one of `command`, `url`, or `httpUrl` must be
provided. If multiple are specified, the order of precedence is `httpUrl`, then
`url`, then `command`.

<!-- prettier-ignore -->
> [!WARNING]
> Avoid using underscores (`_`) in your server aliases (e.g., use
> `my-server` instead of `my_server`). The underlying policy engine parses Fully
> Qualified Names (`mcp_server_tool`) using the first underscore after the
> `mcp_` prefix. An underscore in your server alias will cause the parser to
> misidentify the server name, which can cause security policies to fail
> silently.

- **`mcpServers.<SERVER_NAME>`** (object): The server parameters for the named
  server.
  - `command` (string, optional): The command to execute to start the MCP server
    via standard I/O.
  - `args` (array of strings, optional): Arguments to pass to the command.
  - `env` (object, optional): Environment variables to set for the server
    process.
  - `cwd` (string, optional): The working directory in which to start the
    server.
  - `url` (string, optional): The URL of an MCP server that uses Server-Sent
    Events (SSE) for communication.
  - `httpUrl` (string, optional): The URL of an MCP server that uses streamable
    HTTP for communication.
  - `headers` (object, optional): A map of HTTP headers to send with requests to
    `url` or `httpUrl`.
  - `timeout` (number, optional): Timeout in milliseconds for requests to this
    MCP server.
  - `trust` (boolean, optional): Trust this server and bypass all tool call
    confirmations.
  - `description` (string, optional): A brief description of the server, which
    may be used for display purposes.
  - `includeTools` (array of strings, optional): List of tool names to include
    from this MCP server. When specified, only the tools listed here will be
    available from this server (allowlist behavior). If not specified, all tools
    from the server are enabled by default.
  - `excludeTools` (array of strings, optional): List of tool names to exclude
    from this MCP server. Tools listed here will not be available to the model,
    even if they are exposed by the server. **Note:** `excludeTools` takes
    precedence over `includeTools` - if a tool is in both lists, it will be
    excluded.

#### `telemetry`

Configures logging and metrics collection for Gemini CLI. For more information,
see [Telemetry](/docs/cli/telemetry).

- **Properties:**
  - **`enabled`** (boolean): Whether or not telemetry is enabled.
  - **`target`** (string): The destination for collected telemetry. Supported
    values are `local` and `gcp`.
  - **`otlpEndpoint`** (string): The endpoint for the OTLP Exporter.
  - **`otlpProtocol`** (string): The protocol for the OTLP Exporter (`grpc` or
    `http`).
  - **`logPrompts`** (boolean): Whether or not to include the content of user
    prompts in the logs.
  - **`outfile`** (string): The file to write telemetry to when `target` is
    `local`.
  - **`useCollector`** (boolean): Whether to use an external OTLP collector.