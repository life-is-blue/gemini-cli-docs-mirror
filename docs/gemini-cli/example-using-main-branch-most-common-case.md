# Example using main branch (most common case)
gh workflow run release-patch-2-trigger.yml --ref main \
  --field ref="hotfix/v0.6.0-preview.2/preview/cherry-pick-abc1234" \
  --field workflow_ref=main \
  --field dry_run=false \
  --field force_skip_tests=true
```

**Note**: Replace `<branch-with-updated-workflow>` with the branch containing
the latest workflow improvements (usually `main`, but could be a feature branch
if testing updates).

**Option 2: Update the hotfix branch** Merge the latest main branch into your
hotfix branch to get the updated workflows:

```bash
git checkout hotfix/v0.6.0-preview.2/preview/cherry-pick-abc1234
git merge main
git push
```

Then close and reopen the PR to retrigger the workflow with the updated version.

**Option 3: Direct release trigger** Skip the trigger workflow entirely and
directly run the release workflow:

```bash