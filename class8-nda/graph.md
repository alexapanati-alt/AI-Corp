# Run: Class 8 Follow-Up — Starbucks/Lipton NDA

The orchestrator (the main Claude Code session) reads this file to run the graph. Ask: *"Run Exercise N in `class8-nda/graph.md`."*

## What the graph does and doesn't do

The assignment has to be done **in the Class AI Tools**: Harvey or Legora, and Gemini. Claude can't run those tools, and the graph never writes text that stands in for their output. It splits the work this way:

| You (human steps H1–H5) | The graph |
|---|---|
| Put the class documents in `inputs/` | Checks the inputs are present and are the right documents |
| Paste the prompt from `prompts/` into each tool | Supplies the paste-ready prompt and lists exactly what to upload |
| Save each tool's complete output, plus time and platform, in `tool-outputs/` | Reviews every output (R nodes): defined terms, cross-references, consistency, fidelity to the precedent, citations |
| Read the drafts critically, correct them and make them yours | Drafts the evaluation, deviation memo, cover sheet and discussion notes for you to check and revise |

The evaluations are **drafts for your review**. The assignment grades your judgment about the AI outputs, so read each finding against the documents before you submit it.

## Exercise pipeline

Exercises run in sequence because each one feeds the next: Ex 2 uploads the NDA you pick from Ex 1, and Ex 3 uploads the one you pick from Ex 2. Within an exercise, review nodes run in parallel, one per tool.

```
H1 inputs ─> H(N) run prompts/exN in each tool, save to tool-outputs/
                      │
                      ├─> R(N)-harvey|legora ┐  (parallel; nda-reviewer)
                      ├─> R(N)-gemini        ┤
                      └─> V3 (Ex 3 only)     ┘  (researcher: diligence-claim check)
                                             │
                                  O(N) orchestrator ─> exN-evaluation.md + exN-cover.md
```

## Nodes

| ID | Agent | Scope (passed in the task) | Reads | Writes |
|---|---|---|---|---|
| G | orchestrator | **Input gate.** Confirm each required file for the exercise exists in `inputs/` and `tool-outputs/`, and skim each to confirm it's the right document (e.g. the markup really is Target's markup of the Pubco draft). Stop and list what's missing. Then convert every `.docx`/`.pdf` input and tool output to plain text with `pandoc -t plain` or `pdftotext -layout`, so nodes without Bash (V3) can read them. | `inputs/`, `tool-outputs/` | `inputs/text/*.txt` |
| R1-*tool* | `nda-reviewer` | Mode `ungrounded-eval`, one node per tool. | `tool-outputs/ex1-<tool>*`, `inputs/deal-description.*` | `r1-<tool>.md` |
| O1 | orchestrator | Draft the Ex 1 evaluation answering the assignment's five questions: (1) material differences between tools; (2) omitted or inadequate protections, by tool; (3) aggressive, unrealistic, inconsistent or unsupported provisions; (4) whether each memo accurately explains its NDA; (5) at least five reasons not to rely on the output without precedent-based and lawyer review. **Recommend which AI Generated NDA to carry into Ex 2**, and why. | `r1-*.md` | `ex1-evaluation.md` |
| R2-*tool* | `nda-reviewer` | Mode `deviation`, one node per tool. Compare the precedent, the selected Ex 1 NDA and that tool's Grounded NDA. | `tool-outputs/ex2-<tool>*`, the selected `tool-outputs/ex1-*`, `inputs/precedent-nda.*` | `r2-<tool>.md` |
| O2 | orchestrator | Draft the **internal source-and-deviation memorandum** the assignment requires: provision · precedent · selected AI NDA · Grounded NDA · reason; then every unexplained departure, new AI provision, inaccurate defined term, broken cross-reference and inconsistency. **Recommend which Grounded NDA to carry into Ex 3.** | `r2-*.md` | `ex2-source-and-deviation-memo.md` |
| V3 | `researcher` | **Diligence-claim check.** List the factual claims in the diligence file that the Ex 3 outputs rely on (ownership of Lipton Teas and Infusions, markets, regulators, competitors, employees, IP, supply chain), and verify each against public primary sources. *Not in scope:* NDA drafting. | `inputs/text/diligence-considerations.txt`, `inputs/text/ex3-*.txt` | `v3-diligence-claims.md` |
| R3-*tool* | `nda-reviewer` | Mode `diligence-eval`, one node per tool. First generate an independent redline: `python3 tools/redline.py <Grounded NDA> tool-outputs/ex3-<tool>-nda.* -o class8-nda/ex3-<tool>-redline.html`. | `tool-outputs/ex3-<tool>*`, selected `ex2-*`, `inputs/diligence-considerations.*` | `r3-<tool>.md`, `ex3-<tool>-redline.html` |
| O3 | orchestrator | Draft the Ex 3 evaluation: for each proposed NDA change, whether the uploaded materials support it (apply V3's verdicts), whether the drafting does what it claims, and whether it belongs elsewhere in the deal process. Note where the tool's own redline differs from the independent one. | `r3-*.md`, `v3-diligence-claims.md` | `ex3-evaluation.md` |
| R4 | `nda-reviewer` | Mode `workflow-audit`. First run `python3 tools/redline.py inputs/pubco-draft-nda.* inputs/target-markup.* -o class8-nda/ex4-independent-redline.html` and use it to test the tool's Step 1 and Step 3 and the accuracy of `comparison-redline.*`. | `tool-outputs/ex4-*`, all `inputs/` | `r4-<tool>.md`, `ex4-independent-redline.html` |
| O4 | orchestrator | Draft the Ex 4 explanation the assignment requires: whether the workflow was saved or one-time; every step the tool failed to follow; every material error or omission; and a blank list for the student's corrections. Flag that the assignment says "eight Required Outputs" but lists six. | `r4-*.md` | `ex4-evaluation.md` |
| R5 | `nda-reviewer` | Mode `workflow-audit`, applied to the Harvey table: check each row's cite, Target change and recommended language against the inputs and against R4's findings. | `tool-outputs/ex5-harvey*`, `r4-*.md`, `inputs/` | `r5-harvey.md` |
| D | orchestrator | **Discussion prep.** Bullet answers to the six class discussion questions, grounded in the evaluations above. Run after Ex 4 (or Ex 5). | all `ex*-evaluation.md`, `ex2-source-and-deviation-memo.md` | `discussion-prep.md` |

**Edges:**
- G runs first for every exercise. If anything is missing it stops: no review runs on a missing or placeholder output.
- R nodes for the same exercise start in parallel (and V3 alongside R3 in Ex 3).
- O(N) waits for every R and V node in its exercise.
- Ex N+1 can't start until the student has picked the NDA to carry forward from Ex N (O1 and O2 recommend one).
- D runs once, after the last exercise the student completes.

## Cover sheet (every exercise)

O(N) also writes `exN-cover.md`, one block per tool, with the fields Instruction 1 requires. Fields it can't know are left as `[STUDENT TO COMPLETE]`, never guessed:

```
Exercise: N · Class AI Tool: <tool> · Platform/feature: <from .meta.md>
Documents uploaded: <file list>
Prompt or saved workflow: prompts/exN.md (verbatim | with enhancements listed)
Complete output: tool-outputs/exN-<tool>.*
Approximate time: <from .meta.md, else [STUDENT TO COMPLETE]>
Material corrections or revisions by me: [STUDENT TO COMPLETE]
```

## Run log

| Date | Step | Result |
|---|---|---|
| — | — | Not yet run. |
