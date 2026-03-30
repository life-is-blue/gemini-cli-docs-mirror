# Check file permissions before writing
if [ -w "$file_path" ]; then
  # Safe to write
else
  echo "Insufficient permissions" >&2
  exit 1
fi
```