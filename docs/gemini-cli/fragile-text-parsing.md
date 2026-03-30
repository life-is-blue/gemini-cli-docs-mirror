# Fragile text parsing
tool_name=$(echo "$input" | grep -oP '"tool_name":\s*"\K[^"]+')

```

**Good:**

```bash