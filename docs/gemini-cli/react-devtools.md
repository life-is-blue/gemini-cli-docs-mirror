### React DevTools

To debug the CLI's React-based UI, you can use React DevTools.

1.  **Start the Gemini CLI in development mode:**

    ```bash
    DEV=true npm start
    ```

2.  **Install and run React DevTools version 6 (which matches the CLI's
    `react-devtools-core`):**

    You can either install it globally:

    ```bash
    npm install -g react-devtools@6
    react-devtools
    ```

    Or run it directly using npx:

    ```bash
    npx react-devtools@6
    ```

    Your running CLI application should then connect to React DevTools.
    ![](/docs/assets/connected_devtools.png)