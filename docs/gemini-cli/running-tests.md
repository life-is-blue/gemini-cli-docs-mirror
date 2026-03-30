### Running tests

This project contains two types of tests: unit tests and integration tests.

#### Unit tests

To execute the unit test suite for the project:

```bash
npm run test
```

This will run tests located in the `packages/core` and `packages/cli`
directories. Ensure tests pass before submitting any changes. For a more
comprehensive check, it is recommended to run `npm run preflight`.

#### Integration tests

The integration tests are designed to validate the end-to-end functionality of
the Gemini CLI. They are not run as part of the default `npm run test` command.

To run the integration tests, use the following command:

```bash
npm run test:e2e
```

For more detailed information on the integration testing framework, please see
the
[Integration Tests documentation](https://geminicli.com/docs/integration-tests).