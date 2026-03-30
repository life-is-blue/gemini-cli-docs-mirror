### File system proxy

ACP includes a proxied file system service. This means that when the agent needs
to read or write files, it does so through the ACP client. This is a security
feature that ensures the agent only has access to the files that the client (and
by extension, the user) has explicitly allowed.