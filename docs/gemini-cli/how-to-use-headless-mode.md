## How to use headless mode

Run Gemini CLI in headless mode by providing a prompt with the `-p` (or
`--prompt`) flag. This bypasses the interactive chat interface and prints the
response to standard output (stdout). Positional arguments without the flag
default to interactive mode, unless the input or output is piped or redirected.

Run a single command:

```bash
gemini -p "Write a poem about TypeScript"
```