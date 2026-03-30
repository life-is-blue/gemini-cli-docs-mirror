## Announcements: v0.5.0 - 2025-09-08

- 🎉**FastMCP + Gemini CLI**🎉: Quickly install and manage your Gemini CLI MCP
  servers with FastMCP ([video](https://imgur.com/a/m8QdCPh),
  [pr](https://github.com/jlowin/fastmcp/pull/1709) by
  [@jackwotherspoon](https://github.com/jackwotherspoon)**)**
  - Getting started:
    [https://gofastmcp.com/integrations/gemini-cli](https://gofastmcp.com/integrations/gemini-cli)
- **Positional Prompt for Non-Interactive:** Seamlessly invoke Gemini CLI
  headlessly via `gemini "Hello"`. Synonymous with passing `-p`.
  ([gif](https://imgur.com/a/hcBznpB),
  [pr](https://github.com/google-gemini/gemini-cli/pull/7668) by
  [@allenhutchison](https://github.com/allenhutchison))
- **Experimental Tool output truncation:** Enable truncating shell tool outputs
  and saving full output to a file by setting
  `"enableToolOutputTruncation": true `([pr](https://github.com/google-gemini/gemini-cli/pull/8039)
  by [@SandyTao520](https://github.com/SandyTao520))
- **Edit Tool improvements:** Gemini CLI’s ability to edit files should now be
  far more capable. ([pr](https://github.com/google-gemini/gemini-cli/pull/7679)
  by [@silviojr](https://github.com/silviojr))
- **Custom witty messages:** The feature you’ve all been waiting for…
  Personalized witty loading messages via
  `"ui": { "customWittyPhrases": ["YOLO"]}` in `settings.json`.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/7641) by
  [@JayadityaGit](https://github.com/JayadityaGit))
- **Nested .gitignore File Handling:** Nested `.gitignore` files are now
  respected. ([pr](https://github.com/google-gemini/gemini-cli/pull/7645) by
  [@gsquared94](https://github.com/gsquared94))
- **Enforced authentication:** System administrators can now mandate a specific
  authentication method via
  `"enforcedAuthType": "oauth-personal|gemini-api-key|…"`in `settings.json`.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/6564) by
  [@chrstnb](https://github.com/chrstnb))
- **A2A development-tool extension:** An RFC for an Agent2Agent
  ([A2A](https://a2a-protocol.org/latest/)) powered extension for developer tool
  use cases.
  ([feedback](https://github.com/google-gemini/gemini-cli/discussions/7822),
  [pr](https://github.com/google-gemini/gemini-cli/pull/7817) by
  [@skeshive](https://github.com/skeshive))
- **Hands on Codelab:
  **[https://codelabs.developers.google.com/gemini-cli-hands-on](https://codelabs.developers.google.com/gemini-cli-hands-on)
- **Small features, polish, reliability & bug fixes:** A large amount of
  changes, smaller features, UI updates, reliability and bug fixes + general
  polish made it in this week!