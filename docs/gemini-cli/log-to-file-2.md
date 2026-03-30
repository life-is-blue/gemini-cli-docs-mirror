# Log to file
"[`$(Get-Date -Format 'o')] Tool executed: `$toolName" | Out-File -FilePath ".gemini\tool-log.txt" -Append -Encoding utf8