# Invoked via: /review FileCommandLoader.ts

description = "Reviews the provided context using a best practice guide."
prompt = """
You are an expert code reviewer.

Your task is to review {{args}}.

Use the following best practices when providing your review:

@{docs/best-practices.md}
"""
```

When you run `/review FileCommandLoader.ts`, the `@{docs/best-practices.md}`
placeholder is replaced by the content of that file, and `{{args}}` is replaced
by the text you provided, before the final prompt is sent to the model.

---