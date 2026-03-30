### 2. End-to-end (E2E) tests

All workflows in `.github/workflows/chained_e2e.yml` must pass.

- **Platforms:** **Linux, macOS and Windows**.
- **Sandboxing:** Tests must pass with both `sandbox:none` and `sandbox:docker`
  on Linux.