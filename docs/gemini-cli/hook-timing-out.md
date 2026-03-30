### Hook timing out

**Check configured timeout:** The default is 60000ms (1 minute). You can
increase this in `settings.json`:

```json
{
  "name": "slow-hook",
  "timeout": 120000
}
```

**Optimize slow operations:** Move heavy processing to background tasks or use
caching.