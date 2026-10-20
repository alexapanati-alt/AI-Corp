# Node B: Delaware LLCs and algorithmic/autonomous entities

## 1. Delaware LLC Act: freedom of contract
**Verified**
- 6 Del. C. §18-1101(b): the Act's policy is "to give the maximum effect to the principle of freedom of contract and to the enforceability of LLC agreements." §18-1101(c) lets an agreement expand, restrict or eliminate fiduciary duties, but not the implied covenant of good faith and fair dealing. https://law.justia.com/codes/delaware/title-6/chapter-18/subchapter-xi/section-18-1101
- §18-801(a)(4): an LLC dissolves when it has no members, unless a member is admitted within 90 days "or such other period as is provided for in the LLC agreement," or in the way the agreement provides. https://law.justia.com/codes/delaware/title-6/chapter-18/subchapter-viii/section-18-801

**Uncertain (statutory reading, not settled law)**
- The Act defines a "manager" as a "person," and "person" covers natural persons and legal entities. It does not cover software. The agreement can probably make an algorithm's outputs binding, for example as a contractual decision rule that human or entity managers must carry out, or through delegation under §18-407. But no source I found says software itself can be a Delaware manager or member. No Delaware case or statute addresses AI management.
- Accountability still runs to persons. The good-faith covenant cannot be waived, so someone remains answerable for bad-faith exercise of discretion.

## 2. The zero-member and algorithmic-entity debate
**Verified**
- Shawn Bayern, "Of Bitcoins, Independently Wealthy Software, and the Zero-Member LLC," 108 Nw. U. L. Rev. 1485 (2014). https://scholarlycommons.law.northwestern.edu/nulr/vol108/iss4/9
- Bayern, "The Implications of Modern Business-Entity Law for the Regulation of Autonomous Systems," 19 Stan. Tech. L. Rev. 93 (2015); also in the Eur. J. Risk Reg. (2016). His method: a member forms an LLC, the operating agreement hands control to an autonomous system, and the member withdraws, leaving a memberless LLC that may last indefinitely. https://law.stanford.edu/publications/the-implications-of-modern-business-entity-law-for-the-regulation-of-autonomous-systems/
- Under RULLCA, the default is dissolution after 90 consecutive days with no members. Bayern points to New York, which allows 180 days or a period set by the agreement, as close to allowing a perpetual memberless entity. https://arxiv.org/pdf/2602.20169 ; https://en.wikipedia.org/wiki/Algorithmic_entities
- Lynn LoPucki, "Algorithmic Entities," 95 Wash. U. L. Rev. 887 (2018), accepts that the structure is feasible. He argues that entities with no human controllers make AI risk much worse, and that charter competition between states makes the problem hard to stop. https://journals.library.wustl.edu/lawreview/article/id/3143/
- Critics, notably Sherer (2018), dispute that the structure is viable under New York law, RULLCA, or case law on personhood. https://en.wikipedia.org/wiki/Algorithmic_entities

**Uncertain**
- Delaware's "such other period as is provided for in the LLC agreement" wording could, on its face, let the agreement set a long or open-ended period, which would fit Bayern's theory. No court has tested this, and an open-ended period could clash with §18-1101 limits and with public policy.

## 3. Comparison with DAO statutes
**Verified**
- **Wyoming DAO Supplement** (SF0038, W.S. 17-31-101 to -116, effective July 1, 2021): the articles may make a DAO LLC "member managed" or "algorithmically managed." An algorithmically managed DAO can form only if its smart contracts can be updated or modified. The articles must give a public identifier for the smart contracts, and they override the operating agreement where the two conflict (§17-31-115). The statute does not define "algorithmically managed." https://www.sheppard.com/insights/blogs/wyoming-decentralized-autonomous-organizations ; https://frostbrowntodd.com/wyoming-paves-way-for-dao-legal-company-status/
- **Utah DAO Act** (HB 357, passed 2023, effective Jan. 1, 2024, Utah Code Title 48, Ch. 5): creates the "LLD," a separate entity type rather than an LLC, based on the COALA model law. It still requires a registered agent and at least one human organizer. https://www.polsinelli.com/polsinelli-bitblog/utah-passes-innovative-dao-legislation
- **Tennessee** (2022, Tenn. Code Ann. 48-250-101 et seq.) largely follows Wyoming. https://www.klgates.com/thought-leadership/Beyond-a-Reasonable-DAOubt-Tennessees-Limited-Liability-Statute-for-Decentralized-Autonomous-Organizations-DAOs-8-4-2022
- **Delaware** has no DAO-specific or "algorithmically managed" statute. Algorithmic control there rests only on contract under §18-1101, with persons still acting as members or managers.

**Uncertain**
- Details of New Hampshire's DAO law and any 2024 to 2026 amendments in Wyoming or Utah were not confirmed.

**Bottom line:** An AI can probably steer a Delaware LLC through its operating agreement, but cannot formally be its member or manager. Wyoming is the only state found that expressly allows "algorithmic management," and even there, humans and registered agents remain in the structure.
