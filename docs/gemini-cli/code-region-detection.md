## Code region detection

The import processor uses the `marked` library to detect code blocks and inline
code spans, ensuring that `@` imports inside these regions are properly ignored.
This provides robust handling of nested code blocks and complex Markdown
structures.