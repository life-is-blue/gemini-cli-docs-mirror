## How it works

When you add a path to your `.geminiignore` file, tools that respect this file
will exclude matching files and directories from their operations. For example,
when you use the `@` command to share files, any paths in your `.geminiignore`
file will be automatically excluded.

For the most part, `.geminiignore` follows the conventions of `.gitignore`
files:

- Blank lines and lines starting with `#` are ignored.
- Standard glob patterns are supported (such as `*`, `?`, and `[]`).
- Putting a `/` at the end will only match directories.
- Putting a `/` at the beginning anchors the path relative to the
  `.geminiignore` file.
- `!` negates a pattern.

You can update your `.geminiignore` file at any time. To apply the changes, you
must restart your Gemini CLI session.