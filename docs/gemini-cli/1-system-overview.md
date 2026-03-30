## 1. System Overview

The Model Configuration system (`ModelConfigService`) enables deterministic
control over model generation. It decouples the requested model identifier
(e.g., a CLI flag or agent request) from the underlying API configuration. This
allows for:

- **Precise Hyperparameter Tuning**: Direct control over `temperature`, `topP`,
  `thinkingBudget`, and other SDK-level parameters.
- **Environment-Specific Behavior**: Distinct configurations for different
  operating contexts (e.g., testing vs. production).
- **Agent-Scoped Customization**: Applying specific settings only when a
  particular agent is active.

The system operates on two core primitives: **Aliases** and **Overrides**.