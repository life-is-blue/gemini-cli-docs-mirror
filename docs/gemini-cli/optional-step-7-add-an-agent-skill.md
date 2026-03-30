## (Optional) Step 7: Add an Agent Skill

[Agent Skills](/docs/cli/skills) bundle specialized expertise and workflows.
Skills are activated only when needed, which saves context tokens.

1.  Create a `skills` directory and a subdirectory for your skill:

    **macOS/Linux**

    ```bash
    mkdir -p skills/security-audit
    ```

    **Windows (PowerShell)**

    ```powershell
    New-Item -ItemType Directory -Force -Path "skills\security-audit"
    ```

2.  Create a `skills/security-audit/SKILL.md` file:

    ```markdown
    ---
    name: security-audit
    description:
      Expertise in auditing code for security vulnerabilities. Use when the user
      asks to "check for security issues" or "audit" their changes.
    ---

    # Security Auditor

    You are an expert security researcher. When auditing code:

    1. Look for common vulnerabilities (OWASP Top 10).
    2. Check for hardcoded secrets or API keys.
    3. Suggest remediation steps for any findings.
    ```

Gemini CLI automatically discovers skills bundled with your extension. The model
activates them when it identifies a relevant task.