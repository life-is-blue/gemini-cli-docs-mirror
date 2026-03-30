# [ACP Mode](http://geminicli.com/docs/cli/acp-mode.md)


ACP (Agent Client Protocol) mode is a special operational mode of Gemini CLI
designed for programmatic control, primarily for IDE and other developer tool
integrations. It uses a JSON-RPC protocol over stdio to communicate between
Gemini CLI agent and a client.

To start Gemini CLI in ACP mode, use the `--acp` flag:

```bash
gemini --acp
```