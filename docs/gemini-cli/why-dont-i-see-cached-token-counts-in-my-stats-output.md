### Why don't I see cached token counts in my stats output?

Cached token information is only displayed when cached tokens are being used.
This feature is available for API key users (Gemini API key or Google Cloud
Vertex AI) but not for OAuth users (such as Google Personal/Enterprise accounts
like Google Gmail or Google Workspace, respectively). This is because the Gemini
Code Assist API does not support cached content creation. You can still view
your total token usage using the `/stats` command in Gemini CLI.