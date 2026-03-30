## Environment variables

When `run_shell_command` executes a command, it sets the `GEMINI_CLI=1`
environment variable in the subprocess's environment. This allows scripts or
tools to detect if they are being run from within the Gemini CLI.