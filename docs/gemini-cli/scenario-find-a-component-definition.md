### Scenario: Find a component definition

You know there's a `UserProfile` component, but you don't know where it lives.

```none
`Find the file that defines the UserProfile component.`
```

Gemini uses the `glob` or `list_directory` tools to search your project
structure. It will return the specific path (for example,
`src/components/UserProfile.tsx`), which you can then use with `@` in your next
turn.

<!-- prettier-ignore -->
> [!TIP]
> You can also ask for lists of files, like "Show me all the TypeScript
> configuration files in the root directory."