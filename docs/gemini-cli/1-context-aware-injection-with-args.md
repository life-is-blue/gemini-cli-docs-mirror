### 1. Context-aware injection with `{{args}}`

If your `prompt` contains the special placeholder `{{args}}`, the CLI will
replace that placeholder with the text the user typed after the command name.

The behavior of this injection depends on where it is used:

**A. Raw injection (outside shell commands)**

When used in the main body of the prompt, the arguments are injected exactly as
the user typed them.

**Example (`git/fix.toml`):**

```toml