## Announcements: v0.30.0 - 2026-02-25

- **SDK & Custom Skills:** Introduced the initial SDK package, enabling dynamic
  system instructions, `SessionContext` for SDK tool calls, and support for
  custom skills
  ([#18861](https://github.com/google-gemini/gemini-cli/pull/18861) by
  @mbleigh).
- **Policy Engine Enhancements:** Added a new `--policy` flag for user-defined
  policies, introduced strict seatbelt profiles, and deprecated
  `--allowed-tools` in favor of the policy engine
  ([#18500](https://github.com/google-gemini/gemini-cli/pull/18500) by
  @allenhutchison).
- **UI & Themes:** Added a generic searchable list for settings and extensions,
  new Solarized themes, text wrapping for markdown tables, and a clean UI toggle
  prototype ([#19064](https://github.com/google-gemini/gemini-cli/pull/19064) by
  @rmedranollamas).
- **Vim & Terminal Interaction:** Improved Vim support to feel more complete and
  added support for Ctrl-Z terminal suspension
  ([#18755](https://github.com/google-gemini/gemini-cli/pull/18755) by
  @ppgranger, [#18931](https://github.com/google-gemini/gemini-cli/pull/18931)
  by @scidomino).