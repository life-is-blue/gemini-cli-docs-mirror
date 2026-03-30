### Referencing resources in a conversation

You can use the same `@` syntax already known for referencing local files:

```
@server://resource/path
```

Resource URIs appear in the completion menu together with filesystem paths. When
you submit the message, the CLI calls `resources/read` and injects the content
in the conversation.