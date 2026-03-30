# Create test input
@"
{
  "session_id": "test-123",
  "cwd": "C:\\temp\\test",
  "hook_event_name": "BeforeTool",
  "tool_name": "write_file",
  "tool_input": {
    "file_path": "test.txt",
    "content": "Test content"
  }
}
"@ | Out-File -FilePath test-input.json -Encoding utf8