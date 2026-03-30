# depending on the installation method.
REAL_GEMINI_PATH=$(type -aP gemini | grep -v "^$(type -P gemini)$" | head -n 1)

if [ -z "$REAL_GEMINI_PATH" ]; then
  echo "Error: The original 'gemini' executable was not found." >&2
  exit 1
fi