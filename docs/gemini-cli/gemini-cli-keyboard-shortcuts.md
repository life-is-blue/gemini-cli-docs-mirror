# [Gemini CLI keyboard shortcuts](http://geminicli.com/docs/reference/keyboard-shortcuts.md)


Gemini CLI ships with a set of default keyboard shortcuts for editing input,
navigating history, and controlling the UI. Use this reference to learn the
available combinations.

<!-- KEYBINDINGS-AUTOGEN:START -->

#### Basic Controls

| Command         | Action                                                          | Keys                |
| --------------- | --------------------------------------------------------------- | ------------------- |
| `basic.confirm` | Confirm the current selection or choice.                        | `Enter`             |
| `basic.cancel`  | Dismiss dialogs or cancel the current focus.                    | `Esc`<br />`Ctrl+[` |
| `basic.quit`    | Cancel the current request or quit the CLI when input is empty. | `Ctrl+C`            |
| `basic.exit`    | Exit the CLI when the input buffer is empty.                    | `Ctrl+D`            |

#### Cursor Movement

| Command            | Action                                      | Keys                                       |
| ------------------ | ------------------------------------------- | ------------------------------------------ |
| `cursor.home`      | Move the cursor to the start of the line.   | `Ctrl+A`<br />`Home`                       |
| `cursor.end`       | Move the cursor to the end of the line.     | `Ctrl+E`<br />`End`                        |
| `cursor.up`        | Move the cursor up one line.                | `Up`                                       |
| `cursor.down`      | Move the cursor down one line.              | `Down`                                     |
| `cursor.left`      | Move the cursor one character to the left.  | `Left`                                     |
| `cursor.right`     | Move the cursor one character to the right. | `Right`<br />`Ctrl+F`                      |
| `cursor.wordLeft`  | Move the cursor one word to the left.       | `Ctrl+Left`<br />`Alt+Left`<br />`Alt+B`   |
| `cursor.wordRight` | Move the cursor one word to the right.      | `Ctrl+Right`<br />`Alt+Right`<br />`Alt+F` |

#### Editing

| Command                | Action                                           | Keys                                                     |
| ---------------------- | ------------------------------------------------ | -------------------------------------------------------- |
| `edit.deleteRightAll`  | Delete from the cursor to the end of the line.   | `Ctrl+K`                                                 |
| `edit.deleteLeftAll`   | Delete from the cursor to the start of the line. | `Ctrl+U`                                                 |
| `edit.clear`           | Clear all text in the input field.               | `Ctrl+C`                                                 |
| `edit.deleteWordLeft`  | Delete the previous word.                        | `Ctrl+Backspace`<br />`Alt+Backspace`<br />`Ctrl+W`      |
| `edit.deleteWordRight` | Delete the next word.                            | `Ctrl+Delete`<br />`Alt+Delete`<br />`Alt+D`             |
| `edit.deleteLeft`      | Delete the character to the left.                | `Backspace`<br />`Ctrl+H`                                |
| `edit.deleteRight`     | Delete the character to the right.               | `Delete`<br />`Ctrl+D`                                   |
| `edit.undo`            | Undo the most recent text edit.                  | `Cmd/Win+Z`<br />`Alt+Z`                                 |
| `edit.redo`            | Redo the most recent undone text edit.           | `Ctrl+Shift+Z`<br />`Shift+Cmd/Win+Z`<br />`Alt+Shift+Z` |

#### Scrolling

| Command           | Action                   | Keys                          |
| ----------------- | ------------------------ | ----------------------------- |
| `scroll.up`       | Scroll content up.       | `Shift+Up`                    |
| `scroll.down`     | Scroll content down.     | `Shift+Down`                  |
| `scroll.home`     | Scroll to the top.       | `Ctrl+Home`<br />`Shift+Home` |
| `scroll.end`      | Scroll to the bottom.    | `Ctrl+End`<br />`Shift+End`   |
| `scroll.pageUp`   | Scroll up by one page.   | `Page Up`                     |
| `scroll.pageDown` | Scroll down by one page. | `Page Down`                   |

#### History & Search

| Command                 | Action                                       | Keys     |
| ----------------------- | -------------------------------------------- | -------- |
| `history.previous`      | Show the previous entry in history.          | `Ctrl+P` |
| `history.next`          | Show the next entry in history.              | `Ctrl+N` |
| `history.search.start`  | Start reverse search through history.        | `Ctrl+R` |
| `history.search.submit` | Submit the selected reverse-search match.    | `Enter`  |
| `history.search.accept` | Accept a suggestion while reverse searching. | `Tab`    |

#### Navigation

