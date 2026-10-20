# Graph: Delaware's approach to AI corporations

## Nodes

| ID | Agent | Input | Output (state) |
|---|---|---|---|
| A | `statutes-researcher` | The question | `state/node_a_statutes.md` |
| B | `llc-researcher` | The question | `state/node_b_llc.md` |
| C | `courts-researcher` | The question | `state/node_c_courts.md` |
| V | `aic-verifier` | AIC claims flagged by A | `state/node_v_aic_verification.md` |
| D | Synthesizer (orchestrator) | All state files | `REPORT.md` |

## Edges

```
START ──┬──> A ──┐
        ├──> B ──┼──> GATE ──(AIC claims unverified?)──yes──> V ──> D ──> END
        └──> C ──┘                                   └──no───────> D
```

## State rules

- Each node writes **only its own file**, so nodes running in parallel never overwrite each other.
- A node reads another node's file only along an edge. V reads A's AIC section; D reads everything.
- Every file separates *verified* claims from *uncertain* ones. The gate's decision depends on that split.

## Run log (2026-10-20)

| Step | What happened |
|---|---|
| 1. Fan-out | A, B and C launched in parallel. Each used about 60–68k tokens and took 1–2 minutes; wall time was set by the slowest (A, about 99s). |
| 2. Fan-in | All three finished. B corrected a premise in its task (Utah's DAO Act passed in 2023, not 2024). |
| 3. Gate | A flagged the proposed AIC as **not verified**: no bill text, no bill number, and conflicting dates. The gate routed to V. |
| 4. V | aic-verifier checked eight claims (about 83k tokens, 144s). Result: 3 confirmed, 3 supported, 1 partly wrong (the liability-shield conditions) and 1 that named the wrong drafting body (it was the AI Commission's Sandbox Subcommittee, not the Corporation Law Council). The proxy blocked direct page fetches, so the verdicts rest on search excerpts of primary sources. → `state/node_v_aic_verification.md` |
| 5. D | The synthesizer resolved an apparent conflict: B said Delaware has no algorithmic-entity statute, while A found the AIC. Both are true, because the AIC is a proposal, not enacted law. → `REPORT.md` |
