### How to use manually-triggered tools

You can directly trigger key tools using special syntax in your prompt:

- **[File access](/docs/tools/file-system#read_many_files) (`@`):** Use the `@`
  symbol followed by a file or directory path to include its content in your
  prompt. This triggers the `read_many_files` tool.
- **[Shell commands](/docs/tools/shell) (`!`):** Use the `!` symbol followed by
  a system command to execute it directly. This triggers the `run_shell_command`
  tool.