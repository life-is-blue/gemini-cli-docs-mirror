# Check for secrets
if echo "$content" | grep -qE 'api[_-]?key|password|secret'; then
  # Log to stderr
  echo "Blocked potential secret" >&2

  # Return structured denial to stdout
  cat <<EOF
{
  "decision": "deny",
  "reason": "Security Policy: Potential secret detected in content.",
  "systemMessage": "🔒 Security scanner blocked operation"
}
EOF
  exit 0
fi