### macOS Seatbelt profiles

Built-in profiles (set via `SEATBELT_PROFILE` env var):

- `permissive-open` (default): Write restrictions, network allowed
- `permissive-proxied`: Write restrictions, network via proxy
- `restrictive-open`: Strict restrictions, network allowed
- `restrictive-proxied`: Strict restrictions, network via proxy
- `strict-open`: Read and write restrictions, network allowed
- `strict-proxied`: Read and write restrictions, network via proxy