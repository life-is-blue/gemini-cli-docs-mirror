## Review and confirm changes

Gemini CLI prioritizes safety. Before any file is modified, it presents a
unified diff of the proposed changes.

```diff
- if (!user) return null;
+ if (!user) return <LoadingSpinner />;
```

- **Red lines (-):** Code that will be removed.
- **Green lines (+):** Code that will be added.

Press **y** to confirm and apply the change to your local file system. If the
diff doesn't look right, press **n** to cancel and refine your prompt.