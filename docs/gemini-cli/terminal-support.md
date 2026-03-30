### Terminal support

The CLI uses the OSC 9 terminal escape sequence to trigger system notifications.
This is supported by several modern terminal emulators including iTerm2,
WezTerm, Ghostty, and Kitty. If your terminal does not support OSC 9
notifications, Gemini CLI falls back to a terminal bell (BEL) to get your
attention. Most terminals respond to BEL with a taskbar flash or system alert
sound.