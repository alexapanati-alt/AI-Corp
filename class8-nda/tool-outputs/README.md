# Tool outputs

Save the **complete, unedited** output from each Class AI Tool here, named `ex<N>-<tool>[-nda|-memo].<ext>`, where `<tool>` is `harvey`, `legora` or `gemini`. Examples: `ex1-gemini.docx`, `ex3-harvey-nda.docx`.

Also add a one-line `ex<N>-<tool>.meta.md` per run, so the graph can fill the submission cover sheet:

```text
platform: Harvey · feature: Assistant (Draft) · minutes: 12 · saved workflow: n/a
```

The graph reads these files but never writes to this folder. If you correct a tool's output, save your version separately (e.g. `ex2-harvey-nda.corrected.docx`) so the cover sheet can list the correction.
