## Local testing and validation: Changes to the packaging and publishing process

If you need to test the release process without actually publishing to NPM or
creating a public GitHub release, you can trigger the workflow manually from the
GitHub UI.

1.  Go to the
    [Actions tab](https://github.com/google-gemini/gemini-cli/actions/workflows/release-manual.yml)
    of the repository.
2.  Click on the "Run workflow" dropdown.
3.  Leave the `dry_run` option checked (`true`).
4.  Click the "Run workflow" button.

This will run the entire release process but will skip the `npm publish` and
`gh release create` steps. You can inspect the workflow logs to ensure
everything is working as expected.

It is crucial to test any changes to the packaging and publishing process
locally before committing them. This ensures that the packages will be published
correctly and that they will work as expected when installed by a user.

To validate your changes, you can perform a dry run of the publishing process.
This will simulate the publishing process without actually publishing the
packages to the npm registry.

```bash
npm_package_version=9.9.9 SANDBOX_IMAGE_REGISTRY="registry" SANDBOX_IMAGE_NAME="thename" npm run publish:npm --dry-run
```

This command will do the following:

1.  Build all the packages.
2.  Run all the prepublish scripts.
3.  Create the package tarballs that would be published to npm.
4.  Print a summary of the packages that would be published.

You can then inspect the generated tarballs to ensure that they contain the
correct files and that the `package.json` files have been updated correctly. The
tarballs will be created in the root of each package's directory (e.g.,
`packages/cli/google-gemini-cli-0.1.6.tgz`).

By performing a dry run, you can be confident that your changes to the packaging
process are correct and that the packages will be published successfully.