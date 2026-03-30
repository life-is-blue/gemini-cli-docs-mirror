### Validate all inputs

Never trust data from hooks without validation. Hook inputs often come from the
LLM or user prompts, which can be manipulated.

```bash
#!/usr/bin/env bash
input=$(cat)