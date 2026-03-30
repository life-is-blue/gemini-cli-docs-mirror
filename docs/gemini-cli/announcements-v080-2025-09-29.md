## Announcements: v0.8.0 - 2025-09-29

- 🎉 **Announcing Gemini CLI Extensions** 🎉
  - Completely customize your Gemini CLI experience to fit your workflow.
  - Build and share your own Gemini CLI extensions with the world.
  - Launching with a growing catalog of community, partner, and Google-built
    extensions.
    - Check extensions from
      [key launch partners](https://github.com/google-gemini/gemini-cli/discussions/10718).
  - Easy install:
    - `gemini extensions install <github url|folder path>`
  - Easy management:
    - `gemini extensions install|uninstall|link`
    - `gemini extensions enable|disable`
    - `gemini extensions list|update|new`
  - Or use commands while running with `/extensions list|update`.
  - Everything you need to know:
    [Now open for building: Introducing Gemini CLI extensions](https://blog.google/technology/developers/gemini-cli-extensions/).
- 🎉 **Our New Home Page & Better Documentation** 🎉
  - Check out our new home page for better getting started material, reference
    documentation, extensions and more!
  - _Homepage:_ [https://geminicli.com](https://geminicli.com)
  - ‼️*NEW documentation:*
    [https://geminicli.com/docs](https://geminicli.com/docs) (Have any
    [suggestions](https://github.com/google-gemini/gemini-cli/discussions/8722)?)
  - _Extensions:_
    [https://geminicli.com/extensions](https://geminicli.com/extensions)
- **Non-Interactive Allowed Tools:** `--allowed-tools` will now also work in
  non-interactive mode.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/9114) by
  [@mistergarrison](https://github.com/mistergarrison))
- **Terminal Title Status:** See the CLI's real-time status and thoughts
  directly in the terminal window's title by setting `showStatusInTitle: true`.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/4386) by
  [@Fridayxiao](https://github.com/Fridayxiao))
- **Small features, polish, reliability & bug fixes:** A large amount of
  changes, smaller features, UI updates, reliability and bug fixes + general
  polish made it in this week!