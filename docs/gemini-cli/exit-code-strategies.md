## Exit Code Strategies

There are two ways to control or block an action in Gemini CLI:

| Strategy                   | Exit Code | Implementation                                                     | Best For                                                    |
| :------------------------- | :-------- | :----------------------------------------------------------------- | :---------------------------------------------------------- |
| **Structured (Idiomatic)** | `0`       | Return a JSON object like `{"decision": "deny", "reason": "..."}`. | Production hooks, custom user feedback, and complex logic.  |
| **Emergency Brake**        | `2`       | Print the error message to `stderr` and exit.                      | Simple security gates, script errors, or rapid prototyping. |