## How to use the `/model` command

Use the following command in Gemini CLI:

```
/model
```

Running this command will open a dialog with your options:

| Option            | Description                                                    | Models                                       |
| ----------------- | -------------------------------------------------------------- | -------------------------------------------- |
| Auto (Gemini 3)   | Let the system choose the best Gemini 3 model for your task.   | gemini-3-pro-preview, gemini-3-flash-preview |
| Auto (Gemini 2.5) | Let the system choose the best Gemini 2.5 model for your task. | gemini-2.5-pro, gemini-2.5-flash             |
| Manual            | Select a specific model.                                       | Any available model.                         |

We recommend selecting one of the above **Auto** options. However, you can
select **Manual** to select a specific model from those available.

You can also use the `--model` flag to specify a particular Gemini model on
startup. For more details, refer to the
[configuration documentation](/docs/reference/configuration).

Changes to these settings will be applied to all subsequent interactions with
Gemini CLI.