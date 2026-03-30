### Common issues and solutions

#### Server won't connect

**Symptoms:** Server shows `DISCONNECTED` status

**Troubleshooting:**

1. **Check configuration:** Verify `command`, `args`, and `cwd` are correct
2. **Test manually:** Run the server command directly to ensure it works
3. **Check dependencies:** Ensure all required packages are installed
4. **Review logs:** Look for error messages in the CLI output
5. **Verify permissions:** Ensure the CLI can execute the server command

#### No tools discovered

**Symptoms:** Server connects but no tools are available

**Troubleshooting:**

1. **Verify tool registration:** Ensure your server actually registers tools
2. **Check MCP protocol:** Confirm your server implements the MCP tool listing
   correctly
3. **Review server logs:** Check stderr output for server-side errors
4. **Test tool listing:** Manually test your server's tool discovery endpoint

#### Tools not executing

**Symptoms:** Tools are discovered but fail during execution

**Troubleshooting:**

1. **Parameter validation:** Ensure your tool accepts the expected parameters
2. **Schema compatibility:** Verify your input schemas are valid JSON Schema
3. **Error handling:** Check if your tool is throwing unhandled exceptions
4. **Timeout issues:** Consider increasing the `timeout` setting

#### Sandbox compatibility

**Symptoms:** MCP servers fail when sandboxing is enabled

**Solutions:**

1. **Docker-based servers:** Use Docker containers that include all dependencies
2. **Path accessibility:** Ensure server executables are available in the
   sandbox
3. **Network access:** Configure sandbox to allow necessary network connections
4. **Environment variables:** Verify required environment variables are passed
   through