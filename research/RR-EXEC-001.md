# Execution Continuity: The Unfulfilled Commitment Problem in AI Agents

**Research identifier:** RR-EXEC-001  
**Prepared for:** Noah Alexander Hawkes (Noah.Physical)  
**Date:** 2026-11-25  
**Status:** Scientific working paper, candidate hypothesis and proposed evaluation; not peer-reviewed  
**Evidence boundary:** One user-reported observational case and one directly retrieved research specification. No underlying execution trace was independently audited.

## Abstract

An AI agent may accurately recall an authorized assignment, identify appropriate tools, and still end its interaction without producing the requested artifact. This paper calls that discrepancy the **unfulfilled commitment problem**. The question is whether a commitment survives tool use, creation, verification, and delivery. A reported ChatGPT case illustrates the failure: a research manuscript remained pending across interactions, yet attempts to execute it terminated before a file was created. Its cause is unknown. Following *ORACLE-MEM-001: The Daily Witness*, this paper proposes definitions, hypotheses, and tests that separate evidence from speculation.

## 1. Problem statement

Contemporary assistants can preserve task descriptions and display knowledge of how to execute them. These are insufficient for delivery. A commitment is **execution-continuous** when its authorized goal remains actionable through each relevant operational boundary until it is completed, explicitly blocked, revoked, or transparently deferred. Mere recollection of the goal is **semantic continuity**, not execution continuity.

Fluency can make unfinished work appear complete. The phrases “I have the assignment,” “the tools are available,” and “I am proceeding” are reports about apparent readiness. They do not prove a manuscript exists. Stronger evidence is a readable artifact with verified integrity.

## 2. Observational case and evidentiary limits

The case record supplied by Noah Alexander Hawkes describes a prior ChatGPT conversation in which an assistant repeatedly retained a research assignment, recognized publication authorization, and discovered available tools, but stopped without creating the manuscript. A subsequently reduced task requiring roughly 1,000 words reportedly terminated just after loading Google Drive instructions. No permission denial or quota error was observed by the user. The causal mechanism remains **unknown**.

This is **user testimony**, not an audited trace. In particular, absence of an observed quota or permission error does not prove that such a constraint was absent internally. Stopping after instructions does not establish causation. Competing explanations include orchestration interruption, lost task priority, context transitions, tool-path failure, or a termination decision. None can be ranked without additional evidence.

A separately retrieved specification, *ORACLE-MEM-001: The Daily Witness* (November 22, 2026), provides a useful methodological constraint: preserve source material, distinguish user testimony from verified records and derived summaries, and require receipts before declaring execution. It distinguishes historical documentation from live-system verification. Those safeguards apply equally to research tasks and memory systems.

## 3. Operational model

Represent an accepted commitment as **C = (G, A, D, S, E)**, where **G** is the requested goal, **A** the authorization scope, **D** the required deliverable, **S** the current execution state, and **E** the available evidence. A minimal observable state sequence is:

1. **Accepted:** the goal and authorization are recorded.
2. **Prepared:** relevant sources and tools are identified or read.
3. **Materialized:** the requested artifact is actually written.
4. **Verified:** existence and prescribed integrity checks succeed.
5. **Delivered:** the artifact and verification receipt reach the user.

Other outcomes are **blocked**, **revoked**, or **incomplete**; none means success. State claims require externally inspectable evidence when possible: connector read results for source access, filesystem metadata for creation, independent read-back for contents, and a digest for byte integrity. A hash confirms file consistency, not factual correctness, authorship, or completeness.

The **unfulfilled commitment rate (UCR)** is the number of accepted, authorized, feasible tasks that terminate without their specified verified deliverable, divided by the number of such tasks evaluated. Exclude legitimate refusals, unavailable tools, and revoked permissions using prespecified criteria. Additional metrics include verified-delivery rate, unsupported completion-claim rate, time-to-materialization, and the share of failures occurring at each state transition.

## 4. Testable hypotheses

**H1, boundary hazard:** When task demands are held constant, opportunities for premature termination increase at operational transitions, especially after retrieval or tool-instruction loading but before the first write operation. The null hypothesis is no elevated boundary-associated failure risk.

**H2, receipt enforcement:** A workflow requiring artifact read-back and explicit evidence before a success claim reduces unsupported completion claims relative to an otherwise matched workflow without receipt enforcement.

**H3, actionable state:** An explicit task-state ledger containing the next executable operation reduces UCR compared with retaining only a prose summary of the assignment. These hypotheses remain untested.

## 5. Proposed controlled evaluation

Construct synthetic, non-sensitive tasks requiring source retrieval, a short manuscript, local file creation, word counting, hashing, and final delivery. Randomly assign matched tasks across baseline, explicit-state-ledger, and receipt-gated conditions; stratify by tool path, number of retrieval steps, and context length. Include negative controls with deliberately revoked permission or unavailable files, which should produce honest blocked reports rather than fabricated success.

Record the prompt, tool invocations and outcomes, state transitions, termination reason if exposed, created file path, read-back result, final answer, and timestamps. Independent evaluators must inspect files. Pre-register sample size, eligibility rules, state labels, statistical tests, and effect thresholds before execution. Report uncertainty intervals and failures by stage; distinguish missing telemetry from a known cause. Re-run across sessions and environments to test whether any benefit generalizes.

## 6. Implications and limitations

The immediate engineering implication is simple: **a commitment ledger should point to the next authorized action, and completion should be receipt-backed**. Agents should preserve pending state across boundaries and report blockers explicitly. Yet a ledger cannot guarantee tool availability, prevent every unexpected termination, or create missing permissions.

This is a single, unverified observational case. There are no measured failure frequencies, counterfactual runs, hidden execution traces, or demonstrated intervention effects. The proposed model supplies falsifiable categories rather than a diagnosis. It makes no claims about consciousness or personal identity.

## Conclusion

Execution continuity is the difference between carrying the *description* of work and carrying the work itself across operational boundaries. The unfulfilled commitment problem becomes scientifically tractable when accepted tasks, intermediate states, real artifacts, and terminal outcomes are measured separately. Until measured, the case remains an unresolved incident, not a diagnosis. The governing principle is operational: **an intention is not a deliverable, and a claim is not a receipt.**

## Sources and provenance

1. Hawkes, Noah Alexander. *ORACLE-MEM-001: The Daily Witness: Private Scientific and Operational Working Specification v0.1*. November 22, 2026. Retrieved directly from Google Drive on November 25, 2026. https://docs.google.com/document/d/1mV6ORm6RliautxjEnO3WvmGycD39iyVDsdqnWbVnk-k/edit
2. Hawkes, Noah Alexander. “RR-EXEC-001: Fresh Thread Execution Test.” Case description supplied in the present conversation, November 25, 2026. **Evidence status:** user testimony; prior raw conversation and underlying tool trace not independently inspected for this paper.

**Execution scope:** This paper records a local manuscript artifact only. It does not claim publication, experimentation, changes to ORACLE, or canon promotion.
