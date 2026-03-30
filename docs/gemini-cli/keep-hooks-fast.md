### Keep hooks fast

Hooks run synchronously—slow hooks delay the agent loop. Optimize for speed by
using parallel operations:

```javascript
// Sequential operations are slower
const data1 = await fetch(url1).then((r) => r.json());
const data2 = await fetch(url2).then((r) => r.json());

// Prefer parallel operations for better performance
// Start requests concurrently
const p1 = fetch(url1).then((r) => r.json());
const p2 = fetch(url2).then((r) => r.json());

// Wait for all results
const [data1, data2] = await Promise.all([p1, p2]);
```