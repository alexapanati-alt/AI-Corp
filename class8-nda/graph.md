# Run: Class 8 Follow-Up — Starbucks/Lipton NDA

The orchestrator (the main Claude Code session) reads this file to run the graph. Ask: *"Run Exercise N in `class8-nda/graph.md`."*

## What the graph does and doesn't do

The graph does every part of the assignment, judgment included, and the student reviews and revises the result before submitting. The one exception: the NDAs, memos and workflow outputs themselves must come **from the Class AI Tools** (Harvey or Legora, and Gemini), because the submission must name the tool that produced them. The graph never writes text that stands in for a tool's output.

| Step | Who |
|---|---|
| Put the class documents in `inputs/` | Student |
| Run `prompts/exN` in each tool and save the complete output to `tool-outputs/` | Student, or Claude via a browser connection (Claude in Chrome or the desktop app's built-in browser) if one is attached and course rules allow it |
| Review every output (R nodes) | Graph |
| Write the complete, submission-ready evaluations, deviation memo, corrected outputs, correction logs, cover sheets and discussion answers (O and D nodes) | Graph |
| Choose which NDA to carry into the next exercise | Graph, unless the student overrides |
| Read everything, revise, and submit | Student |

Write each deliverable as finished work in the student's voice ("I", the associate), not as notes or a draft with placeholders. Mark only what genuinely can't be known (e.g. minutes spent, if no `.meta.md` exists).

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
| O1 | orchestrator | Draft the Ex 1 evaluation answering the assignment's five questions: (1) material differences between tools; (2) omitted or inadequate protections, by tool; (3) aggressive, unrealistic, inconsistent or unsupported provisions; (4) whether each memo accurately explains its NDA; (5) at least five reasons not to rely on the output without precedent-based and lawyer review. **Select the AI Generated NDA to carry into Ex 2**, and explain why. Write the corrected outputs and correction log (see below). | `r1-*.md` | `ex1-evaluation.md`, `ex1-<tool>-corrected.md`, `ex1-cover.md` |
| R2-*tool* | `nda-reviewer` | Mode `deviation`, one node per tool. Compare the precedent, the selected Ex 1 NDA and that tool's Grounded NDA. | `tool-outputs/ex2-<tool>*`, the selected `tool-outputs/ex1-*`, `inputs/precedent-nda.*` | `r2-<tool>.md` |
| O2 | orchestrator | Draft the **internal source-and-deviation memorandum** the assignment requires: provision · precedent · selected AI NDA · Grounded NDA · reason; then every unexplained departure, new AI provision, inaccurate defined term, broken cross-reference and inconsistency. **Select the Grounded NDA to carry into Ex 3.** Write the corrected outputs and correction log. | `r2-*.md` | `ex2-source-and-deviation-memo.md`, `ex2-evaluation.md`, `ex2-<tool>-corrected.md`, `ex2-cover.md` |
| V3 | `researcher` | **Diligence-claim check.** List the factual claims in the diligence file that the Ex 3 outputs rely on (ownership of Lipton Teas and Infusions, markets, regulators, competitors, employees, IP, supply chain), and verify each against public primary sources. *Not in scope:* NDA drafting. | `inputs/text/diligence-considerations.txt`, `inputs/text/ex3-*.txt` | `v3-diligence-claims.md` |
| R3-*tool* | `nda-reviewer` | Mode `diligence-eval`, one node per tool. First generate an independent redline: `python3 tools/redline.py <Grounded NDA> tool-outputs/ex3-<tool>-nda.* -o class8-nda/ex3-<tool>-redline.html`. | `tool-outputs/ex3-<tool>*`, selected `ex2-*`, `inputs/diligence-considerations.*` | `r3-<tool>.md`, `ex3-<tool>-redline.html` |
| O3 | orchestrator | Draft the Ex 3 evaluation: for each proposed NDA change, whether the uploaded materials support it (apply V3's verdicts), whether the drafting does what it claims, and whether it belongs elsewhere in the deal process. Note where the tool's own redline differs from the independent one. Write the corrected outputs and correction log. | `r3-*.md`, `v3-diligence-claims.md` | `ex3-evaluation.md`, `ex3-<tool>-corrected.md`, `ex3-cover.md` |
| R4 | `nda-reviewer` | Mode `workflow-audit`. First run `python3 tools/redline.py inputs/pubco-draft-nda.* inputs/target-markup.* -o class8-nda/ex4-independent-redline.html` and use it to test the tool's Step 1 and Step 3 and the accuracy of `comparison-redline.*`. | `tool-outputs/ex4-*`, all `inputs/` | `r4-<tool>.md`, `ex4-independent-redline.html` |
| O4 | orchestrator | Draft the Ex 4 explanation the assignment requires: whether the workflow was saved or one-time; every step the tool failed to follow; every material error or omission; and every correction made. Flag that the assignment says "eight Required Outputs" but lists six. Write corrected versions of the six Required Outputs. | `r4-*.md` | `ex4-evaluation.md`, `ex4-<tool>-corrected.md`, `ex4-cover.md` |
| R5 | `nda-reviewer` | Mode `workflow-audit`, applied to the Harvey table: check each row's cite, Target change and recommended language against the inputs and against R4's findings. | `tool-outputs/ex5-harvey*`, `r4-*.md`, `inputs/` | `r5-harvey.md` |
| O5 | orchestrator | Write the corrected table and cover sheet. | `r5-harvey.md` | `ex5-harvey-corrected.md`, `ex5-cover.md` |
| D | orchestrator | **Discussion prep.** Answers to the six class discussion questions, with a clear position on each,, grounded in the evaluations above. Run after Ex 4 (or Ex 5). | all `ex*-evaluation.md`, `ex2-source-and-deviation-memo.md` | `discussion-prep.md` |

**Edges:**
- G runs first for every exercise. If anything is missing it stops: no review runs on a missing or placeholder output.
- R nodes for the same exercise start in parallel (and V3 alongside R3 in Ex 3).
- O(N) waits for every R and V node in its exercise.
- Ex N+1 uses the NDA that O1 or O2 selected, unless the student names a different one.
- D runs once, after the last exercise the student completes.

## Corrected outputs and correction log

The assignment asks for "any material correction or revision made by you". For each tool output, O(N) writes `exN-<tool>-corrected.md`: the tool's output with every High and Medium reviewer finding fixed, and a numbered correction log at the end (section · what the tool wrote · correction · reason). The original in `tool-outputs/` stays untouched, so the submission can show both.

## Cover sheet (every exercise)

O(N) also writes `exN-cover.md`, one block per tool, with the fields Instruction 1 requires. Only facts the graph can't know (minutes spent, if no `.meta.md` exists) are marked `[STUDENT TO COMPLETE]`:

```
Exercise: N · Class AI Tool: <tool> · Platform/feature: <from .meta.md>
Documents uploaded: <file list>
Prompt or saved workflow: prompts/exN.md (verbatim | with enhancements listed)
Complete output: tool-outputs/exN-<tool>.*
Approximate time: <from .meta.md, else [STUDENT TO COMPLETE]>
Material corrections or revisions by me: <summary of the correction log, with a pointer to exN-<tool>-corrected.md>
```

## Run log

| Date | Step | Result |
|---|---|---|
| — | — | Not yet run. |
