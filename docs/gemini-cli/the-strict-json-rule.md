### The "Strict JSON" rule

The most common cause of hook failure is "polluting" the standard output.

- **stdout** is for **JSON only**.
- **stderr** is for **logs and text**.

**Good:**

```bash
#!/bin/bash
echo "Starting check..." >&2  # <--- Redirect to stderr
echo '{"decision": "allow"}'

```