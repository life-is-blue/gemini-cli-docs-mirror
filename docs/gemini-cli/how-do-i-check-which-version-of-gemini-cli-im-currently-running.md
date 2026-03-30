### How do I check which version of Gemini CLI I'm currently running?

You can check your current Gemini CLI version using one of these methods:

- Run `gemini --version` or `gemini -v` from your terminal
- Check the globally installed version using your package manager:
  - npm: `npm list -g @google/gemini-cli`
  - pnpm: `pnpm list -g @google/gemini-cli`
  - yarn: `yarn global list @google/gemini-cli`
  - bun: `bun pm ls -g @google/gemini-cli`
  - homebrew: `brew list --versions gemini-cli`
- Inside an active Gemini CLI session, use the `/about` command