### `BeforeModel`

Fires before sending a request to the LLM. Operates on a stable, SDK-agnostic
request format.

- **Input Fields**:
  - `llm_request`: (`object`) Contains `model`, `messages`, and `config`
    (generation params).
- **Relevant Output Fields**:
  - `hookSpecificOutput.llm_request`: An object that **overrides** parts of the
    outgoing request (e.g., changing models or temperature).
  - `hookSpecificOutput.llm_response`: A **Synthetic Response** object. If
    provided, the CLI skips the LLM call entirely and uses this as the response.
  - `decision`: Set to `"deny"` to block the request and abort the turn.
- **Exit Code 2 (Block Turn)**: Aborts the turn and skips the LLM call. Uses
  `stderr` as the error message.