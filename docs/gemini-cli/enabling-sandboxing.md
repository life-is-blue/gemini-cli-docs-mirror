### Enabling sandboxing

[Sandboxing](#sandboxing) is highly recommended and requires, at a minimum,
setting `GEMINI_SANDBOX=true` in your `~/.env` and ensuring a sandboxing
provider (e.g. `macOS Seatbelt`, `docker`, or `podman`) is available. See
[Sandboxing](#sandboxing) for details.

To build both the `gemini` CLI utility and the sandbox container, run
`build:all` from the root directory:

```bash
npm run build:all
```

To skip building the sandbox container, you can use `npm run build` instead.