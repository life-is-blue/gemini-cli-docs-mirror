### How to change a release tag

1.  Navigate to the **Actions** tab of the repository.
2.  Select the **Release: Change Tags** workflow from the list.
3.  Click the **Run workflow** dropdown button.
4.  Fill in the required inputs:
    - **Version**: The existing package version that you want to point the tag
      to (e.g., `0.5.0-preview-2`). This version **must** already be published
      to the npm registry.
    - **Channel**: The npm `dist-tag` to apply (e.g., `preview`, `stable`).
    - **Dry Run**: Leave as `true` to log the action without making changes, or
      set to `false` to perform the live tag change.
    - **Environment**: Select the appropriate environment. The `dev` environment
      is intended for testing. The `prod` environment is intended for production
      releases. `prod` is the default and will require authorization from a
      release administrator.
5.  Click **Run workflow**.

The workflow will then run `npm dist-tag add` for the appropriate `gemini-cli`,
`gemini-cli-core` and `gemini-cli-a2a-server` packages, pointing the specified
channel to the specified version.