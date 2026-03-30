# Validate JSON structure
if ! echo "$input" | jq empty 2>/dev/null; then
  echo "Invalid JSON input" >&2
  exit 1
fi