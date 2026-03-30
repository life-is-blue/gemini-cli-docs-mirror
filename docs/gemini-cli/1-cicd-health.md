### 1. CI/CD health

All workflows in `.github/workflows/ci.yml` must pass on the `main` branch (for
nightly) or the release branch (for preview/stable).

- **Platforms:** Tests must pass on **Linux and macOS**.

<!-- prettier-ignore -->
> [!NOTE]
> Windows tests currently run with `continue-on-error: true`. While a
> failure here doesn't block the release technically, it should be
> investigated.

- **Checks:**
  - **Linting:** No linting errors (ESLint, Prettier, etc.).
  - **Typechecking:** No TypeScript errors.
  - **Unit Tests:** All unit tests in `packages/core` and `packages/cli` must
    pass.
  - **Build:** The project must build and bundle successfully.