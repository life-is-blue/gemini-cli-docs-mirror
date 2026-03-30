# Extract tool name (requires jq)
tool_name=$(echo "$input" | jq -r '.tool_name')