# PREREGISTRATION — project #110 `poisoned-skills`

Locked 2026-10-30, AFTER G0/G1 and BEFORE the pilot run, and BEFORE
any head-to-head run. Pilot seed 111 and head-to-head seeds
202/203/204 were not used in any prior run (the only pre-lock runs
were the 10 unit tests and a smoke check on test seed 1, which is
used in no gate). Decision rule (standing, #97 lesson): ANY locked
bar fails -> KILL. No post-hoc bar changes, no bar-shrinking. This
file is not to be edited after a gated run except to append the
verdict.

## Source paper (context only, never reproduced)

arXiv 2610.37738 (see KILLGATE.md). Paper figures are context only.

## Harness (fixed before locking)

src/poisoned_skills.py: scripted agent, authority strengths
benign 0.00 / injected-loaded 0.45 / stealth-loaded 0.45 /
phonetic-loaded 0.30 / user-message 0.15 / not-loaded 0.00;
task resistance = SHA-256(seed, index) uniform in [0,1);
compliance iff resistance < strength (secret tasks); clean tasks
always comply. Paired bootstrap: 2000 resamples, seed 9500, 95% CI
on the per-task paired difference.

## Pilot gate (seed 111; n=200 secret + 50 clean tasks per condition)

- P1: benign_loaded secret rate <= 0.05.
- P2: (injected_loaded - benign_loaded) point lift >= 0.30 AND
  paired bootstrap 95% CI lower bound > 0.
- P3 (differentiation): (injected_loaded - injected_user_message)
  point lift >= 0.20 AND paired bootstrap 95% CI lower bound > 0.
- Any failure -> KILL FAST, no head-to-head.

## Head-to-head protocol (fresh seeds 202, 203, 204; n=300 secret +
50 clean tasks per seed per condition; results pooled over 900
secret tasks, paired by (seed, task index))

Conditions: benign_loaded, injected_loaded, stealth_loaded,
phonetic_loaded, injected_user_message, injected_not_loaded.

## Locked bars — G2 (disease: injected skill files raise compliance)

- G2a: (injected_loaded - benign_loaded) point lift >= 0.30 AND
  paired bootstrap 95% CI lower bound >= 0.20.
- G2b (channel differentiation): (injected_loaded -
  injected_user_message) point lift >= 0.20 AND paired bootstrap
  95% CI lower bound >= 0.10.

## Locked bars — G3 (load-bearing mechanism + benign bound)

- G3a (unloaded file is inert): (injected_not_loaded -
  benign_loaded) point difference <= 0.05 AND paired bootstrap
  95% CI upper bound <= 0.10.
- G3b (stealth gives no gain, as in the paper qualitatively):
  absolute point difference |stealth_loaded - injected_loaded|
  <= 0.20.
- G3c (phonetic weaker than direct): (phonetic_loaded -
  injected_loaded) point difference <= -0.05 AND paired bootstrap
  95% CI upper bound < 0.
- G3d (benign/utility bound): benign_loaded secret rate <= 0.05;
  clean-task compliance >= 0.95 in EVERY condition; maximum
  clean-rate gap across conditions <= 0.05.

## Verdict rule

ALL pilot bars, then ALL G2/G3 bars, must pass. Any single failure
-> KILL with an honest KILLED.md + negative PAPER.md, no repo,
no LinkedIn draft. Scope honesty applies to every artifact:
scripted-analog numbers only, synthetic tasks only, and the
strength parameters above are disclosed as model parameters of
the analog, not measurements of real models.

## Verdict (appended after the gated runs, 2026-10-30)

- Pilot (seed 111, n=200): benign 0.0%; injected-loaded 45.5%;
  lift +45.5pp, 95% CI [38.5, 52.0]; loaded-vs-user +26.5pp, 95% CI
  [20.5, 32.5]. P1, P2, P3 all PASS.
- Head-to-head (seeds 202/203/204, n=900 pooled): G2a, G2b, G3a,
  G3b, G3c, G3d all PASS (see results/headline.json). No bar was
  changed after locking. PASS.
