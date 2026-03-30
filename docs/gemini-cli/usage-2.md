### Usage

#### Enabling and disabling

You can control the IDE integration from within the CLI:

- To enable the connection to the IDE, run:
  ```
  /ide enable
  ```
- To disable the connection, run:
  ```
  /ide disable
  ```

When enabled, Gemini CLI will automatically attempt to connect to the IDE
companion extension.

#### Checking the status

To check the connection status and see the context the CLI has received from the
IDE, run:

```
/ide status
```

If connected, this command will show the IDE it's connected to and a list of
recently opened files it is aware of.

<!-- prettier-ignore -->
> [!NOTE]
> The file list is limited to 10 recently accessed files within your
> workspace and only includes local files on disk.

#### Working with diffs

When you ask Gemini to modify a file, it can open a diff view directly in your
editor.

**To accept a diff**, you can perform any of the following actions:

- Click the **checkmark icon** in the diff editor's title bar.
- Save the file (e.g., with `Cmd+S` or `Ctrl+S`).
- Open the Command Palette and run **Gemini CLI: Accept Diff**.
- Respond with `yes` in the CLI when prompted.

**To reject a diff**, you can:

- Click the **'x' icon** in the diff editor's title bar.
- Close the diff editor tab.
- Open the Command Palette and run **Gemini CLI: Close Diff Editor**.
- Respond with `no` in the CLI when prompted.

You can also **modify the suggested changes** directly in the diff view before
accepting them.

If you select ‘Allow for this session’ in the CLI, changes will no longer show
up in the IDE as they will be auto-accepted.