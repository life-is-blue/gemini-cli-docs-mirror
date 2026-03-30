## Understand the context hierarchy

The CLI uses a hierarchical system to source context. It loads various context
files from several locations, concatenates the contents of all found files, and
sends them to the model with every prompt. The CLI loads files in the following
order:

1.  **Global context file:**
    - **Location:** `~/.gemini/GEMINI.md` (in your user home directory).
    - **Scope:** Provides default instructions for all your projects.

2.  **Environment and workspace context files:**
    - **Location:** The CLI searches for `GEMINI.md` files in your configured
      workspace directories and their parent directories.
    - **Scope:** Provides context relevant to the projects you are currently
      working on.

3.  **Just-in-time (JIT) context files:**
    - **Location:** When a tool accesses a file or directory, the CLI
      automatically scans for `GEMINI.md` files in that directory and its
      ancestors up to a trusted root.
    - **Scope:** Lets the model discover highly specific instructions for
      particular components only when they are needed.

The CLI footer displays the number of loaded context files, which gives you a
quick visual cue of the active instructional context.