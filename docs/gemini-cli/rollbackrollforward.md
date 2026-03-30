## Rollback/rollforward

In the event that a release has a critical regression, you can quickly roll back
to a previous stable version or roll forward to a new patch by changing the npm
`dist-tag`. The `Release: Change Tags` workflow provides a safe and controlled
way to do this.

This is the preferred method for both rollbacks and rollforwards, as it does not
require a full release cycle.