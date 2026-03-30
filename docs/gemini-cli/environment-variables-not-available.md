### Environment variables not available

**Check if variable is set:**

```bash
#!/usr/bin/env bash
if [ -z "$GEMINI_PROJECT_DIR" ]; then
  echo "GEMINI_PROJECT_DIR not set" >&2
  exit 1
fi

```

**Debug available variables:**

```bash
env > .gemini/hook-env.log
```