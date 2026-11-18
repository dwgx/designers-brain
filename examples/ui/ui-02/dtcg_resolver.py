#!/usr/bin/env python3
"""DTCG 2025.10 fixture subset: sRGB color, px/rem dimension, whole-token aliases.

Names, inherited/alias types, explicit values and references share one validation
path. JSON Pointer aliases, composite values and other token/color types are
unsupported and fail explicitly; this is not a complete DTCG implementation.
Sources: https://www.designtokens.org/tr/2025.10/format/ sections 5.1.1, 5.2.2, 7.4.5.
The existing resolver ordering/modifier pipeline is retained below.
"""
import json
import math
import re
from pathlib import Path

CURLY = re.compile(r"^\{([^{}]+)\}$")
NAME_BAD = re.compile(r"[{}.]")
SUPPORTED_TYPES = {"color", "dimension"}
GROUP_METADATA = {"$schema", "$description", "$type", "$extensions", "$deprecated"}


class DTCGError(Exception):
    """Invalid or explicitly unsupported input in this fixture subset."""


def _name(name):
    if not isinstance(name, str) or not name or name.startswith("$") or NAME_BAD.search(name):
        raise DTCGError("format 5.1.1: invalid name segment %r" % name)


def _declared_type(value, path):
    if not isinstance(value, str) or value not in SUPPORTED_TYPES:
        raise DTCGError("unsupported $type %r at %s; supported: color, dimension" % (value, path))
    return value


def _index(doc):
    if not isinstance(doc, dict):
        raise DTCGError("token document must be an object")
    idx, inherited = {}, {}
    def walk(node, parts, parent_type):
        if not isinstance(node, dict):
            raise DTCGError("token/group %s must be an object" % ".".join(parts))
        if "$value" in node:
            if not parts:
                raise DTCGError("root must be a token group, not an unnamed token")
            path = ".".join(parts)
            if path in idx:
                raise DTCGError("duplicate canonical token path: " + path)
            if "$type" in node:
                _declared_type(node["$type"], path)
            idx[path], inherited[path] = node, parent_type
            return
        group_type = parent_type
        if "$type" in node:
            group_type = _declared_type(node["$type"], ".".join(parts) or "<root>")
        for key, value in node.items():
            if key.startswith("$"):
                if key not in GROUP_METADATA:
                    raise DTCGError("unsupported reserved group property: " + key)
                continue
            _name(key)  # before joining: a literal dot cannot become a hierarchy
            walk(value, parts + (key,), group_type)
    walk(doc, (), None)
    return idx, inherited


def iter_tokens(node, path=()):
    """Yield original tokens after validating raw group/token name boundaries."""
    for segment in path:
        _name(segment)
    idx, _ = _index(node)
    prefix = ".".join(path)
    for key, tok in idx.items():
        yield (prefix + "." + key if prefix else key), tok


def build_token_index(doc):
    return _index(doc)[0]


