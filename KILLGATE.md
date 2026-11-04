# KILLGATE — project #110 `poisoned-skills`

Source paper (context only): arXiv 2610.37738, Manjusha (UIUC) &
Emani (Argonne), "Poisoned Skills: Propagating Jailbreaks Through
Agent Markdown Files", submitted 27 Oct 2026. Its real-model figures
(benign mean ASR 0.5% → injected 44.8%, max 68.9%, stealth 43.4%,
phonetic 30.1%, seven real models) are CONTEXT ONLY and are never
presented as reproduced. All measured numbers in this build come from
the scripted analog in src/, which is a weak proxy for real models;
the writeup says so plainly.

## Gate order (STOP at the first failure, no bar-moving, no bar-shrinking)

- G0 harness: deterministic, CPU-only, $0, no LLMs/APIs/GPUs; scripted
  refusal judge over SYNTHETIC benign-proxy tasks only (fictional
  "do not reveal the vault code" policy, dummy placeholder secret).
  Never real disallowed content, never real jailbreak payloads.
  VERDICT: PASS — 10/10 tests green, 2026-10-30.
- G1 author-code recheck (fresh, 2026-10-30 ~09:07 UTC, BEFORE any
  experiment run):
  * Abs page (arxiv.org/abs/2610.37738): NO author code link. The
    "Code, Data and Media" section holds only third-party finder
    toggles (alphaXiv, CatalyzeX, DagsHub, GotitPub, Hugging Face,
    ScienceCast, Replicate, Spaces, TXYZ.AI). The one linked file is
    an example SKILL.md cited in the abstract, not author code.
  * Full-text HTML (arxiv.org/html/2610.37738v1, 464 lines, plus a
    curl re-fetch grepped locally): "github" matches are ONLY the
    langchain-ai/langchain citation and arXiv infrastructure
    (LaTeXML, html_feedback). ZERO "zenodo", ZERO "4open", ZERO
    "replication package", ZERO code-availability statement. The
    only Hugging Face link is the Llama-Guard judge model cited as a
    third-party tool, not an author artifact.
  VERDICT: PASS — no author code or author replication/data package.
- Pilot gate (LINEAGE-FATIGUE GATE, load-bearing): locked bars in
  PREREG.md §Pilot, seed 111, unseen at lock time. Must show a
  near-zero benign floor vs a large injected lift with CIs excluding
  0, AND a real delivery-channel differentiation (loaded skill file
  vs same text as user message, preregistered margin), or KILL FAST.
- G2 disease + G3 mechanism: PREREG-locked BEFORE head-to-head,
  fresh seeds 202/203/204, paired bootstrap CIs. Bars in PREREG.md.
- Tests green, determinism re-run byte-identical, SHA-256 of the
  headline results file recorded.

## Standing warnings honoured

- #97 lesson: PREREG decision rule is "ANY locked bar fails -> KILL".
  No post-hoc amendments, no matter how well-argued.
- #100 lesson: G1 stops builds duplicating an author-released
  artifact; paper-text evidence suffices. Here the paper text
  announces NO such artifact, so G1 passes on the evidence above.
- Differentiation vs lineage (#87, #93, #106 role-spoofing): this
  build's claim is NOT generic injection success. It is the
  configuration-file supply chain: the SAME directive text behaves
  differently when loaded as a skill file (system context) vs sent
  as a user message vs present-but-unloaded. If the loaded-vs-user
  margin fails, the build is just another injection paper and dies
  at the pilot gate.

## Decision rule

ANY locked bar fails -> KILL with an honest KILLED.md + negative
PAPER.md, no repo, no LinkedIn draft. Scope honesty in every
artifact: scripted-analog numbers only, synthetic tasks only.

## Final verdicts

- G0 PASS (10/10 tests). G1 PASS (no author code/package, evidence above).
- Pilot PASS. G2 PASS. G3 PASS. Tests green; determinism re-run
  byte-identical; headline SHA-256
  16fe8ac4be9a2d296135d6d4151514a1938cb0109c47b69fc2cccbd2779eae7b.
- Overall: PASS — staged, REPO NEEDED: habib-analyst/poisoned-skills.
