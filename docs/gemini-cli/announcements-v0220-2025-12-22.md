## Announcements: v0.22.0 - 2025-12-22

- 🎉**Free Tier + Gemini 3:** Free tier users now all have access to Gemini 3
  Pro & Flash. Enable in `/settings` by toggling "Preview Features" to `true`.
- 🎉**Gemini CLI + Colab:** Gemini CLI is now pre-installed. Can be used
  headlessly in notebook cells or interactively in the built-in terminal
  ([pic](https://imgur.com/a/G0Tn7vi))
- 🎉**Gemini CLI Extensions:**
  - **Conductor:** Planning++, Gemini works with you to build out a detailed
    plan, pull in extra details as needed, ultimately to give the LLM guardrails
    with artifacts. Measure twice, implement once!

    `gemini extensions install https://github.com/gemini-cli-extensions/conductor`

    Blog:
    [https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/](https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/)

  - **Endor Labs:** Perform code analysis, vulnerability scanning, and
    dependency checks using natural language.

    `gemini extensions install https://github.com/endorlabs/gemini-extension`