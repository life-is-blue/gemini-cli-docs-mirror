### Build process

To clone the repository:

```bash
git clone https://github.com/google-gemini/gemini-cli.git # Or your fork's URL
cd gemini-cli
```

To install dependencies defined in `package.json` as well as root dependencies:

```bash
npm install
```

To build the entire project (all packages):

```bash
npm run build
```

This command typically compiles TypeScript to JavaScript, bundles assets, and
prepares the packages for execution. Refer to `scripts/build.js` and
`package.json` scripts for more details on what happens during the build.