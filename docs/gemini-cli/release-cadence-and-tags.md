## Release cadence and tags

We will follow https://semver.org/ as closely as possible but will call out when
or if we have to deviate from it. Our weekly releases will be minor version
increments and any bug or hotfixes between releases will go out as patch
versions on the most recent release.

Each Tuesday ~20:00 UTC new Stable and Preview releases will be cut. The
promotion flow is:

- Code is committed to main and pushed each night to nightly
- After no more than 1 week on main, code is promoted to the `preview` channel
- After 1 week the most recent `preview` channel is promoted to `stable` channel
- Patch fixes will be produced against both `preview` and `stable` as needed,
  with the final 'patch' version number incrementing each time.