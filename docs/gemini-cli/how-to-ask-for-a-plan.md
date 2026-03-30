## How to ask for a plan

The best way to trigger task planning is to explicitly ask for it.

**Prompt:**
`I want to migrate this project from JavaScript to TypeScript. Please make a plan first.`

Gemini will analyze your codebase and use the `write_todos` tool to generate a
structured list.

**Example Plan:**

1.  [ ] Create `tsconfig.json`.
2.  [ ] Rename `.js` files to `.ts`.
3.  [ ] Fix type errors in `utils.js`.
4.  [ ] Fix type errors in `server.js`.
5.  [ ] Verify build passes.