### Structure your extension

While simple extensions may contain only a few files, we recommend a organized
structure for complex projects.

```text
my-extension/
├── package.json
├── tsconfig.json
├── gemini-extension.json
├── src/
│   ├── index.ts
│   └── tools/
└── dist/
```

- **Use TypeScript:** We strongly recommend using TypeScript for type safety and
  improved developer experience.
- **Separate source and build:** Keep your source code in `src/` and output
  build artifacts to `dist/`.
- **Bundle dependencies:** If your extension has many dependencies, bundle them
  using a tool like `esbuild` to reduce installation time and avoid conflicts.