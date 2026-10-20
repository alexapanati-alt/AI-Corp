# Delaware's approach to AI corporations

*Synthesized from the node notes in this folder (`a-`, `b-`, `c-` and `v-*.md`). This is research notes, not legal advice. Statutory wording mostly comes from secondary sources.*

## Bottom line

Delaware doesn't let an AI run a company today. In mid-2026, though, it proposed an entity type — the **Artificial Intelligence Company (AIC)** — that would let one, inside a sandbox.

## Current law

| Question | Answer | Node |
|---|---|---|
| Can an AI be a director? | **No.** §141(b) requires a "natural person." | A |
| Officer or incorporator? | The statutes don't say a human is required, but no law or court treats an AI as a legal person, so the accepted view is no. | A |
| Can a board use AI to make decisions? | Yes, as a tool. Under §141(a) the board can't hand over its core decisions or oversight. Whether §141(e) protects directors who rely on AI output is unsettled. | A |
| Can an LLC be run by software? | Probably in practice, not formally. §18-1101 gives wide contract freedom, but software can't be a member or manager, and the good-faith covenant keeps a person accountable. | B |
| Memberless LLC? | Bayern's theory might work under §18-801(a)(4)'s "other period" wording. Nobody has tested it. | B |
| Court rulings on AI oversight? | None yet. *Caremark* / *Marchand* would apply, but only commentary says so far. Musk v. OpenAI was a California federal case. | C |
| How do AI labs use Delaware? | As public benefit corporations: Anthropic, and OpenAI Group PBC. The structure gives directors legal cover to put the mission first, and only holders of at least 2% of shares can sue to enforce it. Delaware's role in OpenAI's recapitalization was the Attorney General's review (no objection, Oct 28, 2025). | C |

## Comparison with other states

Wyoming (2021) expressly allows "algorithmically managed" DAO LLCs. Utah's DAO Act (passed 2023, effective Jan 2024) creates a separate "LLD" entity type that still needs a human organizer. Tennessee (2022) largely follows Wyoming. Delaware has no DAO statute. (Node B)

## The proposed AIC

> **Status: draft bill only, not law.** Node V verified this section (`v-aic-verification.md`). Node V could read only search-engine excerpts of the 36-page draft (dated 06/02/2026), not the full text.

**What it is:** a new entity whose day-to-day operations are run by an AI agent. It would sit in a new **Title 6, Ch. 81** (Artificial Intelligence Company Act), alongside a new **Ch. 80** (Regulatory Sandbox Act). It is neither part of the DGCL nor an amendment to the LLC Act.

**Who made it:**
- The Delaware AI Commission's **Regulatory Sandbox Subcommittee** drafted it. Node A's notes had pointed to the Corporation Law Council, and Node V corrected that.
- The principal drafter is John Mark Zeberkiewicz of Richards Layton & Finger.
- Secretary of State **Charuni Patibanda-Sanchez** and Norm Ai, the "development partner", launched it publicly on July 13–14, 2026. Spotlight Delaware first reported the draft on June 30.

**How it works:**
- **Member:** one person or entity, who must keep the AIC adequately capitalized. The member's liability shield gives way for **underfunding, fraud or willful violation of law**, and applies only inside the sandbox. Node A had described logging and counterparty disclosure as conditions of the shield; they are actually duties of the AIC itself.
- **AIC duties:** keep an activity log of the agent, and tell counterparties that it is a test entity, that the State does not endorse it, when the test ends and how to complain.
- **Gatekeeper:** a four-member committee decides who gets in: the Secretary of State, the Attorney General, the Chief Justice of the Delaware Supreme Court and the chair of the AI Commission. The Secretary of State administers the sandbox.
- **Sandbox length:** 30 months, though sources differ on whether that is the program's lifespan or the application window.
- **Kill switch:** applicants must show they can promptly stop unauthorized agent activity and can terminate the agent.
- **Enforcement:** the committee can suspend or revoke an AIC, or petition the Court of Chancery to dissolve it. Banking is excluded.

**Status and timing:** there is no bill number. The draft was styled for the 153rd General Assembly, which adjourned June 30, 2026, so it must be introduced again in the 154th, expected in January 2027. It grows out of **HJR 7** (signed July 23, 2025).

**Open criticism:**
- "Adequately capitalized" is not defined (Petrin).
- It's unclear who is accountable for what the agent does.
- Other states might not honor the liability shield.
- Norm Ai has a commercial conflict of interest.
