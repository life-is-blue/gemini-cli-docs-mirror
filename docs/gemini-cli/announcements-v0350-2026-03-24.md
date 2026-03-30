## Announcements: v0.35.0 - 2026-03-24

- **Customizable Keyboard Shortcuts:** Users can now customize their keyboard
  shortcuts, including support for literal character keybindings and the
  extended Kitty protocol
  ([#21945](https://github.com/google-gemini/gemini-cli/pull/21945),
  [#21972](https://github.com/google-gemini/gemini-cli/pull/21972) by
  @scidomino).
- **Vim Mode Improvements:** Added missing motions (X, ~, r, f/F/t/T) and
  yank/paste support with the unnamed register
  ([#21932](https://github.com/google-gemini/gemini-cli/pull/21932),
  [#22026](https://github.com/google-gemini/gemini-cli/pull/22026) by @aanari).
- **Tool Isolation and Sandboxing:** Introduced `SandboxManager` to isolate
  process-spawning tools and added Linux bubblewrap/seccomp sandboxing support
  ([#21774](https://github.com/google-gemini/gemini-cli/pull/21774),
  [#22231](https://github.com/google-gemini/gemini-cli/pull/22231) by @galz10,
  [#22680](https://github.com/google-gemini/gemini-cli/pull/22680) by
  @DavidAPierce).
- **JIT Context Discovery:** Implemented Just-In-Time context discovery for file
  system tools to improve model performance and accuracy
  ([#22082](https://github.com/google-gemini/gemini-cli/pull/22082),
  [#22736](https://github.com/google-gemini/gemini-cli/pull/22736) by
  @SandyTao520).