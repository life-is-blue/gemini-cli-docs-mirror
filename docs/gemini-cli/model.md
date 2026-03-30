### Model

| UI Label                      | Setting                      | Description                                                                            | Default     |
| ----------------------------- | ---------------------------- | -------------------------------------------------------------------------------------- | ----------- |
| Model                         | `model.name`                 | The Gemini model to use for conversations.                                             | `undefined` |
| Max Session Turns             | `model.maxSessionTurns`      | Maximum number of user/model/tool turns to keep in a session. -1 means unlimited.      | `-1`        |
| Context Compression Threshold | `model.compressionThreshold` | The fraction of context usage at which to trigger context compression (e.g. 0.2, 0.3). | `0.5`       |
| Disable Loop Detection        | `model.disableLoopDetection` | Disable automatic detection and prevention of infinite loops.                          | `false`     |
| Skip Next Speaker Check       | `model.skipNextSpeakerCheck` | Skip the next speaker check.                                                           | `true`      |