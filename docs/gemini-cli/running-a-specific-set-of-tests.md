## Running a specific set of tests

To run a subset of test files, you can use
`npm run <integration test command> <file_name1> ....` where &lt;integration
test command&gt; is either `test:e2e` or `test:integration*` and `<file_name>`
is any of the `.test.js` files in the `integration-tests/` directory. For
example, the following command runs `list_directory.test.js` and
`write_file.test.js`:

```bash
npm run test:e2e list_directory write_file
```