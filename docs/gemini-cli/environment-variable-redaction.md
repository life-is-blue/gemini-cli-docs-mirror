### Environment variable redaction

To prevent accidental leakage of sensitive information, Gemini CLI automatically
redacts potential secrets from environment variables when executing tools (such
as shell commands). This "best effort" redaction applies to variables inherited
from the system or loaded from `.env` files.

**Default Redaction Rules:**

- **By Name:** Variables are redacted if their names contain sensitive terms
  like `TOKEN`, `SECRET`, `PASSWORD`, `KEY`, `AUTH`, `CREDENTIAL`, `PRIVATE`, or
  `CERT`.
- **By Value:** Variables are redacted if their values match known secret
  patterns, such as:
  - Private keys (RSA, OpenSSH, PGP, etc.)
  - Certificates
  - URLs containing credentials
  - API keys and tokens (GitHub, Google, AWS, Stripe, Slack, etc.)
- **Specific Blocklist:** Certain variables like `CLIENT_ID`, `DB_URI`,
  `DATABASE_URL`, and `CONNECTION_STRING` are always redacted by default.

**Allowlist (Never Redacted):**

- Common system variables (e.g., `PATH`, `HOME`, `USER`, `SHELL`, `TERM`,
  `LANG`).
- Variables starting with `GEMINI_CLI_`.
- GitHub Action specific variables.

**Configuration:**

You can customize this behavior in your `settings.json` file:

- **`security.allowedEnvironmentVariables`**: A list of variable names to
  _never_ redact, even if they match sensitive patterns.
- **`security.blockedEnvironmentVariables`**: A list of variable names to
  _always_ redact, even if they don't match sensitive patterns.

```json
{
  "security": {
    "allowedEnvironmentVariables": ["MY_PUBLIC_KEY", "NOT_A_SECRET_TOKEN"],
    "blockedEnvironmentVariables": ["INTERNAL_IP_ADDRESS"]
  }
}
```