#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Designers_Brain skill 自检：引用路径存在性 + frontmatter 合规 + junction 解析 + domains.yaml 校验。

用法（仓库根 D:/Project/Designers_Brain）：
    python docs/skill/_selfcheck.py

口径：
- 抽取 skill_spec.md / draft/SKILL.md / skills/designers-brain/（SKILL.md + references/*.md +
  domains.yaml + agents/openai.yaml）/ templates/design_brief.md 中全部
  `REPO/...`、`D:/Project/Designers_Brain/...`、`knowledge/...`、`templates/...`、`skills/...` 形态 token；
- 逐条 exists()（目录 / 文件 / 通配符分别处理）；包内相对路径（references/、agents/、domains.yaml）
  解析到 skills/designers-brain/；
- 备选布局（docs/skill/designers-brain/）仍列规划、不计失败；示意形态（含 ... / < / >）跳过；
- frontmatter：草案与落位版均校验（name / description 按 agentskills.io 口径；落位版查与父目录同名）；
- junction 解析：4 条（仓库内 1 + 用户级 3）realpath == REPO/skills/designers-brain（逐条）；
- domains.yaml：逐域 count 与 cards 目录实际数一致（计数规则见 count_cards；新增域时按规格 §5.3 更新）。

退出码：0 = PASS（无失败）；1 = 有失败。
"""
import glob
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PKG = os.path.join(ROOT, "skills", "designers-brain")

FILES = [
    "docs/skill/skill_spec.md",
    "docs/skill/draft/SKILL.md",
    "skills/designers-brain/SKILL.md",
    "skills/designers-brain/domains.yaml",
    "skills/designers-brain/agents/openai.yaml",
    "templates/design_brief.md",
] + ["skills/designers-brain/references/%s.md" % n for n in (
    "painter-modules", "mg-cards", "conflicts", "output-forms", "pipelines",
    "evidence", "review", "question-bank", "direction-protocol")]

TOKEN_RE = re.compile(
    r'(?<![\w.\-])'
    r'(?:'
    r'(?:REPO/|D:/Project/Designers_Brain/)?'
    r'(?:knowledge|docs|experiments|ops|templates|skills|skill|references|agents)/'
    r'[^\s`"\'（）,，;；。、|｜「」：:]+'
    r'|domains\.yaml'
    r')'
)

TOKEN_RE2 = re.compile(
    r'~?/?(?:\.claude-plugin|\.codex-plugin|\.claude|\.codex|\.agents)'
    r'/[^\s`"\'（）,，;；。、|｜「」：:]+'
)

# 规划/备选（未采用）：不计失败
PLANNED_PREFIXES = (
    "docs/skill/designers-brain/",    # 备选布局（v0.2 定稿采用 skills/，此条未采用）
)

# 包内相对路径：解析到 skills/designers-brain/
PACKAGE_PREFIXES = ("references/", "agents/")
PACKAGE_EXACT = {"domains.yaml"}

# junction 解析校验：4 条（仓库内 1 + 用户级 3）→ 均须指向 REPO/skills/designers-brain
JUNCTIONS = [
    ".agents/skills/designers-brain",
    "~/.agents/skills/designers-brain",
    "~/.claude/skills/designers-brain",
    "~/.codex/skills/designers-brain",
]

# 机器级路径中的「设计稿（未创建）」白名单：列出但不计失败
HARNESS_DESIGN_ONLY = {
    "~/.agents/plugins/marketplace.json",   # 个人级市场文件（本包只建仓库级；规格语义说明）
}


def clean(tok: str) -> str:
    tok = tok.strip()
    for pre in ("REPO/", "D:/Project/Designers_Brain/"):
        if tok.startswith(pre):
            tok = tok[len(pre):]
    return tok


def is_schematic(tok: str) -> bool:
    return ("..." in tok) or ("<" in tok) or (">" in tok)


def is_planned(tok: str) -> bool:
    return any(tok.startswith(p) for p in PLANNED_PREFIXES)


def resolve(tok: str) -> str:
    """token → 实际路径：包内相对（references/ · agents/ · domains.yaml）→ PKG；其余 → ROOT。"""
    t = tok.replace("/", os.sep)
    if tok.startswith(PACKAGE_PREFIXES) or tok in PACKAGE_EXACT:
        return os.path.join(PKG, t)
    p = os.path.join(ROOT, t)
    if not os.path.exists(p) and tok.startswith("skill/"):
        alt = os.path.join(ROOT, "docs", t)
        if os.path.exists(alt):
            return alt
    return p


def check_path(tok: str):
    p = resolve(tok)
    if "*" in tok or "?" in tok:
        hits = glob.glob(p)
        return ("ok", f"glob({len(hits)})") if hits else ("fail", "glob no hits")
    if os.path.isdir(p):
        return ("ok", "dir")
    if os.path.isfile(p):
        return ("ok", "file")
    return ("fail", "not found")


def check_frontmatter(path: str, expect_dir: str = None):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    out = []
    if not m:
        return [("FAIL", "无 frontmatter 块")]
    fm_text = m.group(1)
    if yaml is None:
        return [("SKIP", "pyyaml 未安装，跳过 YAML 解析")]
    try:
        data = yaml.safe_load(fm_text)
    except Exception as e:  # noqa: BLE001
        return [("FAIL", f"YAML 解析失败: {e}")]
    name = data.get("name", "")
    desc = data.get("description", "")
    if isinstance(name, str) and name:
        ok_len = 1 <= len(name) <= 64
        ok_re = bool(re.fullmatch(r"[a-z0-9-]+", name))
        ok_edge = not (name.startswith("-") or name.endswith("-")) and "--" not in name
        out.append(("OK" if (ok_len and ok_re and ok_edge) else "FAIL",
                    f"name={name!r} (len={len(name)}, 小写/连字符={ok_re}, 首尾/连续连字符={ok_edge})"))
        if expect_dir is not None:
            same = (name == expect_dir)
            out.append(("OK" if same else "FAIL",
                        f"name 与父目录同名：{name!r} vs {expect_dir!r} = {same}"))
    else:
        out.append(("FAIL", "name 缺失或非字符串"))
    if isinstance(desc, str) and desc:
        out.append(("OK" if len(desc) <= 1024 else "FAIL", f"description 长度={len(desc)} (≤1024)"))
    else:
        out.append(("FAIL", "description 缺失或非字符串"))
    return out


def check_junctions():
    """junction 解析：realpath == REPO/skills/designers-brain（逐条）。"""
    tgt = os.path.normcase(os.path.realpath(PKG))
    rows = []
    for j in JUNCTIONS:
        p = os.path.join(ROOT, j.replace("/", os.sep)) if not j.startswith("~") \
            else os.path.expanduser(j)
        if not os.path.exists(p):
            rows.append((j, "FAIL", "不存在（未激活）"))
            continue
        real = os.path.realpath(p)
        same = os.path.normcase(real) == tgt
        skill_md = os.path.isfile(os.path.join(p, "SKILL.md"))
        detail = f"realpath={real}" + ("" if skill_md else " · SKILL.md 不可达")
        rows.append((j, "ok" if (same and skill_md) else "FAIL", detail))
    return rows


def count_cards(domain_id):
    """域卡片计数规则（新增域时按规格 §5.3 在此更新）。"""
    if domain_id == "painter":
        d = os.path.join(ROOT, "knowledge", "domains", "painters", "modules")
        files = [f for f in glob.glob(os.path.join(d, "*.md"))
                 if os.path.basename(f) != "README.md"]
        return len(files), "knowledge/domains/painters/modules/*.md − README.md"
    if domain_id == "mg-motion":
        d = os.path.join(ROOT, "knowledge", "domains", "motion-graphics", "origin")
        files = [f for f in glob.glob(os.path.join(d, "*.png"))
                 if re.match(r"^(0[1-9]|1[0-5])_", os.path.basename(f))]
        return len(files), "knowledge/domains/motion-graphics/origin/ 01–15 号卡截图"
    return None, "未定义计数规则（按规格 §5.3 需更新 _selfcheck.py）"


def check_domains():
    """domains.yaml：逐域 count 与 cards 目录实际数一致。"""
    path = os.path.join(PKG, "domains.yaml")
    if not os.path.isfile(path):
        return [("domains.yaml", "FAIL", "文件不存在")], False
    if yaml is None:
        return [("domains.yaml", "SKIP", "pyyaml 未安装，跳过")], True
    try:
        data = yaml.safe_load(open(path, encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [("domains.yaml", "FAIL", f"YAML 解析失败: {e}")], False
    rows, ok_all = [], True
    for d in data.get("domains", []):
        did = d.get("id", "?")
        expected = d.get("count")
        actual, rule = count_cards(did)
        if actual is None:
            rows.append((did, "FAIL", f"count={expected} · {rule}"))
            ok_all = False
            continue
        good = (actual == expected)
        rows.append((did, "ok" if good else "FAIL",
                     f"count={expected} actual={actual}（{rule}）"))
        ok_all = ok_all and good
    return rows, ok_all


def check_harness(toks):
    """机器级/打包件路径：能解析的解析（仓库根 → 用户目录），解析不到的白名单项标设计稿。"""
    rows = []
    for t in sorted(toks):
        if is_schematic(t):
            rows.append((t, "skip", "占位符"))
            continue
        cand = []
        if t.startswith("~"):
            cand.append(os.path.expanduser(t))
        else:
            cand.append(os.path.join(ROOT, t.replace("/", os.sep)))
            cand.append(os.path.expanduser("~/" + t.replace("\\", "/")))
        found, detail = False, ""
        for c in cand:
            if "*" in c or "?" in c:
                hits = glob.glob(c)
                if hits:
                    found, detail = True, f"glob({len(hits)})"
                    break
            elif os.path.exists(c):
                found, detail = True, ("dir" if os.path.isdir(c) else "file")
                break
        if found:
            rows.append((t, "ok", detail))
        elif t in HARNESS_DESIGN_ONLY:
            rows.append((t, "design", "设计稿（未创建；非本包产物）"))
        else:
            rows.append((t, "fail", "not found"))
    return rows


def main() -> int:
    per_file = {}
    token_sources = {}
    harness_toks = set()
    missing_files = []
    for f in FILES:
        fp = os.path.join(ROOT, f)
        if not os.path.isfile(fp):
            missing_files.append(f)
            continue
        text = open(fp, encoding="utf-8").read()
        text_norm = text.replace("\\", "/")  # 反斜杠写法（PowerShell 块）归一化后同扫
        text_norm = text_norm.replace("$HOME/", "~/").replace("$HOME", "~")
        toks = set()
        for source in (text, text_norm):
            for m in TOKEN_RE.finditer(source):
                toks.add(clean(m.group(0)))
            for m in TOKEN_RE2.finditer(source):
                h = m.group(0)
                if h.startswith("/."):
                    h = h[1:]
                harness_toks.add(h)
        per_file[f] = toks
        for t in toks:
            token_sources.setdefault(t, []).append(f)

    all_toks = sorted(set().union(*per_file.values())) if per_file else []

    ok, fail, planned, schematic = [], [], [], []
    for t in all_toks:
        if is_schematic(t):
            schematic.append(t)
        elif is_planned(t):
            planned.append(t)
        else:
            status, detail = check_path(t)
            if status == "ok":
                ok.append((t, detail))
            else:
                fail.append((t, detail))

    print("== 文件 ==")
    for f in FILES:
        if f in missing_files:
            print(f"  !! 缺失: {f}")
        else:
            print(f"  {f}  refs(unique)={len(per_file[f])}")

    print(f"\n== 路径核验（仓库既有 + 包内）==\n  checked={len(ok)} ok={len(ok)} fail={len(fail)}")
    n_dir = sum(1 for _, d in ok if d == "dir")
    n_file = sum(1 for _, d in ok if d == "file")
    n_glob = sum(1 for _, d in ok if d.startswith("glob"))
    print(f"  （目录 {n_dir} / 文件 {n_file} / 通配符 {n_glob}）")
    for t, d in ok:
        print(f"    ok   {t}  [{d}]")

    if fail:
        print("\n== 失败 ==")
        for t, d in fail:
            print(f"    FAIL {t}  [{d}]  ← {token_sources.get(t)}")

    print(f"\n== 规划路径（备选布局，不计失败）== planned={len(planned)}")
    for t in planned:
        print(f"    ⏳ {t}")

    harness_rows = check_harness(harness_toks)
    n_h_ok = sum(1 for _, s, _ in harness_rows if s == "ok")
    n_h_design = sum(1 for _, s, _ in harness_rows if s == "design")
    n_h_fail = sum(1 for _, s, _ in harness_rows if s == "fail")
    n_h_skip = sum(1 for _, s, _ in harness_rows if s == "skip")
    print(f"\n== 机器级/打包件路径（状态核对）== ok={n_h_ok} design-only={n_h_design} "
          f"skip={n_h_skip} fail={n_h_fail}")
    for t, s, d in harness_rows:
        mark = {"ok": "ok", "design": "·", "skip": "~", "fail": "FAIL"}[s]
        print(f"    {mark:>4} {t}  [{d}]")

    print(f"\n== 示意形态（占位符，跳过）== schematic={len(schematic)}")
    for t in schematic:
        print(f"    ~ {t}")

    print("\n== frontmatter ==")
    fm_ok = True
    print("  -- 落位版（skills/designers-brain/SKILL.md）--")
    for status, detail in check_frontmatter(
            os.path.join(ROOT, "skills/designers-brain/SKILL.md"), expect_dir="designers-brain"):
        print(f"  {status}: {detail}")
        if status == "FAIL":
            fm_ok = False
    print("  -- 草案（docs/skill/draft/SKILL.md；临时位，父目录同名要求以落位版为准）--")
    for status, detail in check_frontmatter(os.path.join(ROOT, "docs/skill/draft/SKILL.md")):
        print(f"  {status}: {detail}")
        if status == "FAIL":
            fm_ok = False

    jrows = check_junctions()
    n_j_ok = sum(1 for _, s, _ in jrows if s == "ok")
    print(f"\n== junction 解析（4 条；realpath == REPO/skills/designers-brain）== {n_j_ok}/4 ok")
    for j, s, d in jrows:
        print(f"    {s:>4} {j}  [{d}]")

    drows, d_ok = check_domains()
    print(f"\n== domains.yaml 校验（count == cards 目录实际数）==")
    for did, s, d in drows:
        print(f"    {s:>4} [{did}] {d}")

    if missing_files:
        print(f"\n!! 缺失扫描文件: {missing_files}")

    verdict = "PASS" if (not fail and not missing_files and fm_ok
                         and n_j_ok == len(JUNCTIONS) and d_ok
                         and n_h_fail == 0) else "FAIL"
    print(f"\nRESULT: {verdict}  (checked={len(ok)} fail={len(fail)} planned={len(planned)} "
          f"· junctions={n_j_ok}/{len(JUNCTIONS)} · domains={'ok' if d_ok else 'FAIL'} "
          f"· harness_fail={n_h_fail})")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
