### Running the CLI

To start the Gemini CLI from the source code (after building), run the following
command from the root directory:

```bash
npm start
```

If you'd like to run the source build outside of the gemini-cli folder, you can
utilize `npm link path/to/gemini-cli/packages/cli` (see:
[docs](https://docs.npmjs.com/cli/v9/commands/npm-link)) or
`alias gemini="node path/to/gemini-cli/packages/cli"` to run with `gemini`