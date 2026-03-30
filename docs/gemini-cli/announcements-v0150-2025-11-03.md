## Announcements: v0.15.0 - 2025-11-03

- **🎉 Seamless scrollable UI and mouse support:** We’ve given Gemini CLI a
  major facelift to make your terminal experience smoother and much more
  polished. You now get a flicker-free display with sticky headers that keep
  important context visible and a stable input prompt that doesn't jump around.
  We even added mouse support so you can click right where you need to type!
  ([gif](https://imgur.com/a/O6qc7bx),
  [@jacob314](https://github.com/jacob314)).
  - **Announcement:**
    [https://developers.googleblog.com/en/making-the-terminal-beautiful-one-pixel-at-a-time/](https://developers.googleblog.com/en/making-the-terminal-beautiful-one-pixel-at-a-time/)
- **🎉 New partner extensions:**
  - **Arize:** Seamlessly instrument AI applications with Arize AX and grant
    direct access to Arize support:

    `gemini extensions install https://github.com/Arize-ai/arize-tracing-assistant`

  - **Chronosphere:** Retrieve logs, metrics, traces, events, and specific
    entities:

    `gemini extensions install https://github.com/chronosphereio/chronosphere-mcp`

  - **Transmit:** Comprehensive context, validation, and automated fixes for
    creating production-ready authentication and identity workflows:

    `gemini extensions install https://github.com/TransmitSecurity/transmit-security-journey-builder`

- **Todo planning:** Complex questions now get broken down into todo lists that
  the model can manage and check off. ([gif](https://imgur.com/a/EGDfNlZ),
  [pr](https://github.com/google-gemini/gemini-cli/pull/12905) by
  [@anj-s](https://github.com/anj-s))
- **Disable GitHub extensions:** Users can now prevent the installation and
  loading of extensions from GitHub.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/12838) by
  [@kevinjwang1](https://github.com/kevinjwang1)).
- **Extensions restart:** Users can now explicitly restart extensions using the
  `/extensions restart` command.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/12739) by
  [@jakemac53](https://github.com/jakemac53)).
- **Better Angular support:** Angular workflows should now be more seamless
  ([pr](https://github.com/google-gemini/gemini-cli/pull/10252) by
  [@MarkTechson](https://github.com/MarkTechson)).
- **Validate command:** Users can now check that local extensions are formatted
  correctly. ([pr](https://github.com/google-gemini/gemini-cli/pull/12186) by
  [@kevinjwang1](https://github.com/kevinjwang1)).