## Technical behavior

- **Confirmation:** Triggers a confirmation dialog showing the converted URLs.
- **Processing:** Uses the Gemini API's `urlContext` for retrieval.
- **Fallback:** If API access fails, the tool attempts to fetch raw content
  directly from your local machine.
- **Formatting:** Returns a synthesized response with source attribution.