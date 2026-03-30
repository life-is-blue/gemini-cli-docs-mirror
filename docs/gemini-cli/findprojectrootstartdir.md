### `findProjectRoot(startDir)`

Finds the project root by searching for a `.git` directory upwards from the
given start directory. Implemented as an **async** function using non-blocking
file system APIs to avoid blocking the Node.js event loop.

**Parameters:**

- `startDir` (string): The directory to start searching from

**Returns:** Promise&lt;string&gt; - The project root directory (or the start
directory if no `.git` is found)