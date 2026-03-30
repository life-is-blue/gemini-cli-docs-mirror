### 3. Post-deployment smoke tests

After a release is published to npm, the `smoke-test.yml` workflow runs. This
must pass to confirm the package is installable and the binary is executable.

- **Command:** `npx -y @google/gemini-cli@<tag> --version` must return the
  correct version without error.
- **Platform:** Currently runs on `ubuntu-latest`.