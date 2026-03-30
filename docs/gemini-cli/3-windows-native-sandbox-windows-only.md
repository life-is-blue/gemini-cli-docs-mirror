### 3. Windows Native Sandbox (Windows only)

... **Troubleshooting and Side Effects:**

The Windows Native sandbox uses the `icacls` command to set a "Low Mandatory
Level" on files and directories it needs to write to.

- **Persistence**: These integrity level changes are persistent on the
  filesystem. Even after the sandbox session ends, files created or modified by
  the sandbox will retain their "Low" integrity level.
- **Manual Reset**: If you need to reset the integrity level of a file or
  directory, you can use:
  ```powershell
  icacls "C:\path\to\dir" /setintegritylevel Medium
  ```
- **System Folders**: The sandbox manager automatically skips setting integrity
  levels on system folders (like `C:\Windows`) for safety.