### Source of truth for versioning

To ensure the highest reliability, the release promotion process uses the **NPM
registry as the single source of truth** for determining the current version of
each release channel (`stable`, `preview`, and `nightly`).

1.  **Fetch from NPM:** The workflow begins by querying NPM's `dist-tags`
    (`latest`, `preview`, `nightly`) to get the exact version strings for the
    packages currently available to users.
2.  **Cross-check for integrity:** For each version retrieved from NPM, the
    workflow performs a critical integrity check:
    - It verifies that a corresponding **git tag** exists in the repository.
    - It verifies that a corresponding **GitHub release** has been created.
3.  **Halt on discrepancy:** If either the git tag or the GitHub Release is
    missing for a version listed on NPM, the workflow will immediately fail.
    This strict check prevents promotions from a broken or incomplete previous
    release and alerts the on-call engineer to a release state inconsistency
    that must be manually resolved.
4.  **Calculate next version:** Only after these checks pass does the workflow
    proceed to calculate the next semantic version based on the trusted version
    numbers retrieved from NPM.

This NPM-first approach, backed by integrity checks, makes the release process
highly robust and prevents the kinds of versioning discrepancies that can arise
from relying solely on git history or API outputs.