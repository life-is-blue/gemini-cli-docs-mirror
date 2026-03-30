### Auth retry behavior

All auth providers automatically retry on `401` and `403` responses by
re-fetching credentials (up to 2 retries). This handles cases like expired
tokens or rotated credentials. For `apiKey` with `!command` values, the command
is re-executed on retry to fetch a fresh key.