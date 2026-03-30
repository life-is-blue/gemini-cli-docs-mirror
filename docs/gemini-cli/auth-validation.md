### Auth validation

When Gemini CLI loads a remote agent, it validates your auth configuration
against the agent card's declared `securitySchemes`. If the agent requires
authentication that you haven't configured, you'll see an error describing
what's needed.

`google-credentials` is treated as compatible with `http` Bearer security
schemes, since it produces Bearer tokens.