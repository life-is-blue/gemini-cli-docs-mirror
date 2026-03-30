## Additional context-specific shortcuts

- `Option+B/F/M` (macOS only): Are interpreted as `Cmd+B/F/M` even if your
  terminal isn't configured to send Meta with Option.
- `!` on an empty prompt: Enter or exit shell mode.
- `?` on an empty prompt: Toggle the shortcuts panel above the input. Press
  `Esc`, `Backspace`, any printable key, or a registered app hotkey to close it.
  The panel also auto-hides while the agent is running/streaming or when
  action-required dialogs are shown. Press `?` again to close the panel and
  insert a `?` into the prompt.
- `Tab` + `Tab` (while typing in the prompt): Toggle between minimal and full UI
  details when no completion/search interaction is active. The selected mode is
  remembered for future sessions. Full UI remains the default on first run, and
  single `Tab` keeps its existing completion/focus behavior.
- `Shift + Tab` (while typing in the prompt): Cycle approval modes: default,
  auto-edit, and plan (skipped when agent is busy).
- `\` (at end of a line) + `Enter`: Insert a newline without leaving single-line
  mode.
- `Esc` pressed twice quickly: Clear the input prompt if it is not empty,
  otherwise browse and rewind previous interactions.
- `Up Arrow` / `Down Arrow`: When the cursor is at the top or bottom of a
  single-line input, navigate backward or forward through prompt history.
- `Number keys (1-9, multi-digit)` inside selection dialogs: Jump directly to
  the numbered radio option and confirm when the full number is entered.
- `Ctrl + O`: Expand or collapse paste placeholders (`[Pasted Text: X lines]`)
  inline when the cursor is over the placeholder.
- `Ctrl + X` (while a plan is presented): Open the plan in an external editor to
  [collaboratively edit or comment](/docs/cli/plan-mode#collaborative-plan-editing)
  on the implementation strategy.
- `Double-click` on a paste placeholder (alternate buffer mode only): Expand to
  view full content inline. Double-click again to collapse.