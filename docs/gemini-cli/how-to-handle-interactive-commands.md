## How to handle interactive commands

Gemini CLI attempts to handle interactive commands (like `git add -p` or
confirmation prompts) by streaming the output to you. However, for highly
interactive tools (like `vim` or `top`), it's often better to run them yourself
in a separate terminal window or use the `!` prefix.