## Release validation

After pushing a new release smoke testing should be performed to ensure that the
packages are working as expected. This can be done by installing the packages
locally and running a set of tests to ensure that they are functioning
correctly.

- `npx -y @google/gemini-cli@latest --version` to validate the push worked as
  expected if you were not doing a rc or dev tag
- `npx -y @google/gemini-cli@<release tag> --version` to validate the tag pushed
  appropriately
- _This is destructive locally_
  `npm uninstall @google/gemini-cli && npm uninstall -g @google/gemini-cli && npm cache clean --force &&  npm install @google/gemini-cli@<version>`
- Smoke testing a basic run through of exercising a few llm commands and tools
  is recommended to ensure that the packages are working as expected. We'll
  codify this more in the future.