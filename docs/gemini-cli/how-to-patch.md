### How to patch

#### 1. Create the patch pull request

There are two ways to create a patch pull request:

**Option A: From a GitHub comment (recommended)**

After a pull request containing the fix has been merged, a maintainer can add a
comment on that same PR with the following format:

`/patch [channel]`

- **channel** (optional):
  - _no channel_ - patches both stable and preview channels (default,
    recommended for most fixes)
  - `both` - patches both stable and preview channels (same as default)
  - `stable` - patches only the stable channel
  - `preview` - patches only the preview channel

Examples:

- `/patch` (patches both stable and preview - default)
- `/patch both` (patches both stable and preview - explicit)
- `/patch stable` (patches only stable)
- `/patch preview` (patches only preview)

The `Release: Patch from Comment` workflow will automatically find the merge
commit SHA and trigger the `Release: Patch (1) Create PR` workflow. If the PR is
not yet merged, it will post a comment indicating the failure.

**Option B: Manually triggering the workflow**

Navigate to the **Actions** tab and run the **Release: Patch (1) Create PR**
workflow.

- **Commit**: The full SHA of the commit on `main` that you want to cherry-pick.
- **Channel**: The channel you want to patch (`stable` or `preview`).

This workflow will automatically:

1.  Find the latest release tag for the channel.
2.  Create a release branch from that tag if one doesn't exist (e.g.,
    `release/v0.5.1-pr-12345`).
3.  Create a new hotfix branch from the release branch.
4.  Cherry-pick your specified commit into the hotfix branch.
5.  Create a pull request from the hotfix branch back to the release branch.

#### 2. Review and merge

Review the automatically created pull request(s) to ensure the cherry-pick was
successful and the changes are correct. Once approved, merge the pull request.

<!-- prettier-ignore -->
> [!WARNING]
> The `release/*` branches are protected by branch protection
> rules. A pull request to one of these branches requires at least one review from
> a code owner before it can be merged. This ensures that no unauthorized code is
> released.

#### 2.5. Adding multiple commits to a hotfix (advanced)

If you need to include multiple fixes in a single patch release, you can add
additional commits to the hotfix branch after the initial patch PR has been
created:

1. **Start with the primary fix**: Use `/patch` (or `/patch both`) on the most
   important PR to create the initial hotfix branch and PR.

2. **Checkout the hotfix branch locally**:

   ```bash
   git fetch origin
   git checkout hotfix/v0.5.1/stable/cherry-pick-abc1234  # Use the actual branch name from the PR
   ```

3. **Cherry-pick additional commits**:

   ```bash
   git cherry-pick <commit-sha-1>
   git cherry-pick <commit-sha-2>
   # Add as many commits as needed
   ```

4. **Push the updated branch**:

   ```bash
   git push origin hotfix/v0.5.1/stable/cherry-pick-abc1234
   ```

5. **Test and review**: The existing patch PR will automatically update with
   your additional commits. Test thoroughly since you're now releasing multiple
   changes together.

6. **Update the PR description**: Consider updating the PR title and description
   to reflect that it includes multiple fixes.

This approach allows you to group related fixes into a single patch release
while maintaining full control over what gets included and how conflicts are
resolved.

#### 3. Automatic release

Upon merging the pull request, the `Release: Patch (2) Trigger` workflow is
automatically triggered. It will then start the `Release: Patch (3) Release`
workflow, which will:

1.  Build and test the patched code.
2.  Publish the new patch version to npm.
3.  Create a new GitHub release with the patch notes.

This fully automated process ensures that patches are created and released
consistently and reliably.

#### Troubleshooting: Older branch workflows

**Issue**: If the patch trigger workflow fails with errors like "Resource not
accessible by integration" or references to non-existent workflow files (e.g.,
`patch-release.yml`), this indicates the hotfix branch contains an outdated
version of the workflow files.

**Root cause**: When a PR is merged, GitHub Actions runs the workflow definition
from the **source branch** (the hotfix branch), not from the target branch (the
release branch). If the hotfix branch was created from an older release branch
that predates workflow improvements, it will use the old workflow logic.

**Solutions**:

**Option 1: Manual trigger (quick fix)** Manually trigger the updated workflow
from the branch with the latest workflow code:

```bash