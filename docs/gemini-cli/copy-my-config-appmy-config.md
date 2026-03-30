# COPY ./my-config /app/my-config
```

When `.gemini/sandbox.Dockerfile` exists, you can use `BUILD_SANDBOX`
environment variable when running Gemini CLI to automatically build the custom
sandbox image:

```bash
BUILD_SANDBOX=1 gemini -s
```