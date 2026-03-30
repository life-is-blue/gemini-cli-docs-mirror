### Linting and preflight checks

To ensure code quality and formatting consistency, run the preflight check:

```bash
npm run preflight
```

This command will run ESLint, Prettier, all tests, and other checks as defined
in the project's `package.json`.

_ProTip_

after cloning create a git precommit hook file to ensure your commits are always
clean.

```bash
echo "