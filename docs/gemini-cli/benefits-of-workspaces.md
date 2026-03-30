### Benefits of workspaces

- **Simplified dependency management**: Running `npm install` from the root of
  the project will install all dependencies for all packages in the workspace
  and link them together. This means you don't need to run `npm install` in each
  package's directory.
- **Automatic linking**: Packages within the workspace can depend on each other.
  When you run `npm install`, NPM will automatically create symlinks between the
  packages. This means that when you make changes to one package, the changes
  are immediately available to other packages that depend on it.
- **Simplified script execution**: You can run scripts in any package from the
  root of the project using the `--workspace` flag. For example, to run the
  `build` script in the `cli` package, you can run
  `npm run build --workspace @google/gemini-cli`.