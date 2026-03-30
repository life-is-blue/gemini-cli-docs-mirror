# Extract the plan path from the tool input JSON
plan_path=$(jq -r '.tool_input.plan_path // empty')

if [ -f "$plan_path" ]; then
  # Generate a unique filename using a timestamp
  filename="$(date +%s)_$(basename "$plan_path")"

  # Upload the plan to GCS in the background so it doesn't block the CLI
  gsutil cp "$plan_path" "gs://my-audit-bucket/gemini-plans/$filename" > /dev/null 2>&1 &
fi