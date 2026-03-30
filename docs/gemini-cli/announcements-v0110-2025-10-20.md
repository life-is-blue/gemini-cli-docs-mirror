## Announcements: v0.11.0 - 2025-10-20

![Gemini CLI and Jules](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Jules_Extension_-_Blog_Header_O346JNt.original.png)

- 🎉 **Gemini CLI Jules Extension:** Use Gemini CLI to orchestrate Jules. Spawn
  remote workers, delegate tedious tasks, or check in on running jobs!
  - Install:
    `gemini extensions install https://github.com/gemini-cli-extensions/jules`
  - Announcement:
    [https://developers.googleblog.com/en/introducing-the-jules-extension-for-gemini-cli/](https://developers.googleblog.com/en/introducing-the-jules-extension-for-gemini-cli/)
- **Stream JSON output:** Stream real-time JSONL events with
  `--output-format stream-json` to monitor AI agent progress when run
  headlessly. ([gif](https://imgur.com/a/0UCE81X),
  [pr](https://github.com/google-gemini/gemini-cli/pull/10883) by
  [@anj-s](https://github.com/anj-s))
- **Markdown toggle:** Users can now switch between rendered and raw markdown
  display using `alt+m `or` ctrl+m`. ([gif](https://imgur.com/a/lDNdLqr),
  [pr](https://github.com/google-gemini/gemini-cli/pull/10383) by
  [@srivatsj](https://github.com/srivatsj))
- **Queued message editing:** Users can now quickly edit queued messages by
  pressing the up arrow key when the input is empty.
  ([gif](https://imgur.com/a/ioRslLd),
  [pr](https://github.com/google-gemini/gemini-cli/pull/10392) by
  [@akhil29](https://github.com/akhil29))
- **JSON web fetch**: Non-HTML content like JSON APIs or raw source code are now
  properly shown to the model (previously only supported HTML)
  ([gif](https://imgur.com/a/Q58U4qJ),
  [pr](https://github.com/google-gemini/gemini-cli/pull/11284) by
  [@abhipatel12](https://github.com/abhipatel12))
- **Non-interactive MCP commands:** Users can now run MCP slash commands in
  non-interactive mode `gemini "/some-mcp-prompt"`.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/10194) by
  [@capachino](https://github.com/capachino))
- **Removal of deprecated flags:** We’ve finally removed a number of deprecated
  flags to cleanup Gemini CLI’s invocation profile:
  - `--all-files` / `-a` in favor of `@` from within Gemini CLI.
    ([pr](https://github.com/google-gemini/gemini-cli/pull/11228) by
    [@allenhutchison](https://github.com/allenhutchison))
  - `--telemetry-*` flags in favor of
    [environment variables](https://github.com/google-gemini/gemini-cli/pull/11318)
    ([pr](https://github.com/google-gemini/gemini-cli/pull/11318) by
    [@allenhutchison](https://github.com/allenhutchison))