### Security: Block secrets in commits

Prevent committing files containing API keys or passwords. Note that we use
**Exit Code 0** to provide a structured denial message to the agent.

**`.gemini/hooks/block-secrets.sh`:**

```bash
#!/usr/bin/env bash
input=$(cat)