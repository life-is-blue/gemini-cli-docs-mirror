## How it works: The trust dialog

Once the feature is enabled, the first time you run the Gemini CLI from a
folder, a dialog will automatically appear, prompting you to make a choice:

- **Trust folder**: Grants full trust to the current folder (e.g.,
  `my-project`).
- **Trust parent folder**: Grants trust to the parent directory (e.g.,
  `safe-projects`), which automatically trusts all of its subdirectories as
  well. This is useful if you keep all your safe projects in one place.
- **Don't trust**: Marks the folder as untrusted. The CLI will operate in a
  restricted "safe mode."

Your choice is saved in a central file (`~/.gemini/trustedFolders.json`), so you
will only be asked once per folder.