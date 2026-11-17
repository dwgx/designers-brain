#!/usr/bin/env python3
"""Synthetic gate counterexamples only; this does not execute browser input.

The specific historical loopholes are double send, unknown composition state,
and behavior-green overriding a failed geometry/semantic layer.
"""
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, HERE / relative)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


ime = module("ime_gate", "ui-02/cdp_ime_test.py")
visual = module("visual_gate", "ui-03/fixture/run_visual.py")
control = {"compositionStartFired": True, "compositionEndFired": True,
    "enterDuringComposition_isComposing": True, "enterAfterComposition_isComposing": False,
    "compositionStateEnded": True, "sendCountDuringComposition": 0,
    "sendCountAfterComposition": 1, "sendDeltaAfterComposition": 1,
    "resetControlPassed": True, "tabFocusPassed": True}
assert ime.harness_gate(control)
for changed in ({"sendCountAfterComposition": 2, "sendDeltaAfterComposition": 2},
                {"enterAfterComposition_isComposing": None}, {"resetControlPassed": False}):
    assert not ime.harness_gate(dict(control, **changed)), changed
layers = {key: {"ok": True} for key in ("geometry", "behavior", "semantics")}
assert visual.mechanical_gate(layers)
for key in ("geometry", "semantics"):
    bad = copy.deepcopy(layers)
    bad[key]["ok"] = False
    assert not visual.mechanical_gate(bad), key
print("PASS 7 synthetic gate controls; no browser input/pixels measured")
