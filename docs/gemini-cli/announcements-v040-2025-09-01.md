## Announcements: v0.4.0 - 2025-09-01

- 🎉**Gemini CLI CloudRun and Security Integrations**🎉: Automate app deployment
  and security analysis with CloudRun and Security extension integrations. Once
  installed deploy your app to the cloud with `/deploy` and find and fix
  security vulnerabilities with `/security:analyze`.
  - Announcement and how to get started:
    [https://cloud.google.com/blog/products/ai-machine-learning/automate-app-deployment-and-security-analysis-with-new-gemini-cli-extensions](https://cloud.google.com/blog/products/ai-machine-learning/automate-app-deployment-and-security-analysis-with-new-gemini-cli-extensions)
- **Experimental**
  - **Edit Tool:** Give our new edit tool a try by setting
    `"useSmartEdit": true` in `settings.json`!
    ([feedback](https://github.com/google-gemini/gemini-cli/discussions/7758),
    [pr](https://github.com/google-gemini/gemini-cli/pull/6823) by
    [@silviojr](https://github.com/silviojr))
  - **Model talking to itself fix:** We’ve removed a model workaround that would
    encourage Gemini CLI to continue conversations on your behalf. This may be
    disruptive and can be disabled via `"skipNextSpeakerCheck": false` in your
    `settings.json`
    ([feedback](https://github.com/google-gemini/gemini-cli/discussions/6666),
    [pr](https://github.com/google-gemini/gemini-cli/pull/7614) by
    [@SandyTao520](https://github.com/SandyTao520))
  - **Prompt completion:** Get real-time AI suggestions to complete your prompts
    as you type. Enable it with `"general": { "enablePromptCompletion": true }`
    and share your feedback!
    ([gif](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*hvegW7YXOg6N_beUWhTdxA.gif),
    [pr](https://github.com/google-gemini/gemini-cli/pull/4691) by
    [@3ks](https://github.com/3ks))
- **Footer visibility configuration:** Customize the CLI's footer look and feel
  in `settings.json`
  ([pr](https://github.com/google-gemini/gemini-cli/pull/7419) by
  [@miguelsolorio](https://github.com/miguelsolorio))
  - `hideCWD`: hide current working directory.
  - `hideSandboxStatus`: hide sandbox status.
  - `hideModelInfo`: hide current model information.
  - `hideContextSummary`: hide request context summary.
- **Citations:** For enterprise Code Assist licenses users will now see
  citations in their responses by default. Enable this yourself with
  `"showCitations": true`
  ([pr](https://github.com/google-gemini/gemini-cli/pull/7350) by
  [@scidomino](https://github.com/scidomino))
- **Pro Quota Dialog:** Handle daily Pro model usage limits with an interactive
  dialog that lets you immediately switch auth or fallback.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/7094) by
  [@JayadityaGit](https://github.com/JayadityaGit))
- **Custom commands @:** Embed local file or directory content directly into
  your custom command prompts using `@{path}` syntax
  ([gif](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*GosBAo2SjMfFffAnzT7ZMg.gif),
  [pr](https://github.com/google-gemini/gemini-cli/pull/6716) by
  [@abhipatel12](https://github.com/abhipatel12))
- **2.5 Flash Lite support:** You can now use the `gemini-2.5-flash-lite` model
  for Gemini CLI via `gemini -m …`.
  ([gif](https://miro.medium.com/v2/resize:fit:2000/format:webp/1*P4SKwnrsyBuULoHrFqsFKQ.gif),
  [pr](https://github.com/google-gemini/gemini-cli/pull/4652) by
  [@psinha40898](https://github.com/psinha40898))
- **CLI streamlining:** We have deprecated a number of command line arguments in
  favor of `settings.json` alternatives. We will remove these arguments in a
  future release. See the PR for the full list of deprecations.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/7360) by
  [@allenhutchison](https://github.com/allenhutchison))
- **JSON session summary:** Track and save detailed CLI session statistics to a
  JSON file for performance analysis with `--session-summary <path>`
  ([pr](https://github.com/google-gemini/gemini-cli/pull/7347) by
  [@leehagoodjames](https://github.com/leehagoodjames))
- **Robust keyboard handling:** More reliable and consistent behavior for arrow
  keys, special keys (Home, End, etc.), and modifier combinations across various
  terminals. ([pr](https://github.com/google-gemini/gemini-cli/pull/7118) by
  [@deepankarsharma](https://github.com/deepankarsharma))
- **MCP loading indicator:** Provides visual feedback during CLI initialization
  when connecting to multiple servers.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/6923) by
  [@swissspidy](https://github.com/swissspidy))
- **Small features, polish, reliability & bug fixes:** A large amount of
  changes, smaller features, UI updates, reliability and bug fixes + general
  polish made it in this week!