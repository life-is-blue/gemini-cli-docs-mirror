## Announcements: v0.7.0 - 2025-09-22

- 🎉**Build your own Gemini CLI IDE plugin:** We've published a spec for
  creating IDE plugins to enable rich context-aware experiences and native
  in-editor diffing in your IDE of choice.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/8479) by
  [@skeshive](https://github.com/skeshive))
- 🎉 **Gemini CLI extensions**
  - **Flutter:** An early version to help you create, build, test, and run
    Flutter apps with Gemini CLI
    ([extension](https://github.com/gemini-cli-extensions/flutter))
  - **nanobanana:** Integrate nanobanana into Gemini CLI
    ([extension](https://github.com/gemini-cli-extensions/nanobanana))
- **Telemetry config via environment:** Manage telemetry settings using
  environment variables for a more flexible setup.
  ([docs](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/telemetry.md#configuration),
  [pr](https://github.com/google-gemini/gemini-cli/pull/9113) by
  [@jerop](https://github.com/jerop))
- **​​Experimental todos:** Track and display progress on complex tasks with a
  managed checklist. Off by default but can be enabled via
  `"useWriteTodos": true`
  ([pr](https://github.com/google-gemini/gemini-cli/pull/8761) by
  [@anj-s](https://github.com/anj-s))
- **Share chat support for tools:** Using `/chat share` will now also render
  function calls and responses in the final markdown file.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/8693) by
  [@rramkumar1](https://github.com/rramkumar1))
- **Citations:** Now enabled for all users
  ([pr](https://github.com/google-gemini/gemini-cli/pull/8570) by
  [@scidomino](https://github.com/scidomino))
- **Custom commands in Headless Mode:** Run custom slash commands directly from
  the command line in non-interactive mode: `gemini "/joke Chuck Norris"`
  ([pr](https://github.com/google-gemini/gemini-cli/pull/8305) by
  [@capachino](https://github.com/capachino))
- **Small features, polish, reliability & bug fixes:** A large amount of
  changes, smaller features, UI updates, reliability and bug fixes + general
  polish made it in this week!