### Debug mode

```bash
DEBUG=1 gemini -s -p "debug command"
```

<!-- prettier-ignore -->
> [!NOTE]
> If you have `DEBUG=true` in a project's `.env` file, it won't affect
> gemini-cli due to automatic exclusion. Use `.gemini/.env` files for
> gemini-cli specific debug settings.