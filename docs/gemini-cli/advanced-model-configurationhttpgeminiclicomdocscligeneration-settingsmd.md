# [Advanced Model Configuration](http://geminicli.com/docs/cli/generation-settings.md)


This guide details the Model Configuration system within the Gemini CLI.
Designed for researchers, AI quality engineers, and advanced users, this system
provides a rigorous framework for managing generative model hyperparameters and
behaviors.

> **Warning**: This is a power-user feature. Configuration values are passed
> directly to the model provider with minimal validation. Incorrect settings
> (e.g., incompatible parameter combinations) may result in runtime errors from
> the API.