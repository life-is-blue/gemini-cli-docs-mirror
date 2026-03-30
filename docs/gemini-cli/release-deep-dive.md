## Release deep dive

The release process creates two distinct types of artifacts for different
distribution channels: standard packages for the NPM registry and a single,
self-contained executable for GitHub Releases.

Here are the key stages:

**Stage 1: Pre-release sanity checks and versioning**

- **What happens:** Before any files are moved, the process ensures the project
  is in a good state. This involves running tests, linting, and type-checking
  (`npm run preflight`). The version number in the root `package.json` and
  `packages/cli/package.json` is updated to the new release version.

**Stage 2: Building the source code for NPM**

- **What happens:** The TypeScript source code in `packages/core/src` and
  `packages/cli/src` is compiled into standard JavaScript.
- **File movement:**
  - `packages/core/src/**/*.ts` -> compiled to -> `packages/core/dist/`
  - `packages/cli/src/**/*.ts` -> compiled to -> `packages/cli/dist/`
- **Why:** The TypeScript code written during development needs to be converted
  into plain JavaScript that can be run by Node.js. The `core` package is built
  first as the `cli` package depends on it.

**Stage 3: Publishing standard packages to NPM**

- **What happens:** The `npm publish` command is run for the
  `@google/gemini-cli-core` and `@google/gemini-cli` packages.
- **Why:** This publishes them as standard Node.js packages. Users installing
  via `npm install -g @google/gemini-cli` will download these packages, and
  `npm` will handle installing the `@google/gemini-cli-core` dependency
  automatically. The code in these packages is not bundled into a single file.

**Stage 4: Assembling and creating the GitHub release asset**

This stage happens _after_ the NPM publish and creates the single-file
executable that enables `npx` usage directly from the GitHub repository.

1.  **The JavaScript bundle is created:**
    - **What happens:** The built JavaScript from both `packages/core/dist` and
      `packages/cli/dist`, along with all third-party JavaScript dependencies,
      are bundled by `esbuild` into a single, executable JavaScript file (e.g.,
      `gemini.js`). The `node-pty` library is excluded from this bundle as it
      contains native binaries.
    - **Why:** This creates a single, optimized file that contains all the
      necessary application code. It simplifies execution for users who want to
      run the CLI without a full `npm install`, as all dependencies (including
      the `core` package) are included directly.

2.  **The `bundle` directory is assembled:**
    - **What happens:** A temporary `bundle` folder is created at the project
      root. The single `gemini.js` executable is placed inside it, along with
      other essential files.
    - **File movement:**
      - `gemini.js` (from esbuild) -> `bundle/gemini.js`
      - `README.md` -> `bundle/README.md`
      - `LICENSE` -> `bundle/LICENSE`
      - `packages/cli/src/utils/*.sb` (sandbox profiles) -> `bundle/`
    - **Why:** This creates a clean, self-contained directory with everything
      needed to run the CLI and understand its license and usage.

3.  **The GitHub release is created:**
    - **What happens:** The contents of the `bundle` directory, including the
      `gemini.js` executable, are attached as assets to a new GitHub Release.
    - **Why:** This makes the single-file version of the CLI available for
      direct download and enables the
      `npx https://github.com/google-gemini/gemini-cli` command, which downloads
      and runs this specific bundled asset.

**Summary of artifacts**

- **NPM:** Publishes standard, un-bundled Node.js packages. The primary artifact
  is the code in `packages/cli/dist`, which depends on
  `@google/gemini-cli-core`.
- **GitHub release:** Publishes a single, bundled `gemini.js` file that contains
  all dependencies, for easy execution via `npx`.

This dual-artifact process ensures that both traditional `npm` users and those
who prefer the convenience of `npx` have an optimized experience.