# Run: Delaware's approach to AI corporations

The orchestrator reads this file to run the graph. The general flow is drawn in the [README diagram](../README.md#architecture); this file holds what's specific to this run.

## Nodes

| ID | Agent | Scope (passed in the task) | Writes |
|---|---|---|---|
| A | `researcher` | **Delaware corporate statutes (DGCL):** whether an AI can be a director (§141(b)), officer (§142) or incorporator (§§101/103/107); delegation under §141(a) and reliance under §141(e); SB 21 and later amendments; AI-specific bills. *Not in scope:* LLCs, case law. | `a-statutes.md` |
| B | `researcher` | **LLC Act and autonomous entities:** §18-1101 freedom of contract, §18-801 memberless dissolution, the Bayern and LoPucki debate, and comparison with the Wyoming, Utah and Tennessee DAO laws. *Not in scope:* the DGCL, case law. | `b-llc.md` |
| C | `researcher` | **Courts and fiduciary duty:** Caremark and Marchand applied to AI risk; litigation over AI-company governance from 2023 on (say when a case is not in Delaware); public benefit corporations (§§361–368). *Not in scope:* statute text, LLCs. | `c-courts.md` |
| V | `aic-verifier` | **The claims A flagged** about the proposed Artificial Intelligence Company (AIC), read from `a-statutes.md` | `v-aic-verification.md` |
| D | orchestrator | Reads every notes file, resolves conflicts and writes the report | `report.md` |

**Edges:**
- A, B and C start in parallel.
- When all three are done, the gate checks whether any notes are flagged **Not verified** about the AIC.
- If they are, V runs and then D. If not, D runs directly.

## Run log (2026-10-20)

| Step | Result |
|---|---|
| A, B, C in parallel | Each used about 60–68k tokens and took 1–2 minutes; wall time was about 99s, set by the slowest node. B corrected a premise in its task (Utah's DAO Act passed in 2023, not 2024). |
| Gate | A flagged the AIC as not verified: no bill text, no bill number, conflicting dates. The gate routed to V. |
| V | About 83k tokens and 144s for eight claims: 3 confirmed, 3 supported, 1 partly wrong (the liability-shield conditions), 1 naming the wrong drafting body (it was the AI Commission's Sandbox Subcommittee, not the Corporation Law Council). The proxy blocked direct page fetches, so the verdicts rest on search excerpts. |
| D | Resolved an apparent conflict: B said Delaware has no algorithmic-entity statute, while A found the AIC. Both are true, because the AIC is a draft, not law. Applied V's corrections to `report.md`. |
