### 6. Release automation

This workflow handles the process of packaging and publishing new versions of
the Gemini CLI.

- **Workflow File**: `.github/workflows/release-manual.yml`
- **When it runs**: On a daily schedule for "nightly" releases, and manually for
  official patch/minor releases.
- **What it does**:
  - Automatically builds the project, bumps the version numbers, and publishes
    the packages to npm.
  - Creates a corresponding release on GitHub with generated release notes.
- **What you should do**:
  - As a contributor, you don't need to do anything for this process. You can be
    confident that once your PR is merged into the `main` branch, your changes
    will be included in the very next nightly release.

We hope this detailed overview is helpful. If you have any questions about our
automation or processes, please don't hesitate to ask!