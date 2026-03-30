# Run npm build and check for errors
if ! npm run preflight; then
  echo "npm build failed. Commit aborted."
  exit 1
fi
" > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

#### Formatting

To separately format the code in this project, run the following command from
the root directory:

```bash
npm run format
```

This command uses Prettier to format the code according to the project's style
guidelines.

#### Linting

To separately lint the code in this project, run the following command from the
root directory:

```bash
npm run lint
```