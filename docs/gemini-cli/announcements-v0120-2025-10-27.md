## Announcements: v0.12.0 - 2025-10-27

![Codebase investigator subagent in Gemini CLI.](https://i.imgur.com/4J1njsx.png)

- **🎉 New partner extensions:**
  - **🤗 Hugging Face extension:** Access the Hugging Face hub.
    ([gif](https://drive.google.com/file/d/1LEzIuSH6_igFXq96_tWev11svBNyPJEB/view?usp=sharing&resourcekey=0-LtPTzR1woh-rxGtfPzjjfg))

    `gemini extensions install https://github.com/huggingface/hf-mcp-server`

  - **Monday.com extension**: Analyze your sprints, update your task boards,
    etc.
    ([gif](https://drive.google.com/file/d/1cO0g6kY1odiBIrZTaqu5ZakaGZaZgpQv/view?usp=sharing&resourcekey=0-xEr67SIjXmAXRe1PKy7Jlw))

    `gemini extensions install https://github.com/mondaycom/mcp`

  - **Data Commons extension:** Query public datasets or ground responses on
    data from Data Commons
    ([gif](https://drive.google.com/file/d/1cuj-B-vmUkeJnoBXrO_Y1CuqphYc6p-O/view?usp=sharing&resourcekey=0-0adXCXDQEd91ZZW63HbW-Q)).

    `gemini extensions install https://github.com/gemini-cli-extensions/datacommons`

- **Model selection:** Choose the Gemini model for your session with `/model`.
  ([pic](https://imgur.com/a/ABFcWWw),
  [pr](https://github.com/google-gemini/gemini-cli/pull/8940) by
  [@abhipatel12](https://github.com/abhipatel12)).
- **Model routing:** Gemini CLI will now intelligently pick the best model for
  the task. Simple queries will be sent to Flash while complex analytical or
  creative tasks will still use the power of Pro. This ensures your quota will
  last for a longer period of time. You can always opt-out of this via `/model`.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/9262) by
  [@abhipatel12](https://github.com/abhipatel12)).
  - Discussion:
    [https://github.com/google-gemini/gemini-cli/discussions/12375](https://github.com/google-gemini/gemini-cli/discussions/12375)
- **Codebase investigator subagent:** We now have a new built-in subagent that
  will explore your workspace and resolve relevant information to improve
  overall performance.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/9988) by
  [@abhipatel12](https://github.com/abhipatel12),
  [pr](https://github.com/google-gemini/gemini-cli/pull/10282) by
  [@silviojr](https://github.com/silviojr)).
  - Enable, disable, or limit turns in `/settings`, plus advanced configs in
    `settings.json` ([pic](https://imgur.com/a/yJiggNO),
    [pr](https://github.com/google-gemini/gemini-cli/pull/10844) by
    [@silviojr](https://github.com/silviojr)).
- **Explore extensions with `/extension`:** Users can now open the extensions
  page in their default browser directly from the CLI using the `/extension`
  explore command. ([pr](https://github.com/google-gemini/gemini-cli/pull/11846)
  by [@JayadityaGit](https://github.com/JayadityaGit)).
- **Configurable compression:** Users can modify the context compression
  threshold in `/settings` (decimal with percentage display). The default has
  been made more proactive
  ([pr](https://github.com/google-gemini/gemini-cli/pull/12317) by
  [@scidomino](https://github.com/scidomino)).
- **API key authentication:** Users can now securely enter and store their
  Gemini API key via a new dialog, eliminating the need for environment
  variables and repeated entry.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/11760) by
  [@galz10](https://github.com/galz10)).
- **Sequential approval:** Users can now approve multiple tool calls
  sequentially during execution.
  ([pr](https://github.com/google-gemini/gemini-cli/pull/11593) by
  [@joshualitt](https://github.com/joshualitt)).