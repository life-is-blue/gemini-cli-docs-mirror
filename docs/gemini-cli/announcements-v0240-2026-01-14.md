## Announcements: v0.24.0 - 2026-01-14

- **Agent Skills:** We've introduced significant advancements in Agent Skills.
  This includes initial documentation and tutorials to help you get started,
  alongside enhanced support for remote agents, allowing for more distributed
  and powerful automation within Gemini CLI.
  ([#15869](https://github.com/google-gemini/gemini-cli/pull/15869) by
  [@NTaylorMullen](https://github.com/NTaylorMullen)),
  ([#16013](https://github.com/google-gemini/gemini-cli/pull/16013) by
  [@adamweidman](https://github.com/adamweidman))
- **Improved UI/UX:** The user interface has received several updates, featuring
  visual indicators for hook execution, a more refined display for settings, and
  the ability to use the Tab key to effortlessly switch focus between the shell
  and input areas.
  ([#15408](https://github.com/google-gemini/gemini-cli/pull/15408) by
  [@abhipatel12](https://github.com/abhipatel12)),
  ([#14332](https://github.com/google-gemini/gemini-cli/pull/14332) by
  [@galz10](https://github.com/galz10))
- **Enhanced Security:** Security has been a major focus, with default folder
  trust now set to untrusted for increased safety. The Policy Engine has been
  improved to allow specific modes in user and administrator policies, and
  granular allowlisting for shell commands has been implemented, providing finer
  control over tool execution.
  ([#15943](https://github.com/google-gemini/gemini-cli/pull/15943) by
  [@galz10](https://github.com/galz10)),
  ([#15977](https://github.com/google-gemini/gemini-cli/pull/15977) by
  [@NTaylorMullen](https://github.com/NTaylorMullen))
- **Core Functionality:** This release includes a mandatory MessageBus
  injection, marking Phase 3 of a hard migration to a more robust internal
  communication system. We've also added support for built-in skills with the
  CLI itself, and enhanced model routing to effectively utilize subagents.
  ([#15776](https://github.com/google-gemini/gemini-cli/pull/15776) by
  [@abhipatel12](https://github.com/abhipatel12)),
  ([#16300](https://github.com/google-gemini/gemini-cli/pull/16300) by
  [@NTaylorMullen](https://github.com/NTaylorMullen))
- **Terminal Features:** Terminal interactions are more seamless with new
  features like OSC 52 paste support, along with fixes for Windows clipboard
  paste issues and general improvements to pasting in Windows terminals.
  ([#15336](https://github.com/google-gemini/gemini-cli/pull/15336) by
  [@scidomino](https://github.com/scidomino)),
  ([#15932](https://github.com/google-gemini/gemini-cli/pull/15932) by
  [@scidomino](https://github.com/scidomino))
- **New Commands:** To manage the new features, we've added several new
  commands: `/agents refresh` to update agent configurations, `/skills reload`
  to refresh skill definitions, and `/skills install/uninstall` for easier
  management of your Agent Skills.
  ([#16204](https://github.com/google-gemini/gemini-cli/pull/16204) by
  [@NTaylorMullen](https://github.com/NTaylorMullen)),
  ([#15865](https://github.com/google-gemini/gemini-cli/pull/15865) by
  [@NTaylorMullen](https://github.com/NTaylorMullen)),
  ([#16377](https://github.com/google-gemini/gemini-cli/pull/16377) by
  [@NTaylorMullen](https://github.com/NTaylorMullen))