### 2. Tool discovery

Upon successful connection:

1. **Tool listing:** The client calls the MCP server's tool listing endpoint
2. **Schema validation:** Each tool's function declaration is validated
3. **Tool filtering:** Tools are filtered based on `includeTools` and
   `excludeTools` configuration
4. **Name sanitization:** Tool names are cleaned to meet Gemini API
   requirements:
   - Characters other than letters, numbers, underscore (`_`), hyphen (`-`), dot
     (`.`), and colon (`:`) are replaced with underscores
   - Names longer than 63 characters are truncated with middle replacement
     (`...`)