### Validate inputs

Your MCP server runs on the user's machine. Always validate tool inputs to
prevent arbitrary code execution or unauthorized filesystem access.

```typescript
// Example: Validating paths
if (!path.resolve(inputPath).startsWith(path.resolve(allowedDir) + path.sep)) {
  throw new Error('Access denied');
}
```