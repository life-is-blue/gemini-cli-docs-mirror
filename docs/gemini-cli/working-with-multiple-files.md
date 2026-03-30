### Working with multiple files

Complex features often span multiple files. You can chain `@` references to give
the agent a complete picture of the dependencies.

```bash
`@src/components/UserProfile.tsx @src/types/User.ts Refactor the component to use the updated User interface.`
```