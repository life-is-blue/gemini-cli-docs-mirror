### Scenario: Choosing what to revert

Gemini gives you granular control over the undo process. You can choose to:

1.  **Rewind conversation:** Only remove the chat history. The files stay
    changed. (Useful if the code is good but the chat got off track).
2.  **Revert code changes:** Keep the chat history but undo the file edits.
    (Useful if you want to keep the context but retry the implementation).
3.  **Rewind both:** Restore everything to exactly how it was.