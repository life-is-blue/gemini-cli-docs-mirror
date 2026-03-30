# Don't run as root
if [ "$EUID" -eq 0 ]; then
  echo "Hook should not run as root" >&2
  exit 1
fi