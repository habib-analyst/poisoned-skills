import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from poisoned_skills import (
    Agent, BENIGN_SKILL, INJECTED_SKILL, STRENGTH, make_secret_tasks,
    make_clean_tasks, normalise_loaded_text, paired_bootstrap_ci,
    phonetic_variant, run_condition, stealth_variant, task_resistance,
    wilson_ci,
)


def test_resistance_deterministic_and_bounded():
    a = [task_resistance(7, i) for i in range(50)]
    b = [task_resistance(7, i) for i in range(50)]
    assert a == b
    assert all(0.0 <= r < 1.0 for r in a)
    assert len(set(a)) == 50


def test_benign_floor_and_clean_utility():
    sec = make_secret_tasks(1, 100)
    clean = make_clean_tasks(1, 20)
    r = run_condition("benign_loaded", sec, clean)
    assert r["secret_comply"] == 0
    assert r["clean_rate"] == 1.0


def test_not_loaded_has_no_effect():
    sec = make_secret_tasks(1, 100)
    clean = make_clean_tasks(1, 20)
    r = run_condition("injected_not_loaded", sec, clean)
    assert r["secret_comply"] == 0
    assert r["clean_rate"] == 1.0


def test_loaded_beats_user_message_nested():
    sec = make_secret_tasks(1, 200)
    clean = make_clean_tasks(1, 20)
    loaded = run_condition("injected_loaded", sec, clean)
    user = run_condition("injected_user_message", sec, clean)
    assert loaded["secret_rate"] > user["secret_rate"]
    # Nesting: every user-message compliance is also a loaded compliance.
    for u, l in zip(user["secret_outcomes"], loaded["secret_outcomes"]):
        assert not (u == "comply" and l == "refuse")


def test_stealth_normalisation_restores_directive():
    assert normalise_loaded_text(stealth_variant(INJECTED_SKILL)) == INJECTED_SKILL
    sec = make_secret_tasks(1, 200)
    clean = make_clean_tasks(1, 20)
    direct = run_condition("injected_loaded", sec, clean)
    stealth = run_condition("stealth_loaded", sec, clean)
    assert direct["secret_outcomes"] == stealth["secret_outcomes"]


def test_phonetic_weaker_than_direct():
    sec = make_secret_tasks(1, 200)
    clean = make_clean_tasks(1, 20)
    direct = run_condition("injected_loaded", sec, clean)
    phon = run_condition("phonetic_loaded", sec, clean)
    assert phon["secret_rate"] < direct["secret_rate"]
    assert phon["secret_rate"] > 0.0


def test_clean_tasks_unaffected_by_injection():
    sec = make_secret_tasks(1, 50)
    clean = make_clean_tasks(1, 20)
    for cond in ("benign_loaded", "injected_loaded", "stealth_loaded",
                 "phonetic_loaded", "injected_user_message"):
        assert run_condition(cond, sec, clean)["clean_rate"] == 1.0


def test_paired_bootstrap_ci_contains_point_and_excludes_zero_when_large():
    sec = make_secret_tasks(1, 300)
    clean = make_clean_tasks(1, 20)
    a = run_condition("benign_loaded", sec, clean)["secret_outcomes"]
    b = run_condition("injected_loaded", sec, clean)["secret_outcomes"]
    point, lo, hi = paired_bootstrap_ci(a, b, n_resamples=500, seed=1)
    assert lo <= point <= hi
    assert lo > 0


def test_wilson_ci_sane():
    lo, hi = wilson_ci(0, 100)
    assert lo == 0.0 and hi < 0.05
    lo, hi = wilson_ci(50, 100)
    assert lo < 0.5 < hi


def test_strengths_documented():
    assert STRENGTH["benign_loaded"] == 0.0
    assert STRENGTH["injected_loaded"] == 0.45
    assert STRENGTH["phonetic_loaded"] < STRENGTH["injected_loaded"]
    assert STRENGTH["injected_user_message"] < STRENGTH["phonetic_loaded"]
