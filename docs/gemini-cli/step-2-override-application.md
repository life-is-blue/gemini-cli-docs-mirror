### Step 2: Override Application

The system evaluates the `overrides` list against the request context (`model`
and `overrideScope`).

1.  **Filtering**: All matching overrides are identified.
2.  **Sorting**: Matches are prioritized by **specificity** (the number of
    matched keys in the `match` object).
    - Specific matches (e.g., `model` + `overrideScope`) override broad matches
      (e.g., `model` only).
    - Tie-breaking: If specificity is equal, the order of definition in the
      `overrides` array is preserved (last one wins).
3.  **Merging**: The configurations from the sorted overrides are merged
    sequentially onto the base configuration.