### Dynamic values

For `apiKey` and `http` auth types, secret values (`key`, `token`, `username`,
`password`, `value`) support dynamic resolution:

| Format      | Description                                         | Example                    |
| :---------- | :-------------------------------------------------- | :------------------------- |
| `$ENV_VAR`  | Read from an environment variable.                  | `$MY_API_KEY`              |
| `!command`  | Execute a shell command and use the trimmed output. | `!gcloud auth print-token` |
| literal     | Use the string as-is.                               | `sk-abc123`                |
| `$$` / `!!` | Escape prefix. `$$FOO` becomes the literal `$FOO`.  | `$$NOT_AN_ENV_VAR`         |

> **Security tip:** Prefer `$ENV_VAR` or `!command` over embedding secrets
> directly in agent files, especially for project-level agents checked into
> version control.