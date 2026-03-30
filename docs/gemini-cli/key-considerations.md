## Key considerations

- **Destructive action:** Rewinding is a destructive action for your current
  session history and potentially your files. Use it with care.
- **Agent awareness:** When you rewind the conversation, the AI model loses all
  memory of the interactions that were removed. If you only revert code changes,
  you may need to inform the model that the files have changed.
- **Manual edits:** Rewinding only affects file changes made by the AI's edit
  tools. It does **not** undo manual edits you've made or changes triggered by
  the shell tool (`!`).
- **Compression:** Rewind works across chat compression points by reconstructing
  the history from stored session data.