### Configuration schema

| Field              | Type    | Required | Description                                                                                |
| :----------------- | :------ | :------- | :----------------------------------------------------------------------------------------- |
| `enabled`          | boolean | Yes      | Must be `true` to enable the feature.                                                      |
| `classifier`       | object  | Yes      | The configuration for the local model endpoint. It includes the host and model specifiers. |
| `classifier.host`  | string  | Yes      | The URL to the local model server. Should be `http://localhost:<port>`.                    |
| `classifier.model` | string  | Yes      | The model name to use for decisions. Must be `"gemma3-1b-gpu-custom"`.                     |

> **Note: You will need to restart after configuration changes for local model
> routing to take effect.**