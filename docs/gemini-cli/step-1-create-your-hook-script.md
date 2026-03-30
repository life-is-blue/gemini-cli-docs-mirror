### Step 1: Create your hook script

Create a directory for hooks and a simple logging script.

> **Note**:
>
> This example uses `jq` to parse JSON. If you don't have it installed, you can
> perform similar logic using Node.js or Python.

**macOS/Linux**

```bash
mkdir -p .gemini/hooks
cat > .gemini/hooks/log-tools.sh << 'EOF'
#!/usr/bin/env bash