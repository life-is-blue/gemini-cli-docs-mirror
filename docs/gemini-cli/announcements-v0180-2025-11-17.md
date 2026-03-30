## Announcements: v0.18.0 - 2025-11-17

- 🎉 **New extensions:**
  - **Google Workspace**: Integrate Gemini CLI with your Workspace data. Write
    docs, build slides, chat with others or even get your calc on in sheets:
    `gemini extensions install https://github.com/gemini-cli-extensions/workspace`
    - Blog:
      [https://allen.hutchison.org/2025/11/19/bringing-the-office-to-the-terminal/](https://allen.hutchison.org/2025/11/19/bringing-the-office-to-the-terminal/)
  - **Redis:** Manage and search data in Redis with natural language:
    `gemini extensions install https://github.com/redis/mcp-redis`
  - **Anomalo:** Query your data warehouse table metadata and quality status
    through commands and natural language:
    `gemini extensions install https://github.com/datagravity-ai/anomalo-gemini-extension`
- **Experimental permission improvements:** We are now experimenting with a new
  policy engine in Gemini CLI. This allows users and administrators to create
  fine-grained policy for tool calls. Currently behind a flag. See
  [policy engine documentation](/docs/reference/policy-engine) for more
  information.
  - Blog:
    [https://allen.hutchison.org/2025/11/26/the-guardrails-of-autonomy/](https://allen.hutchison.org/2025/11/26/the-guardrails-of-autonomy/)
- **Gemini 3 support for paid:** Gemini 3 support has been rolled out to all API
  key, Google AI Pro or Google AI Ultra (for individuals, not businesses) and
  Gemini Code Assist Enterprise users. Enable it via `/settings` and toggling on
  **Preview Features**.
- **Updated UI rollback:** We’ve temporarily rolled back our updated UI to give
  it more time to bake. This means for a time you won’t have embedded scrolling
  or mouse support. You can re-enable with `/settings` -> **Use Alternate Screen
  Buffer** -> `true`.
- **Model in history:** Users can now toggle in `/settings` to display model in
  their chat history. ([gif](https://imgur.com/a/uEmNKnQ),
  [pr](https://github.com/google-gemini/gemini-cli/pull/13034) by
  [@scidomino](https://github.com/scidomino))
- **Multi-uninstall:** Users can now uninstall multiple extensions with a single
  command. ([pic](https://imgur.com/a/9Dtq8u2),
  [pr](https://github.com/google-gemini/gemini-cli/pull/13016) by
  [@JayadityaGit](https://github.com/JayadityaGit))