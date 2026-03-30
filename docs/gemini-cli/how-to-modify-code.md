## How to modify code

Once Gemini CLI has context, you can direct it to make specific edits. The agent
is capable of complex refactoring, not just simple text replacement.

```none
`Update @src/components/UserProfile.tsx to show a loading spinner if the user data is null.`
```

Gemini CLI uses the `replace` tool to propose a targeted code change.