def _number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def _validate_value(kind, value, path):
    if not isinstance(value, dict):
        raise DTCGError("invalid %s value at %s: expected object" % (kind, path))
    if kind == "dimension":
        if set(value) != {"value", "unit"} or not _number(value.get("value")) or value.get("unit") not in ("px", "rem"):
            raise DTCGError("invalid dimension at %s: finite value and px/rem unit required" % path)
    elif kind == "color":
        components = value.get("components")
        if value.get("colorSpace") != "srgb":
            raise DTCGError("unsupported color space at %s: fixture supports srgb" % path)
        if (not isinstance(components, list) or len(components) != 3
                or not all(c == "none" or _number(c) for c in components)):
            raise DTCGError("invalid color at %s: three finite/none components required" % path)
        alpha = value.get("alpha", 1)
        if not _number(alpha) or not 0 <= alpha <= 1:
            raise DTCGError("invalid color alpha at " + path)
        if "hex" in value and (not isinstance(value["hex"], str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", value["hex"])):
            raise DTCGError("invalid optional sRGB hex fallback at " + path)


def _resolve(doc, paths=None):
    idx, inherited = _index(doc)
    values, types = {}, {}
    def visit(path, stack):
        if path in stack:
            raise DTCGError("format 7.2.3: circular reference: " + " -> ".join(stack + [path]))
        if path in values:
            return values[path], types[path]
        if path not in idx:
            raise DTCGError("format 7.1.1: alias target %s not found" % path)
        tok = idx[path]
        value = tok["$value"]
        match = CURLY.fullmatch(value) if isinstance(value, str) else None
        if match:
            target = match.group(1)
            for segment in target.split("."):
                _name(segment)
            value, target_type = visit(target, stack + [path])
            # 5.2.2: absent explicit type on an alias comes from its target.
            kind = tok["$type"] if "$type" in tok else target_type
            if kind != target_type:
                raise DTCGError("format 7.4.5: type conflict at %s: %s alias targets %s" % (path, kind, target_type))
        else:
            kind = tok["$type"] if "$type" in tok else inherited[path]
            if kind is None:
                raise DTCGError("format 8/5.2.2: token %s has no determinable $type" % path)
        _validate_value(kind, value, path)
        values[path], types[path] = value, kind
        return value, kind
    wanted = list(idx) if paths is None else list(paths)
    for path in wanted:
        visit(path, [])
    return {p: values[p] for p in wanted}, {p: types[p] for p in wanted}


def check_names_and_types(doc):
    """Validate names, resolved types AND values consistently with public entrypoints."""
    _, types = _resolve(doc)
    return list(types.items())


def resolve_alias(doc, path, idx=None, _stack=None):
    """Resolve one token; supplied legacy caches never bypass document validation."""
    values, _ = _resolve(doc, [path])
    return values[path]


def resolve_all(doc):
    """Resolve all tokens after shared name/type/value/reference validation."""
    return _resolve(doc)[0]


# ---- Resolver module (2025.10) -------------------------------------------

def deep_merge(base, override):
    """Last-wins merge used for resolutionOrder flattening (6.2 step 1.3)."""
    out = dict(base)
    for k, v in override.items():
        if k in out and isinstance(out[k], dict) and isinstance(v, dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def validate_inputs(resolver, inputs):
    """Resolver 6.1 + 5.2 + 4.1.5.3 default handling."""
    mods = resolver.get("modifiers", {})
    for key, val in inputs.items():
        if key not in mods:
            raise DTCGError("resolver 6.1: input key %r is not a declared modifier" % key)
        if not isinstance(val, str):
            raise DTCGError("resolver 5.2: input %r value MUST be a string" % key)
        contexts = mods[key].get("contexts", {})
        if val not in contexts:
            raise DTCGError("resolver 6.1: input %s=%r not in modifier contexts %s"
                            % (key, val, sorted(contexts)))
    # apply defaults (4.1.5.3) then require every modifier to have a value
    effective = dict(inputs)
    for key, mod in mods.items():
        if key not in effective:
            if "default" in mod:
                effective[key] = mod["default"]
            else:
                raise DTCGError("resolver 6.1: modifier %r has no default and no input" % key)
    return effective


def _resolve_ref(resolver, ref):
    """Resolve a same-document $ref JSON pointer (resolver 4.2)."""
    if not isinstance(ref, str) or not ref.startswith("#/"):
        raise DTCGError("resolver 4.2: only same-document #/ pointers supported, got %r" % ref)
    cur = resolver
    for seg in ref[2:].split("/"):
        cur = cur[seg.replace("~1", "/").replace("~0", "~")]
    return cur


def resolve_document(resolver, inputs):
    """Full resolver 6 pipeline: input validation -> ordering -> aliases.
    Returns (flattened_tokens, resolved_values, effective_inputs)."""
    eff = validate_inputs(resolver, inputs)
    order = resolver["resolutionOrder"]
    sets = resolver.get("sets", {})
    mods = resolver.get("modifiers", {})
    flat = {}
    for item in order:
        if "$ref" in item:
            target = _resolve_ref(resolver, item["$ref"])
            # detect inline vs named; a named set/modifier is looked up by name
            name = item["$ref"].split("/")[-1]
        else:
            name = item.get("name")
            target = item
            if item.get("type") == "set" or "sources" in item:
                target = {"sources": item.get("sources", [])}
            elif item.get("type") == "modifier" or "contexts" in item:
                target = {"contexts": item.get("contexts", {}), "default": item.get("default")}
        # decide set vs modifier
        is_modifier = (name in mods) or ("contexts" in target)
        if is_modifier:
            context_key = eff.get(name)
            contexts = target.get("contexts", mods.get(name, {}).get("contexts", {}))
            if context_key not in contexts:
                raise DTCGError("resolver 6.2: context %r missing in modifier %r" % (context_key, name))
            sources = contexts[context_key]
        else:
            sources = target.get("sources", [])
        for src in sources:
            # each source may be an inline tokens object or a reference object
            if isinstance(src, dict) and "$ref" in src:
                src = _resolve_ref(resolver, src["$ref"])
            flat = deep_merge(flat, src)  # 6.2 step 1.3: later last wins
    # 6.3: aliases resolved ONLY now, after full flattening
    values = resolve_all(flat)
    return flat, values, eff


if __name__ == "__main__":
    import sys
    doc = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    check_names_and_types(doc)
    print(json.dumps(resolve_all(doc), indent=2, ensure_ascii=False))
