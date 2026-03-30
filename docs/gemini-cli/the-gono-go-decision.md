## The "go/no-go" decision

Before triggering the `Release: Promote` workflow to move `preview` to `stable`:

1.  [ ] **Level 1:** CI and E2E workflows are green for the commit corresponding
        to the current `preview` tag.
2.  [ ] **Level 2:** The `preview` version has been out for one week, and the
        CUJ checklist has been completed successfully by a release manager. No
        blocking issues have been reported.
3.  [ ] **Level 3:** Dashboard Health and Model Evaluation checks have been
        completed and show no regressions.

If all checks pass, proceed with the promotion.