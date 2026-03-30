## Import tree structure

The processor returns an import tree that shows the hierarchy of imported files,
similar to Claude's `/memory` feature. This helps users debug problems with
their GEMINI.md files by showing which files were read and their import
relationships.

Example tree structure:

```
Memory Files
 L project: GEMINI.md
            L a.md
              L b.md
                L c.md
              L d.md
                L e.md
                  L f.md
            L included.md
```

The tree preserves the order that files were imported and shows the complete
import chain for debugging purposes.