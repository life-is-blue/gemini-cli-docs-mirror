# Extract content being written
content=$(echo "$input" | jq -r '.tool_input.content // .tool_input.new_string // ""')