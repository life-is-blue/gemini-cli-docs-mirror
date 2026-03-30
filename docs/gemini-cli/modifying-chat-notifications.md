### Modifying chat notifications

Notifications use
[GitHub for Google Chat](https://workspace.google.com/marketplace/app/github_for_google_chat/536184076190).
To modify the notifications, use `/github-settings` within the chat space.

<!-- prettier-ignore -->
> [!WARNING]
> The following instructions describe a fragile workaround that depends on the
> internal structure of the chat application's UI. It is likely to break with
> future updates.

The list of available labels is not currently populated correctly. If you want
to add a label that does not appear alphabetically in the first 30 labels in the
repo, you must use your browser's developer tools to manually modify the UI:

1. Open your browser's developer tools (e.g., Chrome DevTools).
2. In the `/github-settings` dialog, inspect the list of labels.
3. Locate one of the `<li>` elements representing a label.
4. In the HTML, modify the `data-option-value` attribute of that `<li>` element
   to the desired label name (e.g., `release-failure`).
5. Click on your modified label in the UI to select it, then save your settings.