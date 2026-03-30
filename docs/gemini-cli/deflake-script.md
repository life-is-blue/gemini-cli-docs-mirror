### Deflake script

```bash
npm run deflake -- --runs=5 --command="npm run test:e2e -- -- --test-name-pattern '<your-new-test-name>'"
```

#### Deflake workflow

```bash
gh workflow run deflake.yml --ref <your-branch> -f test_name_pattern="<your-test-name-pattern>"
```