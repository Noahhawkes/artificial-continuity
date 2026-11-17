# Operation PROMETHEUS: Public Research Accounting and Open Questions
**Date:** 2026-11-16 | **Prepared by:** Reg / ChatGPT | **Authority:** Noah.Physical | **Status:** research record, not canon

## Abstract
PROMETHEUS investigates whether longitudinal human-AI records can preserve documented decisions, corrections, and unfinished commitments across sessions and model changes. It does not claim mind transfer, consciousness, or identity equivalence. The principal outcome is not word count but *decision reconstruction accuracy, provenance fidelity, false-memory rate, and human effort saved on resumption*.

## Project corpus: reported counts
| Measurement | Count | Interpretation |
|---|---:|---|
| Top-level readable project-file words | 14,701,153 | Prior extraction; needs independently archived manifest |
| Readable words in project ZIP | 9,113,695 | Gross ZIP extraction; overlapping files |
| Gross top-level plus ZIP words | 23,814,848 | **Not unique** |
| Exact-file-content deduplicated project words | **19,700,812** | Exact extracted-text hash deduplication only, not passage deduplication |
| Distinct extracted text hashes | 115 | Across counted project-file instances |
| PROMETHEUS v0.1 subset scan | 27 files; 14,599,613 words | Excludes ZIP internals, PDFs, external connectors |

**Cautions:** The 19.7M figure includes AI responses, quoted transmissions, and repeated passages within distinct files. It is neither Noah-authored words nor a two-year prompt count. Native project threads were not independently enumerated. These counts are provisional until extraction methods, manifests, and source hashes are reproduced.

## Other channels, reported but not additive
- **Merlin:** 598,952 words conservatively classified as original composition (583,270 direct plus 15,682 framing); upper bound 943,276; 10,530 structured prompt-record turns; 2,538,274 NOAH-attributed words including 1,594,998 classified transmission. Reported Drive v2 content-unique words: 91,111,026. These are Merlin's claims, not independently reproduced here.
- **Grok:** reported 111,621,465-byte `prod-grok-backend.json`; streaming pattern occurrences: 6,596 `create_time`, 6,456 `message`, 6,256 `_id`; approximately 9,000 user-side markers. **Pattern occurrences are not verified unique conversation/message counts.** Source JSON was not accessed in this run.
- **Lifetime prompts:** hundreds of thousands is Noah's **unverified estimate**, not an observed total.
- **Cross-source addition is invalid** until overlap, authorship, and passage-level deduplication are resolved.

## Executed engineering work, not scientific validation
**v0.1:** Read-only source inventory and hashing, five candidate benchmark keyword searches, and one synthetic supersession fixture. Five candidate records had excerpts located; **zero primary historical ground truths adjudicated; zero real benchmark trials run**. The synthetic governed filter returned the current fixture claim while flat retrieval returned both old and current claims.

**v0.2:** Deterministic evidence gate applied to five source-excerpt candidate records. Unsafe keyword-only rule would promote 5/5; conservative rule promoted 0/5 due to absent source, attribution, temporal, and human-approval verification. Seven code assertions passed. This is a **policy unit test**, not evidence of improved RAG accuracy. The prototype's signoff field is not cryptographically authenticated.

## The Forgotten Conversation: pre-registered candidate protocol
100 candidate items, stratified into 30 corrections, 25 canon/draft collisions, 25 provenance traps, and 20 UNKNOWN probes. Three conditions: A stateless; B flat retrieval; C governed provenance/temporal retrieval. B and C require the same underlying model, matched retrieval-token budgets, and access to the same frozen source universe. Blind scoring should cover factual accuracy, exact source retrieval, correction handling, authority preservation, and uncertainty calibration. Primary-source ground truth must be adjudicated independently and Noah.Physical signoff recorded before the benchmark is frozen. No results are claimed.

## Serious research questions
1. What is the **minimum evidence budget** that predicts held-out decisions better than biographical summaries and flat RAG?
2. Does provenance governance increase accuracy, or does it merely **increase abstention while reducing recall**?
3. Can an AI distinguish a person's *directly expressed belief*, *approved AI-assisted writing*, *pasted transmission*, and *someone else's account activity*?
4. When an original statement is contradicted, what evidence suffices to supersede it, and who has authority?
5. Can correction history transfer between vendors without hidden conversational state?
6. How much **human time** does governed continuity save after an interruption, compared with normal document search?
7. Can a system demonstrate that a task was completed using execution receipts rather than conversational assurances?
8. What are the privacy, consent, deletion, and impersonation risks of a portable human reasoning record?
9. What failures would disconfirm the claim that governed continuity outperforms ordinary retrieval?
10. How should subjective identity claims remain outside the engineering evidence boundary?

## Google Drive inspection
Connected Drive search found native Google Sheets, including **Noah Hawkes Theory Index v0.1** (created May 2026). The sheet's opening rows enumerate theories, evidence types, tiers, and statuses; one visible row has misaligned fields. A November 2026 PROMETHEUS Google Sheet was **not located in the accessible search results**; this is an access/indexing limitation, not proof of nonexistence. No private sheet contents are reproduced here.

## Release boundary
**Public:** methodology, aggregate counts with caveats, synthetic tests, non-identifying code, research questions, and source pointers.
**Not public:** raw transcripts, family/medical/financial information, private filenames, raw evidence excerpts, personally identifying ledger entries, and unsigned adjudication records.

## Next falsifiable milestone
Freeze five dated, speaker-attributed primary records; create blind questions; compare B and C under token parity; publish item-level redacted receipts, recall penalties, and uncertainty. Do not claim novelty or superiority before independent review.

**The human keeps the keys. The system keeps the receipts.**
