### Step 1: Alias Resolution

The requested model string is looked up in the merged map of system `aliases`
and user `customAliases`.

1.  If found, the system recursively resolves the `extends` chain.
2.  Settings are merged from parent to child (child wins).
3.  This results in a base `ResolvedModelConfig`.
4.  If not found, the requested string is treated as the raw model name.