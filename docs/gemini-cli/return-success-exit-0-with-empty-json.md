# Return success (exit 0) with empty JSON
echo "{}"
exit 0
EOF

chmod +x .gemini/hooks/log-tools.sh
```

**Windows (PowerShell)**

```powershell
New-Item -ItemType Directory -Force -Path ".gemini\hooks"
@"