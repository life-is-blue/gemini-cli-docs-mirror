## Use Gemini API key <a id="gemini-api"></a>

If you don't want to authenticate using your Google account, you can use an API
key from Google AI Studio.

To authenticate and use Gemini CLI with a Gemini API key:

1. Obtain your API key from
   [Google AI Studio](https://aistudio.google.com/app/apikey).

2. Set the `GEMINI_API_KEY` environment variable to your key. For example:

   **macOS/Linux**

   ```bash
   # Replace YOUR_GEMINI_API_KEY with the key from AI Studio
   export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
   ```

   **Windows (PowerShell)**

   ```powershell
   # Replace YOUR_GEMINI_API_KEY with the key from AI Studio
   $env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
   ```

   To make this setting persistent, see
   [Persisting Environment Variables](#persisting-vars).

3. Start the CLI:

   ```bash
   gemini
   ```

4. Select **Use Gemini API key**.

<!-- prettier-ignore -->
> [!WARNING]
> Treat API keys, especially for services like Gemini, as sensitive
> credentials. Protect them to prevent unauthorized access and potential misuse
> of the service under your account.