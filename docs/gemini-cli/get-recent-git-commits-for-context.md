# Get recent git commits for context
context=$(git log -5 --oneline 2>/dev/null || echo "No git history")