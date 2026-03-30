# Test regex pattern
echo "write_file|replace" | grep -E "write_.*|replace"

```

**Check disabled list:** Verify the hook is not listed in your `settings.json`:

```json
{
  "hooks": {
    "disabled": ["my-hook-name"]
  }
}
```

**Ensure script is executable**: For macOS and Linux users, verify the script
has execution permissions:

```bash
ls -la .gemini/hooks/my-hook.sh
chmod +x .gemini/hooks/my-hook.sh
```

**Windows Note**: On Windows, ensure your execution policy allows running
scripts (e.g., `Get-ExecutionPolicy`).

**Verify script path:** Ensure the path in `settings.json` resolves correctly.

```bash