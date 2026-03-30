### Enable sandboxing (in order of precedence)

1. **Command flag**: `-s` or `--sandbox`
2. **Environment variable**:
   `GEMINI_SANDBOX=true|docker|podman|sandbox-exec|runsc|lxc`
3. **Settings file**: `"sandbox": true` in the `tools` object of your
   `settings.json` file (e.g., `{"tools": {"sandbox": true}}`).