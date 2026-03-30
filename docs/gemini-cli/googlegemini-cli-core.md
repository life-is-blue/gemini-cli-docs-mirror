## `@google/gemini-cli-core`

This package contains the core logic for interacting with the Gemini API. It is
responsible for making API requests, handling authentication, and managing the
local cache.

This package is not bundled. When it is published, it is published as a standard
Node.js package with its own dependencies. This allows it to be used as a
standalone package in other projects, if needed. All transpiled js code in the
`dist` folder is included in the package.