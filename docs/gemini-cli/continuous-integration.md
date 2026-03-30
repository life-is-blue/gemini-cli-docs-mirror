## Continuous integration

To ensure the integration tests are always run, a GitHub Actions workflow is
defined in `.github/workflows/chained_e2e.yml`. This workflow automatically runs
the integrations tests for pull requests against the `main` branch, or when a
pull request is added to a merge queue.

The workflow runs the tests in different sandboxing environments to ensure
Gemini CLI is tested across each:

- `sandbox:none`: Runs the tests without any sandboxing.
- `sandbox:docker`: Runs the tests in a Docker container.
- `sandbox:podman`: Runs the tests in a Podman container.