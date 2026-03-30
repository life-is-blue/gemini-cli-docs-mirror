### Use stderr for errors

Error messages on stderr are surfaced appropriately based on exit codes:

```javascript
try {
  const result = dangerousOperation();
  console.log(JSON.stringify({ result }));
} catch (error) {
  // Write the error description to stderr so the user/agent sees it
  console.error(`Hook error: ${error.message}`);
  process.exit(2); // Blocking error
}
```