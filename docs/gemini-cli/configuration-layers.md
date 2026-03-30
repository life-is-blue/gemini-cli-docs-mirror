## Configuration layers

Configuration is applied in the following order of precedence (lower numbers are
overridden by higher numbers):

1.  **Default values:** Hardcoded defaults within the application.
2.  **System defaults file:** System-wide default settings that can be
    overridden by other settings files.
3.  **User settings file:** Global settings for the current user.
4.  **Project settings file:** Project-specific settings.
5.  **System settings file:** System-wide settings that override all other
    settings files.
6.  **Environment variables:** System-wide or session-specific variables,
    potentially loaded from `.env` files.
7.  **Command-line arguments:** Values passed when launching the CLI.