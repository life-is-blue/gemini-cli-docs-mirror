### Schema compatibility

- **Property stripping:** The system automatically removes certain schema
  properties (`$schema`, `additionalProperties`) for Gemini API compatibility
- **Name sanitization:** Tool names are automatically sanitized to meet API
  requirements
- **Conflict resolution:** Tool name conflicts between servers are resolved
  through automatic prefixing

This comprehensive integration makes MCP servers a powerful way to extend the
Gemini CLI's capabilities while maintaining security, reliability, and ease of
use.