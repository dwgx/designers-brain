#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""walkthrough_01 · 提示词构建（S-05 真实需求走查 · 演练版）

- 从模块卡（research/prompts/artist_modules/*.md）逐字提取 §8.1 正向段 / 负向段
  （仅归一化空白：多行 → 单行、连续空白 → 单空格；文本内容不改），作为 main_segment。
- 按配方组装：prompt = 主题句 + [融合句] + 主段 [+ 轴归属句]。
- 写入/合并 prompts.json（按 name 合并：保留既有 result 字段，不覆盖出图结果）。

用法:
  python _build_w01.py candidates   # 写 3 个候选 job（候选1/2/3）
  python _build_w01.py final        # 追加/更新定稿 job（在候选出图、客户选定之后运行）
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
CARDS = os.path.join(REPO, "research", "prompts", "artist_modules")
PROMPTS = os.path.join(HERE, "prompts.json")

MODEL = "grok-imagine-image-2.0"
ENDPOINT = "http://192.168.11.4:3000/v1/images/generations"
SIZE = "1024x1536"


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def extract_block(text, marker):
    i = text.index(marker)
    m = re.search(r"```\n(.*?)```", text[i:], re.S)
    if not m:
        raise SystemExit("FATAL: no code block after %r" % marker)
    return re.sub(r"\s+", " ", m.group(1)).strip()


def card_segments(card_id):
    path = os.path.join(CARDS, card_id + ".md")
    t = open(path, encoding="utf-8").read()
    pos = extract_block(t, "正向段（可直接粘贴）")   # 首个出现 = §8.1（§8.1b 在后）
    neg = extract_block(t, "负向约束")
    return pos, neg


def build_job(name, role, direction, out, theme, main_id, strength,
              fusion=None, axis=None, aux_source=None, card_refs=None,
              neg_note=None, neg_remove=None):
    pos, neg = card_segments(main_id)
    parts = [theme]
    if fusion:
        parts.append(fusion)
    parts.append(pos)
    if axis:
        parts.append(axis)
    prompt = " ".join(parts)
    neg_archived = neg
    if neg_remove:
        for frag in neg_remove:
            neg_archived = neg_archived.replace(frag, "").replace("  ", " ").strip(" ,")
    return {
        "name": name,
        "role": role,
        "direction": direction,
        "out": out,
        "theme": theme,
        "fusion": fusion,
        "axis_note": axis,
        "main_card": main_id,
        "main_segment": pos,
        "main_segment_sha256": sha(pos),
        "aux_source": aux_source,
        "strength": strength,
        "negative_archived": neg_archived,
        "negative_removed_n1": neg_remove or [],
        "negative_sent": False,
        "negative_note": neg_note or "通道无负向参数（B-20 实测）——负向段只留档、不随请求发送",
        "card_refs": card_refs or [],
        "prompt": prompt,
        "prompt_sha256": sha(prompt),
    }


def candidates_jobs():
    j1 = build_job(
        name="cand1_monet_dawn",
        role="candidate",
        direction="方向 A · 晨光（莫奈 单模块）",
        out="candidates",
        theme=("A small independent cafe opening visual: a quiet street-side cafe corner at early "
               "morning, a small round table beside a tall window, one ceramic cup of coffee with "
               "gentle rising steam, soft hazy light after rain, warm broken reflections on the "
               "wet pavement."),
        main_id="monet",
        strength=("单模块 · §4 默认档起步：P1 70% / P2 65% / P3 50% / P4 60%；"
                  "P5（水面占比）本场景无水面——不适用，湿地面倒影承接其精神（如实注记）"),
        card_refs=["monet.md §8.1 正向段（逐字）", "monet.md §4（默认档）", "monet.md §8.2-1/2/3（非冲突轴自查）"],
    )
    j2 = build_job(
        name="cand2_vermeer_monet_windowlight",
        role="candidate",
        direction="方向 B · 窗光（维米尔 70% × 莫奈 30%）",
        out="candidates",
        theme=("A small cafe opening visual: the quiet everyday moment of pouring steamed milk from "
               "a small pitcher into a ceramic cup of coffee, at a wooden table beside a tall "
               "window on the left; one person seen from the side at close range, absorbed in the "
               "action; a small pastry on a plate; gentle steam rising; soft daylight."),
        main_id="vermeer",
        fusion=("Fusion of two painterly languages: Johannes Vermeer dominant (70%), "
                "Claude Monet secondary (30%)."),
        axis=("Claude Monet contributes only the atmospheric envelope: in the far distance the "
              "contrast is compressed and all colour is gathered toward one soft airy warm tone; "
              "no broken brushwork and no comma strokes."),
        aux_source=("档案 vermeer.md §8.3 组合建议（派生句；非 §8.1 逐字——莫奈笔触段与维米尔表面轴同轴冲突，"
                    "按 N3 整条移除，仅保留「大气包络」轴）"),
        strength=("主·维米尔 §4 默认：P1 75% / P2 70% / P3 80%（静物·器物档）/ P4 60% / P5 80% / P6 85%；"
                  "辅·莫奈仅大气包络轴（P3 默认 50%），笔触轴规则按 N3 整条移除"),
        neg_note=("通道无负向参数——负向段只留档、不随请求发送；N1 重算：莫奈负向「smooth blending」"
                  "与维米尔正向「smooth levigated paint surface」冲突 → 整条移除；其余莫奈负向条均与维米尔一致，保留"),
        neg_remove=["smooth blending"],
        card_refs=["vermeer.md §8.1 正向段（逐字）", "vermeer.md §8.3（组合建议）", "vermeer.md §4（默认档）",
                   "conflicts.md §3 N1/N3/N4/N9", "conflicts.md §4 near-miss #4/#5（取值）"],
    )
    j3 = build_job(
        name="cand3_matisse_colorblocks",
        role="candidate",
        direction="方向 C · 色块（马蒂斯 单模块）",
        out="candidates",
        theme=("A small cafe opening poster: a large warm sun disc above a simple ceramic cup of "
               "coffee, with a leaf, a star and flowing organic shapes gathering around a beam of "
               "warm light, on a cream paper ground."),
        main_id="matisse",
        strength=("P1 65%（油画期档；卡默认 85% 剪纸期——因客户「别太花哨」调档，说出口可否决）/ "
                  "P2 7 色 / P3 80% / P5 90% / P6 70%"),
        card_refs=["matisse.md §8.1 正向段（逐字）", "matisse.md §4（P1 调档）"],
    )
    return [j1, j2, j3]


def final_job():
    """定稿 job：候选 2 方向选定后的定稿版（含候选阶段观察到的微调；见 dialogue.md）。"""
    theme = ("A small cafe opening visual: the quiet everyday moment of pouring steamed milk from "
             "a small pitcher into a ceramic cup of coffee, at a wooden table beside a tall "
             "window on the left; one person seen from the side at close range, absorbed in the "
             "action; a small pastry on a plate; gentle steam rising; soft warm morning daylight; "
             "warm light pooling across the table top and the pale wall.")
    j = build_job(
        name="final_vermeer_monet_windowlight",
        role="final",
        direction="定稿 · 窗光（维米尔 70% × 莫奈 30%）",
        out="final",
        theme=theme,
        main_id="vermeer",
        fusion=("Fusion of two painterly languages: Johannes Vermeer dominant (70%), "
                "Claude Monet secondary (30%)."),
        axis=("Claude Monet contributes only the atmospheric envelope: in the far distance the "
              "contrast is compressed and all colour is gathered toward one soft airy warm tone; "
              "no broken brushwork and no comma strokes."),
        aux_source=("档案 vermeer.md §8.3 组合建议（派生句；非 §8.1 逐字——莫奈笔触段与维米尔表面轴同轴冲突，"
                    "按 N3 整条移除，仅保留「大气包络」轴）"),
        strength=("主·维米尔 §4 默认：P1 75% / P2 70% / P3 80%（静物·器物档）/ P4 60% / P5 80% / P6 85%；"
                  "辅·莫奈仅大气包络轴（P3 默认 50%），笔触轴规则按 N3 整条移除"),
        neg_note=("通道无负向参数——负向段只留档、不随请求发送；N1 重算：莫奈负向「smooth blending」"
                  "与维米尔正向「smooth levigated paint surface」冲突 → 整条移除；其余莫奈负向条均与维米尔一致，保留"),
        neg_remove=["smooth blending"],
        card_refs=["vermeer.md §8.1 正向段（逐字）", "vermeer.md §8.3（组合建议）", "vermeer.md §4（默认档）",
                   "conflicts.md §3 N1/N3/N4/N9", "conflicts.md §4 near-miss #4/#5（取值）",
                   "dialogue.md · 候选 2 观察 → 定稿微调记录"],
    )
    return j


def merge_write(jobs):
    if os.path.exists(PROMPTS):
        doc = json.load(open(PROMPTS, encoding="utf-8"))
    else:
        doc = {
            "task": "S-05 · 真实需求走查（演练版）·「拾光」咖啡馆开业主视觉",
            "date": "2026-10-15",
            "model": MODEL,
            "endpoint": ENDPOINT,
            "size_requested": SIZE,
            "channel_notes": {
                "bare_model_name": True,
                "negative_channel": "无（负向段只留档、不发送）",
                "size_actual": "768x1152（实测；请求 1024x1536 不严格兑现）",
                "ref": "research/agent-art/cards/image_channel.md（B-20）",
            },
            "jobs": [],
        }
    by_name = {j["name"]: j for j in doc.get("jobs", [])}
    for j in jobs:
        old = by_name.get(j["name"])
        if old and "result" in old:
            j["result"] = old["result"]           # 保留出图结果
        by_name[j["name"]] = j
    order = [j["name"] for j in jobs] + [n for n in by_name if n not in {j["name"] for j in jobs}]
    doc["jobs"] = [by_name[n] for n in order]
    with open(PROMPTS, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    return doc


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "candidates"
    if mode == "candidates":
        jobs = candidates_jobs()
    elif mode == "final":
        jobs = [final_job()]
    else:
        raise SystemExit("usage: python _build_w01.py [candidates|final]")
    doc = merge_write(jobs)
    for j in doc["jobs"]:
        if j["name"] in {x["name"] for x in jobs}:
            print("[build] %s | prompt_sha256=%s | len=%d" % (j["name"], j["prompt_sha256"][:12], len(j["prompt"])))
    print("[build] prompts.json jobs=%d" % len(doc["jobs"]))


if __name__ == "__main__":
    main()
