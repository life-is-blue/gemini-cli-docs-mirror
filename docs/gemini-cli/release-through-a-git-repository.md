## Release through a Git repository

Releasing through Git is the most flexible option. Create a public Git
repository and provide the URL to your users. They can then install your
extension using `gemini extensions install <your-repo-uri>`.

Users can optionally depend on a specific branch, tag, or commit using the
`--ref` argument. For example:

```bash
gemini extensions install <your-repo-uri> --ref=stable
```

Whenever you push commits to the referenced branch, the CLI prompts users to
update their installation. The `HEAD` commit is always treated as the latest
version.