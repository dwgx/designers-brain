#!/usr/bin/env python3
"""Bounded controls for the shipped sRGB/dimension/whole-token alias subset.

Exercises independent counterexamples and the original 14-token/order controls.
No browser or network. Exit zero only when valid inputs pass and invalid ones fail.
"""
import copy
import json
from pathlib import Path
import dtcg_resolver as R

HERE = Path(__file__).resolve().parent
COUNT = 0


def check(label, ok):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(label)
    print("PASS " + label)


def rejects(label, fn, contains=None):
    try:
        fn()
    except R.DTCGError as exc:
        check(label, contains is None or contains in str(exc))
        return
    raise AssertionError(label + ": invalid input accepted")


def main():
    tokens = json.loads((HERE / "tokens.tokens.json").read_text())
    cycle = json.loads((HERE / "tokens-cycle.tokens.json").read_text())
    res = json.loads((HERE / "themes.resolver.json").read_text())
    values = R.resolve_all(tokens)
    check("original 14 tokens and chained aliases", len(values) == 14 and values["color.action"] == values["color.primary"])
    R.check_names_and_types(tokens)
    _, default, effective = R.resolve_document(res, {})
    check("default modifier order", effective == {"theme": "light", "density": "comfortable"} and default["size.controlHeight"]["value"] == 44)
    _, dark, _ = R.resolve_document(res, {"theme": "dark", "density": "compact"})
    check("explicit modifiers", dark["color.surface"]["hex"] == "#121217" and dark["size.controlHeight"]["value"] == 24)
    _, hc, _ = R.resolve_document(res, {"theme": "hc"})
    check("aliases resolved after ordering", hc["color.action"]["hex"] == "#ffff00")

    color = {"colorSpace": "srgb", "components": [1, 0, 0]}
    dim = {"value": 4, "unit": "px"}
    conflict = {"bad": {"$type": "color", "$value": "{spacing}"}, "spacing": {"$type": "dimension", "$value": dim}}
    for name, call in (("check", R.check_names_and_types), ("all", R.resolve_all)):
        rejects("actual alias type conflict / " + name, lambda call=call: call(conflict), "type conflict")
    rejects("actual alias type conflict / single", lambda: R.resolve_alias(conflict, "bad"), "type conflict")
    alias = {"base": {"$type": "color", "$value": color}, "alias": {"$value": "{base}"}, "chain": {"$value": "{alias}"}}
    check("untyped chained alias inherits target type", dict(R.check_names_and_types(alias))["chain"] == "color" and R.resolve_all(alias)["chain"] == color)
    inherited = {"$type": "dimension", "spacing": {"$value": dim}}
    check("root group type inherited", dict(R.check_names_and_types(inherited))["spacing"] == "dimension" and R.resolve_all(inherited)["spacing"] == dim)
    collision = {"brand.primary": {"$type": "color", "$value": color}, "brand": {"primary": {"$type": "dimension", "$value": dim}}}
    rejects("literal dot name never silently overwrites", lambda: R.resolve_all(collision), "invalid name")
    missing_type = {"sets": {"base": {"sources": [{"bad": {"$value": 7}}]}}, "resolutionOrder": [{"$ref": "#/sets/base"}]}
    rejects("resolve_document validates type", lambda: R.resolve_document(missing_type, {}), "$type")
    positive_names = {"price$ token": {"$type": "dimension", "$value": dim}, "alias": {"$value": "{price$ token}"}}
    check("legal dollar-in-name and spaces retained", R.resolve_all(positive_names)["alias"] == dim)
    rejects("invalid dimension literal", lambda: R.resolve_all({"x": {"$type": "dimension", "$value": color}}), "dimension")
    rejects("invalid color literal", lambda: R.resolve_all({"x": {"$type": "color", "$value": dim}}), "color")
    rejects("cycle alias", lambda: R.resolve_all(cycle), "circular reference")
    rejects("self cycle", lambda: R.resolve_alias(cycle, "selfLoop.x"), "circular")
    missing = copy.deepcopy(tokens)
    missing["color"]["brand"]["$value"] = "{color.doesNotExist}"
    rejects("missing target", lambda: R.resolve_all(missing), "not found")
    for bad in ({"nope": "x"}, {"theme": 1}, {"theme": "neon"}):
        rejects("invalid modifier " + repr(bad), lambda bad=bad: R.resolve_document(res, bad))
    print("RESULT: %d resolver controls passed; explicit sRGB/px-rem subset." % COUNT)


if __name__ == "__main__":
    main()
