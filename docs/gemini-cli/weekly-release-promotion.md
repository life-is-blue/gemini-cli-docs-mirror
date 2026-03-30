## Weekly release promotion

Each Tuesday, the on-call engineer will trigger the "Promote Release" workflow.
This single action automates the entire weekly release process:

1.  **Promotes preview to stable:** The workflow identifies the latest `preview`
    release and promotes it to `stable`. This becomes the new `latest` version
    on npm.
2.  **Promotes nightly to preview:** The latest `nightly` release is then
    promoted to become the new `preview` version.
3.  **Prepares for next nightly:** A pull request is automatically created and
    merged to bump the version in `main` in preparation for the next nightly
    release.

This process ensures a consistent and reliable release cadence with minimal
manual intervention.