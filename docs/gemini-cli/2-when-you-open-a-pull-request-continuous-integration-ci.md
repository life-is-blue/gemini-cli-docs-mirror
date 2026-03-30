### 2. When you open a pull request: `Continuous Integration (CI)`

This workflow ensures that all changes meet our quality standards before they
can be merged.

- **Workflow File**: `.github/workflows/ci.yml`
- **When it runs**: On every push to a pull request.
- **What it does**:
  - **Lint**: Checks that your code adheres to our project's formatting and
    style rules.
  - **Test**: Runs our full suite of automated tests across macOS, Windows, and
    Linux, and on multiple Node.js versions. This is the most time-consuming
    part of the CI process.
  - **Post Coverage Comment**: After all tests have successfully passed, a bot
    will post a comment on your PR. This comment provides a summary of how well
    your changes are covered by tests.
- **What you should do**:
  - Ensure all CI checks pass. A green checkmark ✅ will appear next to your
    commit when everything is successful.
  - If a check fails (a red "X" ❌), click the "Details" link next to the failed
    check to view the logs, identify the problem, and push a fix.