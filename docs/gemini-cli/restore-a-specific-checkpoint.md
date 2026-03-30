### Restore a specific checkpoint

To restore your project to a specific checkpoint, use the checkpoint file from
the list:

```
/restore <checkpoint_file>
```

For example:

```
/restore 2025-06-22T10-00-00_000Z-my-file.txt-write_file
```

After running the command, your files and conversation will be immediately
restored to the state they were in when the checkpoint was created, and the
original tool prompt will reappear.