# Hook logic
if process_input; then
  echo '{"decision": "allow"}'
  exit 0
else
  echo "Critical validation failure" >&2
  exit 2
fi

```