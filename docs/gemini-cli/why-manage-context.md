## Why manage context?

Gemini CLI is powerful but general. It doesn't know your preferred testing
framework, your indentation style, or your preference against `any` in
TypeScript. Context management solves this by giving the agent persistent
memory.

You'll use these features when you want to:

- **Enforce standards:** Ensure every generated file matches your team's style
  guide.
- **Set a persona:** Tell the agent to act as a "Senior Rust Engineer" or "QA
  Specialist."
- **Remember facts:** Save details like "My database port is 5432" so you don't
  have to repeat them.