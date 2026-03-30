### Model selection precedence

The model used by Gemini CLI is determined by the following order of precedence:

1.  **`--model` command-line flag:** A model specified with the `--model` flag
    when launching the CLI will always be used.
2.  **`GEMINI_MODEL` environment variable:** If the `--model` flag is not used,
    the CLI will use the model specified in the `GEMINI_MODEL` environment
    variable.
3.  **`model.name` in `settings.json`:** If neither of the above are set, the
    model specified in the `model.name` property of your `settings.json` file
    will be used.
4.  **Local model (experimental):** If the Gemma local model router is enabled
    in your `settings.json` file, the CLI will use the local Gemma model
    (instead of Gemini models) to route the request to an appropriate model.
5.  **Default model:** If none of the above are set, the default model will be
    used. The default model is `auto`