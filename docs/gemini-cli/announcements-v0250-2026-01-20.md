## Announcements: v0.25.0 - 2026-01-20

- **Skills and Agents Improvements:** We've enhanced the `activate_skill` tool,
  added a new `pr-creator` skill
  ([#16232](https://github.com/google-gemini/gemini-cli/pull/16232) by
  [@NTaylorMullen](https://github.com/NTaylorMullen)), enabled skills by
  default, improved the `cli_help` agent
  ([#16100](https://github.com/google-gemini/gemini-cli/pull/16100) by
  [@scidomino](https://github.com/scidomino)), and added a new `/agents refresh`
  command ([#16204](https://github.com/google-gemini/gemini-cli/pull/16204) by
  [@joshualitt](https://github.com/joshualitt)).
- **UI/UX Refinements:** You'll notice more transparent feedback for skills
  ([#15954](https://github.com/google-gemini/gemini-cli/pull/15954) by
  [@NTaylorMullen](https://github.com/NTaylorMullen)), the ability to switch
  focus between the shell and input with Tab
  ([#14332](https://github.com/google-gemini/gemini-cli/pull/14332) by
  [@jacob314](https://github.com/jacob314)), and dynamic terminal tab titles
  ([#16378](https://github.com/google-gemini/gemini-cli/pull/16378) by
  [@NTaylorMullen](https://github.com/NTaylorMullen)).
- **Core Functionality & Performance:** This release includes support for
  built-in agent skills
  ([#16045](https://github.com/google-gemini/gemini-cli/pull/16045) by
  [@NTaylorMullen](https://github.com/NTaylorMullen)), refined Gemini 3 system
  instructions ([#16139](https://github.com/google-gemini/gemini-cli/pull/16139)
  by [@NTaylorMullen](https://github.com/NTaylorMullen)), caching for ignore
  instances to improve performance
  ([#16185](https://github.com/google-gemini/gemini-cli/pull/16185) by
  [@EricRahm](https://github.com/EricRahm)), and enhanced retry mechanisms
  ([#16489](https://github.com/google-gemini/gemini-cli/pull/16489) by
  [@sehoon38](https://github.com/sehoon38)).
- **Bug Fixes and Stability:** We've squashed numerous bugs across the CLI,
  core, and workflows, addressing issues with subagent delegation, unicode
  character crashes, and sticky header regressions.