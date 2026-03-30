## Building the tests

Prior to running any integration tests, you need to create a release bundle that
you want to actually test:

```bash
npm run bundle
```

You must re-run this command after making any changes to the CLI source code,
but not after making changes to tests.