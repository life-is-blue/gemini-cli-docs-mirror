### Scenario: Create a project context file

1.  In the root of your project, create a file named `GEMINI.md`.

2.  Add your instructions:

    ```markdown
    # Project Instructions

    - **Framework:** We use React with Vite.
    - **Styling:** Use Tailwind CSS for all styling. Do not write custom CSS.
    - **Testing:** All new components must include a Vitest unit test.
    - **Tone:** Be concise. Don't explain basic React concepts.
    ```

3.  Start a new session. Gemini CLI will now know these rules automatically.