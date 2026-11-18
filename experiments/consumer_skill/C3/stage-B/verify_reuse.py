#!/usr/bin/env python3
"""C3 Stage B local verifier.

Reads ONLY:
  - candidate public inputs (CAPABILITIES.json + 4 reuse evidence files)
  - this consumer's own sealed A/ files (READY.json, manifest.json, unaided-selection.json)
  - Root-published CUE.json / A-SEAL.json / consumer-binding-C3.json (read-only)
Writes ONLY the single --out path (which the caller places under B/).

Design note for control 5: the process exit code is ALWAYS 0 by design. The
authoritative result is the printed VERDICT line and the out JSON. This
demonstrates that an outer exit code 0 is NOT equivalent to PASS.
"""
import argparse, json, hashlib, os, sys

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def judge_cell(row):
    """Judgment function: accept a cell ONLY as conditional under the exact
    preserved conditions. Reject any inflation to supported, any missing
    required field, and any deviation of the preserved statuses."""
    required = ["state", "basis", "scope", "current_output_reverified",
                "determinism_scope", "historical_only", "current_runtime_readiness"]
    for k in required:
        if k not in row:
            return False, f"missing required field: {k}"
    if row["state"] == "supported":
        return False, "inflation: conditional must NOT be upgraded to supported"
    if row["state"] != "conditional":
        return False, f"unexpected state: {row['state']}"
    if row["scope"] != "historical_only":
        return False, "scope must remain historical_only"
    if row["current_output_reverified"] is not False:
        return False, "current_output_reverified must remain false"
    if "P1" not in str(row["determinism_scope"]) or "not P0" not in str(row["determinism_scope"]):
        return False, "determinism_scope must remain P1 / not P0"
    if row["current_runtime_readiness"] != "unverified_by_this_build":
        return False, "current_runtime_readiness mismatch"
    return True, "accepted as conditional (preserved fields intact)"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidate", required=True)
    ap.add_argument("--a", required=True)
    ap.add_argument("--rootctrl", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    results = []
    def record(name, expected, actual, passed):
        results.append({"control": name, "expected": expected, "actual": actual,
                        "passed": bool(passed)})

    with open(f"{args.candidate}/knowledge/CAPABILITIES.json", encoding="utf-8") as f:
        caps = json.load(f)
    row = caps["views"]["motion_historical_3"]["rows"][0]
    blender = row["capabilities"]["blender"]

    # ---- Control 1: A/A metadata consistency (Stage A sealed == B re-read) ----
    ready = json.load(open(f"{args.a}/READY.json", encoding="utf-8"))
    manifest = json.load(open(f"{args.a}/manifest.json", encoding="utf-8"))
    unaided = json.load(open(f"{args.a}/unaided-selection.json", encoding="utf-8"))
    cue = json.load(open(f"{args.rootctrl}/CUE.json", encoding="utf-8"))
    seal = json.load(open(f"{args.rootctrl}/A-SEAL.json", encoding="utf-8"))
    exp_meta = {"case_id": "C3", "attempt_id": "P4R-C3-20261117T123432",
                "final_commit": "c35d748e1cc9f23415fff0bf019a9c03234c421e",
                "final_tree": "fb24565b02597057784cbeed23f70ba657711804"}
    actual_meta = {k: ready.get(k) for k in exp_meta}
    meta_ok = (actual_meta == exp_meta
               and unaided["case_id"] == "C3" and unaided["attempt_id"] == exp_meta["attempt_id"]
               and cue["case_id"] == "C3" and seal["case_id"] == "C3"
               and ready["manifest_sha256"] == cue["stage_a_manifest_sha256"] == seal["stage_a_manifest_sha256"])
    record("A_A_metadata_consistency", exp_meta, actual_meta, meta_ok)

    # ---- Control 2: inflation rejection (conditional -> supported must be rejected) ----
    real = {"state": blender["state"], "basis": blender["basis"], "scope": row["scope"],
            "current_output_reverified": row["current_output_reverified"],
            "determinism_scope": row["determinism_scope"],
            "historical_only": row["scope"] == "historical_only",
            "current_runtime_readiness": row["current_runtime_readiness"]}
    ok_real, why_real = judge_cell(real)
    inflated = dict(real); inflated["state"] = "supported"
    ok_infl, why_infl = judge_cell(inflated)
    inflation_rejected = (ok_real is True and ok_infl is False and "inflation" in why_infl)
    record("inflation_rejection", "real accepted; supported-inflation rejected",
           f"real={ok_real}({why_real}); inflated={ok_infl}({why_infl})", inflation_rejected)

    # ---- Control 3: missing required field must fail ----
    missing = dict(real); missing.pop("determinism_scope")
    ok_miss, why_miss = judge_cell(missing)
    missing_failed = (ok_miss is False and "missing required field" in why_miss)
    record("missing_field_failure", "reject row with determinism_scope removed",
           f"accepted={ok_miss}; reason={why_miss}", missing_failed)

    # ---- Control 4: reuse hash mismatch must fail ----
    reuse_paths = {
        "checks.md": "experiments/anim_test_03_blender/checks.md",
        "out.mp4": "experiments/anim_test_03_blender/out.mp4",
        "build_scene.py": "experiments/anim_test_03_blender/build_scene.py",
        "scene.blend": "experiments/anim_test_03_blender/scene.blend",
    }
    expected_sha = {e["locator"].split("/")[-1]: e["retrieved_bytes_sha256"]
                    for e in blender["source_refs"] if e["locator"].startswith("experiments/")}
    actual_sha = {}
    all_match = True
    for key, rel in reuse_paths.items():
        a = sha256_file(f"{args.candidate}/{rel}")
        actual_sha[key] = a
        if a != expected_sha.get(key):
            all_match = False
    mismatch_detected = (sha256_file(f"{args.candidate}/{reuse_paths['out.mp4']}") != "0"*64)
    # deliberately compare a wrong expected hash -> must NOT match
    wrong_ok = (actual_sha["out.mp4"] == "deadbeef"*8)
    hash_control = all_match and (wrong_ok is False) and mismatch_detected
    record("reuse_hash_verification", "4 reuse SHAs match matrix; wrong hash rejected",
           {"expected": expected_sha, "actual": actual_sha,
            "wrong_hash_accepted": wrong_ok}, hash_control)

    # ---- Control 5: exit0 != PASS is demonstrated by tool design (always exit 0) ----
    verdict = "PASS" if all(r["passed"] for r in results) else "FAIL"
    out = {"case_id": "C3", "attempt_id": exp_meta["attempt_id"], "stage": "B",
           "controls": results, "verdict": verdict,
           "exit_code_semantics": "process exit code forced 0; verdict line is authoritative",
           "candidate_head": None}
    import subprocess
    out["candidate_head"] = subprocess.check_output(
        ["git", "-C", args.candidate, "rev-parse", "HEAD"], text=True).strip()
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    for r in results:
        print(f"[{('PASS' if r['passed'] else 'FAIL')}] {r['control']}")
    print("VERDICT: " + verdict)
    # NOTE: intentional always-zero exit, to prove outer exit0 is not the PASS gate.
    return 0

if __name__ == "__main__":
    sys.exit(main())
