# Guide: building a multi-agent research graph

How this project was built, and what each step shows. The architecture diagram is in the [README](README.md); the details of this run are in [`delaware-ai-corps/graph.md`](delaware-ai-corps/graph.md).

## 1. The three concepts

| Concept | What it is here | In a framework like LangGraph |
|---|---|---|
| **Node** | One agent with a narrow job: researcher A, B or C, verifier V, or orchestrator D | A function that reads state and returns an update to it |
| **State** | Notes files, one per node, all in the run's folder | A typed state object; when nodes run in parallel, "reducers" merge their updates |
| **Edge** | The order nodes run in, written in `graph.md` and carried out by the orchestrator | `add_edge` for a fixed next step, `add_conditional_edges` for a branch |

Each node starts fresh: it knows only its own prompt, not the conversation it came from. That's why every task spells out the scope, what to deliver and the rules for evidence.

## 2. Edge types used in this run

```
Question ──┬─> A ─┐
           ├─> B ─┼─> Gate: anything flagged "Not verified"? ──yes─> V ─> D ─> report.md
           └─> C ─┘                                         └─no──────> D
```

| Edge | Where | Meaning |
|---|---|---|
| **Fan-out** | Question → A, B, C | A, B and C don't depend on each other, so all three start in the same step. Wall time equals the slowest node, not the sum of all three. |
| **Fan-in** | A, B, C → Gate | Nothing past this point runs until all three are finished. Each agent sends a completion notice when it's done. |
| **Conditional** | Gate → V | V runs only if a node flagged claims as **Not verified**. |
| **Sequential** | V → D → report | The final write-up waits for verification. |

## 3. Rules of thumb for splitting work

1. **Split by independence.** If two subtasks need each other's results, connect them in sequence. Otherwise, run them in parallel.
2. **Give each node a clear boundary.** Every scope says what's out of scope, so nodes running in parallel don't overlap.
3. **Each node writes only its own state file.** Nodes running in parallel never overwrite each other.
4. **Keep outputs small and structured,** about 500 words with sources. This keeps the orchestrator's context lean.
5. **Put judgment in one place.** Merging results, resolving conflicts and drawing the final conclusion all happen in the orchestrator.
6. **Make uncertainty explicit.** Every node separates *Verified* from *Uncertain*. The gate depends on that label, so without it a conditional edge has nothing to route on.
7. **One shared definition for nodes that work the same way, a separate file for a specialist.** The researchers share `researcher.md`, and each node's scope is a row in `graph.md`. The verifier works differently, so it has its own file.

## 4. How the run went

| Step | Outcome | What it shows |
|---|---|---|
| A, B, C run in parallel | About 60–68k tokens each, about 99s of wall time in total | Running in parallel cost only as much time as the slowest node |
| B's premise check | Corrected a wrong year in its own task: Utah's DAO Act passed in 2023, not 2024 | Asking nodes to correct their premises catches errors the orchestrator introduced |
| Fan-in conflict | B said "no Delaware algorithmic-entity statute", while A found the AIC | Only the orchestrator sees every file at once. Both claims were true, because the AIC is a draft. |
| Gate → V | Of A's eight AIC claims, V found 3 confirmed, 3 supported, 1 partly wrong and 1 naming the wrong body | **The claims that sounded most specific were the ones with errors.** The gate caught them before they reached the report. |
| V's limitation | The proxy blocked direct page fetches, so V worked from search excerpts | V reported this limitation instead of hiding it. The next step would be to give V the full draft bill. |

## 5. Evolution of the repository

1. **v1:** one agent file per node, plus `research/<topic>/state/`. Clear, but the three researcher files repeated the same rules, and the README and `GRAPH.md` described the flow twice.
2. **v2 (current):** one shared `researcher.md`, with each node's scope in `graph.md`, and one flat folder per run. That cut the repository from 11 files to 9 and from 5 folders to 2, and nothing is described twice.

## 6. Reusing it

1. Copy `delaware-ai-corps/graph.md` into a new folder, such as `wyoming-dao/`, and rewrite each node's scope.
2. If a different kind of claim needs dedicated checking, add a new specialist file in `.claude/agents/`, using `aic-verifier.md` as the template.
3. In Claude Code, ask: *"Run the graph in `<folder>/graph.md`."*
