## Announcements: v0.21.0 - 2025-12-15

- **⚡️⚡️⚡️ Gemini 3 Flash + Gemini CLI:** Better, faster and cheaper than 2.5
  Pro - and in some scenarios better than 3 Pro! For paid tiers + free tier
  users who were on the wait list enable **Preview Features** in `/settings.`
- For more information:
  [Gemini 3 Flash is now available in Gemini CLI](https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/).
- 🎉 Gemini CLI Extensions:
  - Rill: Utilize natural language to analyze Rill data, enabling the
    exploration of metrics and trends without the need for manual queries.
    `gemini extensions install https://github.com/rilldata/rill-gemini-extension`
  - Browserbase: Interact with web pages, take screenshots, extract information,
    and perform automated actions with atomic precision.
    `gemini extensions install https://github.com/browserbase/mcp-server-browserbase`
- Quota Visibility: The `/stats` command now displays quota information for all
  available models, including those not used in the current session. (@sehoon38)
- Fuzzy Setting Search: Users can now quickly find settings using fuzzy search
  within the settings dialog. (@sehoon38)
- MCP Resource Support: Users can now discover, view, and search through
  resources using the @ command. (@MrLesk)
- Auto-execute Simple Slash Commands: Simple slash commands are now executed
  immediately on enter. (@jackwotherspoon)