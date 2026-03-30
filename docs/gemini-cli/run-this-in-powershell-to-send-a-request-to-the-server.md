# Run this in PowerShell to send a request to the server

$uri = "http://localhost:9379/v1beta/models/gemma3-1b-gpu-custom:generateContent"
$body = @{contents = @( @{
  role = "user"
  parts = @( @{ text = "Tell me a joke." } )
})} | ConvertTo-Json -Depth 10

Invoke-RestMethod -Uri $uri -Method Post -Body $body -ContentType "application/json"
```

#### Linux/MacOS

```bash
$ curl "http://localhost:9379/v1beta/models/gemma3-1b-gpu-custom:generateContent" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{"contents":[{"role":"user","parts":[{"text":"Tell me a joke."}]}]}'
```