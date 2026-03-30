# For a preview channel patch with tests skipped
gh workflow run release-patch-2-trigger.yml --ref <branch-with-updated-workflow> \
  --field ref="hotfix/v0.6.0-preview.2/preview/cherry-pick-abc1234" \
  --field workflow_ref=<branch-with-updated-workflow> \
  --field dry_run=false \
  --field force_skip_tests=true