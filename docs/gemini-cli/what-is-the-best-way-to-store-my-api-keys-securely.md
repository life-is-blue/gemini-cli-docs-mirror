### What is the best way to store my API keys securely?

Exposing API keys in scripts or checking them into source control is a security
risk.

To store your API keys securely, you can:

- **Use a `.env` file:** Create a `.env` file in your project's `.gemini`
  directory (`.gemini/.env`) and store your keys there. Gemini CLI will
  automatically load these variables.
- **Use your system's keyring:** For the most secure storage, use your operating
  system's secret management tool (like macOS Keychain, Windows Credential
  Manager, or a secret manager on Linux). You can then have your scripts or
  environment load the key from the secure storage at runtime.