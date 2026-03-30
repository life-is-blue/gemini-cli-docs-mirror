### How to create a manual release

1.  Navigate to the **Actions** tab of the repository.
2.  Select the **Release: Manual** workflow from the list.
3.  Click the **Run workflow** dropdown button.
4.  Fill in the required inputs:
    - **Version**: The exact version to release (e.g., `v0.6.1`). This must be a
      valid semantic version with a `v` prefix.
    - **Ref**: The branch, tag, or full commit SHA to release from.
    - **NPM Channel**: The npm channel to publish to. The options are `preview`,
      `nightly`, `latest` (for stable releases), and `dev`. The default is
      `dev`.
    - **Dry Run**: Leave as `true` to run all steps without publishing, or set
      to `false` to perform a live release.
    - **Force Skip Tests**: Set to `true` to skip the test suite. This is not
      recommended for production releases.
    - **Skip GitHub Release**: Set to `true` to skip creating a GitHub release
      and create an npm release only.
    - **Environment**: Select the appropriate environment. The `dev` environment
      is intended for testing. The `prod` environment is intended for production
      releases. `prod` is the default and will require authorization from a
      release administrator.
5.  Click **Run workflow**.

The workflow will then proceed to test (if not skipped), build, and publish the
release. If the workflow fails during a non-dry run, it will automatically
create a GitHub issue with the failure details.