## `@google/gemini-cli`

This is the main package for the Gemini CLI. It is responsible for the user
interface, command parsing, and all other user-facing functionality.

When this package is published, it is bundled into a single executable file.
This bundle includes all of the package's dependencies, including
`@google/gemini-cli-core`. This means that whether a user installs the package
with `npm install -g @google/gemini-cli` or runs it directly with
`npx @google/gemini-cli`, they are using this single, self-contained executable.