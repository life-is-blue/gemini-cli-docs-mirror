# Validate JSON
if echo "$output" | jq empty 2>/dev/null; then
  echo "$output"
else
  echo "Invalid JSON generated" >&2
  exit 1
fi

```