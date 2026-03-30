## Announcements: v0.23.0 - 2026-01-07

- 🎉 **Experimental Agent Skills Support in Preview:** Gemini CLI now supports
  [Agent Skills](https://agentskills.io/home) in our preview builds. This is an
  early preview where we’re looking for feedback!
  - Install Preview: `npm install -g @google/gemini-cli@preview`
  - Enable in `/settings`
  - Docs:
    [https://geminicli.com/docs/cli/skills/](https://geminicli.com/docs/cli/skills/)
- **Gemini CLI wrapped:** Run `npx gemini-wrapped` to visualize your usage
  stats, top models, languages, and more!
- **Windows clipboard image support:** Windows users can now paste images
  directly from their clipboard into the CLI using `Alt`+`V`.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/13997) by
  [@sgeraldes](https://github.com/sgeraldes))
- **Terminal background color detection:** Automatically optimizes your
  terminal's background color to select compatible themes and provide
  accessibility warnings.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/15132) by
  [@jacob314](https://github.com/jacob314))
- **Session logout:** Use the new `/logout` command to instantly clear
  credentials and reset your authentication state for seamless account
  switching. ([pr](https://github.com/google-gemini/gemini-cli/pull/13383) by
  [@CN-Scars](https://github.com/CN-Scars))