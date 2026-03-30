### 2. Critical user journey (CUJ) checklist

Before promoting a `preview` release to `stable`, a release manager must
manually run through this checklist.

- **Setup:**
  - [ ] Uninstall any existing global version:
        `npm uninstall -g @google/gemini-cli`
  - [ ] Clear npx cache (optional but recommended): `npm cache clean --force`
  - [ ] Install the preview version: `npm install -g @google/gemini-cli@preview`
  - [ ] Verify version: `gemini --version`

- **Authentication:**
  - [ ] In interactive mode run `/auth` and verify all sign in flows work:
    - [ ] Sign in with Google
    - [ ] API Key
    - [ ] Vertex AI

- **Basic prompting:**
  - [ ] Run `gemini "Tell me a joke"` and verify a sensible response.
  - [ ] Run in interactive mode: `gemini`. Ask a follow-up question to test
        context.

- **Piped input:**
  - [ ] Run `echo "Summarize this" | gemini` and verify it processes stdin.

- **Context management:**
  - [ ] In interactive mode, use `@file` to add a local file to context. Ask a
        question about it.

- **Settings:**
  - [ ] In interactive mode run `/settings` and make modifications
  - [ ] Validate that setting is changed

- **Function calling:**
  - [ ] In interactive mode, ask gemini to "create a file named hello.md with
        the content 'hello world'" and verify the file is created correctly.

If any of these CUJs fail, the release is a no-go until a patch is applied to
the `preview` channel.