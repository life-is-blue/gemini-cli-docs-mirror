# Invoked via: /git:fix "Button is misaligned"

description = "Generates a fix for a given issue."
prompt = "Please provide a code fix for the issue described here: {{args}}."
```

The model receives:
`Please provide a code fix for the issue described here: "Button is misaligned".`

**B. Using arguments in shell commands (inside `!{...}` blocks)**

When you use `{{args}}` inside a shell injection block (`!{...}`), the arguments
are automatically **shell-escaped** before replacement. This allows you to
safely pass arguments to shell commands, ensuring the resulting command is
syntactically correct and secure while preventing command injection
vulnerabilities.

**Example (`/grep-code.toml`):**

```toml
prompt = """
Please summarize the findings for the pattern `{{args}}`.

Search Results:
!{grep -r {{args}} .}
"""
```

When you run `/grep-code It's complicated`:

1. The CLI sees `{{args}}` used both outside and inside `!{...}`.
2. Outside: The first `{{args}}` is replaced raw with `It's complicated`.
3. Inside: The second `{{args}}` is replaced with the escaped version (e.g., on
   Linux: `"It\'s complicated"`).
4. The command executed is `grep -r "It's complicated" .`.
5. The CLI prompts you to confirm this exact, secure command before execution.
6. The final prompt is sent.