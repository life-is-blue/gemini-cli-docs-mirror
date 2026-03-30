## Migrating an Extension Repository

If you need to move your extension to a new repository (e.g., from a personal
account to an organization) or rename it, you can use the `migratedTo` property
in your `gemini-extension.json` file to seamlessly transition your users.

1. **Create the new repository**: Setup your extension in its new location.
2. **Update the old repository**: In your original repository, update the
   `gemini-extension.json` file to include the `migratedTo` property, pointing
   to the new repository URL, and bump the version number. You can optionally
   change the `name` of your extension at this time in the new repository.
   ```json
   {
     "name": "my-extension",
     "version": "1.1.0",
     "migratedTo": "https://github.com/new-owner/new-extension-repo"
   }
   ```
3. **Release the update**: Publish this new version in your old repository.

When users check for updates, the Gemini CLI will detect the `migratedTo` field,
verify that the new repository contains a valid extension update, and
automatically update their local installation to track the new source and name
moving forward. All extension settings will automatically migrate to the new
installation.