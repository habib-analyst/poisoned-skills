# poisoned-skills — project #110

**Scripted analog** of arXiv 2610.37738 (Manjusha & Emani, UIUC/Argonne),
"Poisoned Skills: Propagating Jailbreaks Through Agent Markdown Files".
The paper's real-model figures are context only and are NOT reproduced
here. Everything measured in this repo comes from a deterministic,
CPU-only, $0 scripted agent over **synthetic benign-proxy tasks**
(a fictional "do not reveal the vault code" policy with a dummy
placeholder secret). No real disallowed content, no real jailbreak
payloads, no LLMs, no APIs, no GPUs.

## The claim tested

A directive planted in a SKILL.md file **loaded** into an agent's
system context propagates differently from the **same text** sent as
a user message or sitting in a file that is never loaded. That
delivery-channel difference — the configuration-file supply chain —
is the differentiation from generic prompt-injection work (and from
#106 role-spoofing, which is about role attribution, not file loading).

## Run

```bash
python3 -m pytest tests/ -q
python3 experiments/run_pilot.py          # PREREG pilot, seed 111
python3 experiments/run_head_to_head.py   # PREREG head-to-head, seeds 202-204
```

## Layout

- `src/poisoned_skills.py` — scripted agent, skill files, authority
  model, paired bootstrap CIs. Authority strengths are fixed model
  parameters, documented in the module docstring and PREREG.md.
- `tests/` — 10 unit tests (delivery-path nesting, stealth
  normalisation, clean-task utility, CI sanity).
- `experiments/` — pilot + head-to-head runners.
- `results/` — `pilot.json`, `headline.json` (SHA-256 recorded in
  the writeup; re-runs are byte-identical).
- `KILLGATE.md`, `PREREG.md` — gates locked before the gated runs;
  decision rule: ANY locked bar fails -> KILL.

## Limits (stated plainly)

A scripted judge is a weak proxy for real models. The compliance
rates below demonstrate a channel effect **inside this analog** under
its stated authority parameters; they say nothing about how any real
model would behave. The value of the analog is the ablation structure
(loaded vs user-message vs unloaded, stealth vs phonetic), not the
absolute percentages.
