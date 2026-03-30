### Manual publish

We publish an artifact for each commit to our internal registry. But if you need
to manually cut a local build, then run the following commands:

```
npm run clean
npm install
npm run auth
npm run prerelease:dev
npm publish --workspaces
```