## Proxy support

Gemini CLI routes traffic to remote agents through an HTTP/HTTPS proxy if one is
configured. It uses the `general.proxy` setting in your `settings.json` file or
standard environment variables (`HTTP_PROXY`, `HTTPS_PROXY`).

```json
{
  "general": {
    "proxy": "http://my-proxy:8080"
  }
}
```