### Enter Plan Mode manually

To start Plan Mode while using Gemini CLI:

- **Keyboard shortcut:** Press `Shift+Tab` to cycle through approval modes
  (`Default` -> `Auto-Edit` -> `Plan`). Plan Mode is automatically removed from
  the rotation when Gemini CLI is actively processing or showing confirmation
  dialogs.

- **Command:** Type `/plan` in the input box.

- **Natural Language:** Ask Gemini CLI to "start a plan for...". Gemini CLI
  calls the
  [`enter_plan_mode`](/docs/tools/planning#1-enter_plan_mode-enterplanmode) tool
  to switch modes. This tool is not available when Gemini CLI is in
  [YOLO mode](/docs/reference/configuration#command-line-arguments).