| Command               | Action                                             | Keys            |
| --------------------- | -------------------------------------------------- | --------------- |
| `nav.up`              | Move selection up in lists.                        | `Up`            |
| `nav.down`            | Move selection down in lists.                      | `Down`          |
| `nav.dialog.up`       | Move up within dialog options.                     | `Up`<br />`K`   |
| `nav.dialog.down`     | Move down within dialog options.                   | `Down`<br />`J` |
| `nav.dialog.next`     | Move to the next item or question in a dialog.     | `Tab`           |
| `nav.dialog.previous` | Move to the previous item or question in a dialog. | `Shift+Tab`     |

#### Suggestions & Completions

| Command                 | Action                                  | Keys                 |
| ----------------------- | --------------------------------------- | -------------------- |
| `suggest.accept`        | Accept the inline suggestion.           | `Tab`<br />`Enter`   |
| `suggest.focusPrevious` | Move to the previous completion option. | `Up`<br />`Ctrl+P`   |
| `suggest.focusNext`     | Move to the next completion option.     | `Down`<br />`Ctrl+N` |
| `suggest.expand`        | Expand an inline suggestion.            | `Right`              |
| `suggest.collapse`      | Collapse an inline suggestion.          | `Left`               |

#### Text Input

| Command                    | Action                                                                    | Keys                                                                                |
| -------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `input.submit`             | Submit the current prompt.                                                | `Enter`                                                                             |
| `input.queueMessage`       | Queue the current prompt to be processed after the current task finishes. | `Tab`                                                                               |
| `input.newline`            | Insert a newline without submitting.                                      | `Ctrl+Enter`<br />`Cmd/Win+Enter`<br />`Alt+Enter`<br />`Shift+Enter`<br />`Ctrl+J` |
| `input.openExternalEditor` | Open the current prompt or the plan in an external editor.                | `Ctrl+X`                                                                            |
| `input.paste`              | Paste from the clipboard.                                                 | `Ctrl+V`<br />`Cmd/Win+V`<br />`Alt+V`                                              |

#### App Controls

| Command                       | Action                                                                                                                                             | Keys               |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `app.showErrorDetails`        | Toggle detailed error information.                                                                                                                 | `F12`              |
| `app.showFullTodos`           | Toggle the full TODO list.                                                                                                                         | `Ctrl+T`           |
| `app.showIdeContextDetail`    | Show IDE context details.                                                                                                                          | `Ctrl+G`           |
| `app.toggleMarkdown`          | Toggle Markdown rendering.                                                                                                                         | `Alt+M`            |
| `app.toggleCopyMode`          | Toggle copy mode when in alternate buffer mode.                                                                                                    | `Ctrl+S`           |
| `app.toggleYolo`              | Toggle YOLO (auto-approval) mode for tool calls.                                                                                                   | `Ctrl+Y`           |
| `app.cycleApprovalMode`       | Cycle through approval modes: default (prompt), auto_edit (auto-approve edits), and plan (read-only). Plan mode is skipped when the agent is busy. | `Shift+Tab`        |
| `app.showMoreLines`           | Expand and collapse blocks of content when not in alternate buffer mode.                                                                           | `Ctrl+O`           |
| `app.expandPaste`             | Expand or collapse a paste placeholder when cursor is over placeholder.                                                                            | `Ctrl+O`           |
| `app.focusShellInput`         | Move focus from Gemini to the active shell.                                                                                                        | `Tab`              |
| `app.unfocusShellInput`       | Move focus from the shell back to Gemini.                                                                                                          | `Shift+Tab`        |
| `app.clearScreen`             | Clear the terminal screen and redraw the UI.                                                                                                       | `Ctrl+L`           |
| `app.restart`                 | Restart the application.                                                                                                                           | `R`<br />`Shift+R` |
| `app.suspend`                 | Suspend the CLI and move it to the background.                                                                                                     | `Ctrl+Z`           |
| `app.showShellUnfocusWarning` | Show warning when trying to move focus away from shell input.                                                                                      | `Tab`              |

#### Background Shell Controls

| Command                     | Action                                                             | Keys        |
| --------------------------- | ------------------------------------------------------------------ | ----------- |
| `background.escape`         | Dismiss background shell list.                                     | `Esc`       |
| `background.select`         | Confirm selection in background shell list.                        | `Enter`     |
| `background.toggle`         | Toggle current background shell visibility.                        | `Ctrl+B`    |
| `background.toggleList`     | Toggle background shell list.                                      | `Ctrl+L`    |
| `background.kill`           | Kill the active background shell.                                  | `Ctrl+K`    |
| `background.unfocus`        | Move focus from background shell to Gemini.                        | `Shift+Tab` |
| `background.unfocusList`    | Move focus from background shell list to Gemini.                   | `Tab`       |
| `background.unfocusWarning` | Show warning when trying to move focus away from background shell. | `Tab`       |

<!-- KEYBINDINGS-AUTOGEN:END -->