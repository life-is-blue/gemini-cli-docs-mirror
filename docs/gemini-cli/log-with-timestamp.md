# Log with timestamp
log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

input=$(cat)
log "Received input: ${input:0:100}..."