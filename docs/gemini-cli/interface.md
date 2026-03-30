## Interface

When you trigger a rewind, an interactive list of your previous interactions
appears.

1.  **Select interaction:** Use the **Up/Down arrow keys** to navigate through
    the list. The most recent interactions are at the bottom.
2.  **Preview:** As you select an interaction, you'll see a preview of the user
    prompt and, if applicable, the number of files changed during that step.
3.  **Confirm selection:** Press **Enter** on the interaction you want to rewind
    back to.
4.  **Action selection:** After selecting an interaction, you'll be presented
    with a confirmation dialog with up to three options:
    - **Rewind conversation and revert code changes:** Reverts both the chat
      history and the file modifications to the state before the selected
      interaction.
    - **Rewind conversation:** Only reverts the chat history. File changes are
      kept.
    - **Revert code changes:** Only reverts the file modifications. The chat
      history is kept.
    - **Do nothing (esc):** Cancels the rewind operation.

If no code changes were made since the selected point, the options related to
reverting code changes will be hidden.