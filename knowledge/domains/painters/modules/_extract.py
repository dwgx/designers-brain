#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A-19 模块库 · 抽取与逐字校验工具（只读档案；只写本目录）
================================================================
从 11 份画家档案（knowledge/domains/painters/dossiers/<id>.md）抽取：
  - §8.1 图像 prompt：正向段 + 负向段（英文，原样）
  - §8.2 代码艺术规则：原样（含 [归纳] 等标注与尾注）
  - §4   控制参数：原样（含 [归纳] 等标注与用法注）
生成可组合模块卡 <id>.md；视觉指纹为 §1 浓缩 5 条；冲突注记指向
knowledge/cross/conflicts.md 相关 C 条。

用法：
  python _extract.py --write               # 生成/重建 11 张模块卡
  python _extract.py --check               # 逐字校验：卡片 §8.1/§8.2/§4 vs 档案
  python _extract.py --diff <id> [--sec 81|82|4] [--full]
                                           # 单卡比对详情（--full 附原样全文）

口径：只搬运与浓缩，不改档案；§8.1/§8.2/§4 与档案逐字一致（--check 复核）。

§8.1b（E-02 派生补充，2026-10-15）：卡内「## §8.1b」节非档案内容——--check 时 §8.1 段
在 §8.1b 处截断后与档案比对；--write 重建时原样保留现有卡内的 §8.1b 节。
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = Path(__file__).resolve().parent          # knowledge/domains/painters/modules
ROOT = HERE.parents[3]                          # 项目根 Designers_Brain
ARCH = ROOT / "knowledge" / "domains" / "painters" / "dossiers"

# ---------------------------------------------------------------------------
# 数据：每张卡的元信息 / 指纹浓缩（自档案 §1）/ 冲突注记（→ conflicts.md）
# 注：§8.1 / §8.2 / §4 正文一律从档案机械抽取，不在此处维护。
# ---------------------------------------------------------------------------
ARTISTS = [
    {
        "id": "da_vinci", "name": "达·芬奇", "n": 10,
        "fingerprint": [
            "**无轮廓线**：亮暗过渡为宽而连续的灰色带，无「勾线＋填色」边界——sfumato 招牌",
            "**烟式中间调**：灰层次极多、深色不脏、亮部不闪，整体像隔一层薄雾",
            "**窄色域、低饱和**：同屏色相少（晚期主为蓝／黄／棕三家族）；人物从暗部「浮」出",
            "**空气透视**：远景转蓝、边缘化开、对比下降——山体像被雾吃掉一截",
            "**谜样表情＋微扭转**：微笑停在「将笑未笑」；三／四分之三姿势「转身到一半」；卷发呈连续带状（绳结纹样）",
        ],
        "conflicts": [
            ("C-02", "× 米开朗基罗；本卡 §8.2-1/-2", "明暗过渡带宽度（≥1.5% vs ≤0.6% 短边）"),
            ("C-03", "× 卡拉瓦乔；本卡 §8.2-3", "直方图/中间调（≥55% vs ≤25%）"),
            ("C-05", "× 梵高 / 莫奈 / 塞尚；本卡 §8.2-7", "笔触可见度（只有渐变 vs ≥95% 笔触覆盖）"),
            ("C-06", "× 马蒂斯；本卡 §8.2-4，同侧旁证组", "饱和度（每块 ≥70% vs 全帧 ≤35%）"),
            ("C-14", "× Lane B 06/07/13 卡反约束；本卡 §8.2-2/-7", "渐变（禁令 vs sfumato/包络）"),
        ],
        "nearmiss": "#4（饱和度上限组：达·芬奇/毕加索/莫奈/米开朗基罗 → 取 ≤0.35）",
    },
    {
        "id": "michelangelo", "name": "米开朗基罗", "n": 10,
        "fingerprint": [
            "**人体即舞台**：肌肉分明的裸体主导画面；第一眼是敬畏（terribilità），不是优美",
            "**扭转体**：肩线—髋线反向扭动、脊柱成 S 形；《最后的审判》整面墙呈「缓慢的旋转运动」",
            "**雕塑性明暗**：形体像被「凿」出，硬边阴影、浮雕感",
            "**仰视放大＋密集人群**：下排人物剧烈透视缩短；满构图人群绕中心涡旋（天顶 300 余人）",
            "**英雄化裸体＋明亮湿壁画色**：超常肌群、无视惯例的裸体基督；肉色／土黄／暗绿／青蓝四族",
        ],
        "conflicts": [
            ("C-01", "× Lane B 模板「硬阴影」禁令；本卡 §8.2-3", "阴影硬度（种子案例；反约束句须改写）"),
            ("C-02", "× 达·芬奇；本卡 §8.2-3", "明暗过渡带宽度（≤0.6% vs ≥1.5% 短边）"),
            ("C-17", "× 北斋 / 马蒂斯；本卡 §8.2-4", "负空间（≤15% vs ≥35% / ≥20%）"),
            ("C-18", "× 毕加索 / 马蒂斯；本卡 §4 浮雕强度 + §8.2-3", "形体塑造（浮雕 vs 平涂）"),
        ],
        "nearmiss": "#4（饱和度 → ≤0.35）、#7（与维米尔「物体边缘」量纲不同，需写清测量对象）",
    },
    {
        "id": "van_gogh", "name": "梵高", "n": 10,
        "fingerprint": [
            "**厚涂＋可见笔触**：颜料堆到压出画布纹理；笔触方向分区（天空漩涡／地面短笔／树火焰状上升）",
            "**互补色对置**：黄-蓝、橙-蓝成对并置，靠笔触并置产生「振动」",
            "**高彩度黄蓝主导、少渐变**：色块直接并置，不做平滑过渡",
            "**母题象征化与放大**：星月加同心光环；柏树贯穿近画顶",
            "**浅空间／平面化**：日本版画式裁切与非对称构图；线条书写趣味强",
        ],
        "conflicts": [
            ("C-05", "× 达·芬奇；本卡 §8.2-3 + §8.2-7", "笔触可见度（≥95% 覆盖 vs 只有渐变）"),
            ("C-09", "× 维米尔；本卡 §8.2-4/-5", "运动预算（全画面场 2–6°/s vs 事件外 Δ≤1%）"),
            ("C-12", "× 北斋 / 卡拉瓦乔；本卡 §4 P3 + §8.2-2", "色相面积预算（互补对近 1:1 vs 蓝 ≥40% / 土色系）"),
        ],
        "nearmiss": None,
    },
    {
        "id": "monet", "name": "莫奈", "n": 10,
        "fingerprint": [
            "**短逗号笔触、并置不混合**：高调浅色底；笔触「一笔一笔放上去」（示范间距约 1 英寸、厚 0.25 英寸）",
            "**有色阴影、无黑**：阴影蓝紫（蓝天反射），不用黑",
            "**大气包络**：同一道光铺满全画（enveloppe）；远景对比下降",
            "**水面／天空镜像母题**：非对称、去线性透视、平面化",
            "**系列重复**：同一母题 × 不同时刻／天气（干草堆／白杨／鲁昂大教堂）",
        ],
        "conflicts": [
            ("C-05", "× 达·芬奇；本卡 §8.2-1", "笔触可见度（90–100% 覆盖 vs 只有渐变）"),
            ("C-06", "× 马蒂斯；本卡 §8.2-3，同侧旁证组", "饱和度（每块 ≥70% vs 全帧 ≤35%）"),
            ("C-10", "× 塞尚；本卡 §4 P3 + §8.2-4", "深度衰减（大气包络 vs 反大气透视）"),
            ("C-14", "× Lane B 06/07/13 卡反约束；本卡 §8.2-4", "渐变（禁令 vs 雾色渐变）"),
        ],
        "nearmiss": "#4（饱和度上限组 → 取 ≤0.35）",
    },
    {
        "id": "picasso", "name": "毕加索", "n": 12,
        "fingerprint": [
            "**面片化边缘**：形体碎成 10°–40° 折角的「水晶切面」；浅浮雕空间",
            "**多视点同框**：同一物体的正面／侧面／俯视被同时画出",
            "**近单色棕灰域**：赭／灰／棕／黑、低饱和；明度中心亮（暗环包亮心）",
            "**平涂无渐变**：面片互相咬合如拼图；体量靠角度差与明度跳变，不靠明暗",
            "**锚点残留＋材料入侵**：3–5 个具象锚点（发浪／领结／表链）；字母、乐谱、报纸、木纹进入画面",
        ],
        "conflicts": [
            ("C-06", "× 马蒂斯；本卡 §8.2-1", "饱和度（全帧 ≤35% vs 每块 ≥70%）"),
            ("C-16", "× Lane B 02 卡反约束；本卡 §8.2-6", "反约束适用域（「没有高光的平涂」误伤平涂系）"),
            ("C-18", "× 米开朗基罗；本卡 §4 P3 + §8.2-6", "形体塑造（平涂 vs 浮雕）"),
        ],
        "nearmiss": "#4（饱和度上限组 → 取 ≤0.35）、#5（色相上限组 → 取 ≤5）",
    },
    {
        "id": "cezanne", "name": "塞尚", "n": 12,
        "fingerprint": [
            "**离散笔触（tache）铺满全画面**：按局部结构成组（4–8 个方向族）",
            "**色阶代替明暗**：红↔绿色阶塑形、无黑阴影；暖冷交错编织",
            "**轮廓破碎与多重线**：一物常 2–3 条轮廓，形体互渗；蓝网贯穿（阴影／轮廓／天空）",
            "**反大气透视＋空间压缩**：远近同尺度、视点游移、透视不自洽",
            "**几何化块面＋未完成感**：裸露画布／骨架线，作品停在「进行中」",
        ],
        "conflicts": [
            ("C-04", "× 卡拉瓦乔；本卡 §8.2-7", "直方图单桶上限（无 >20% vs 暗带 ≥40%＋背景均匀）"),
            ("C-05", "× 达·芬奇；本卡 §8.2-1", "笔触可见度（≥80% 覆盖 vs 只有渐变）"),
            ("C-10", "× 莫奈；本卡 §4 P4 + §8.2-5", "深度衰减（反大气透视 vs 大气包络）"),
            ("C-13", "× 卡拉瓦乔；本卡 §8.2-4", "阴影色相（蓝 ≥15% vs 深棕黑暗部）"),
        ],
        "nearmiss": None,
    },
    {
        "id": "matisse", "name": "马蒂斯", "n": 10,
        "fingerprint": [
            "**平涂色块**：内部明度变化 ≤5%、无描边无投影；剪裁硬边（直线段＋圆弧）",
            "**色相少而纯**：5–8 个高纯度色、互补对撞；黑与彩同权",
            "**空间＝色面积与方向**：无消失点；所有曲线回应隐含垂直轴",
            "**留白是主角**：纸／底色可见 ≥20%；缩略图（64px）仍可读",
            "**图案与主体同权**：纹样与人体同一平面处理；剪纸形状跨作品复用",
        ],
        "conflicts": [
            ("C-06", "× 毕加索 / 达·芬奇 / 莫奈；本卡 §4 P1 + §8.2-1", "饱和度（每块 ≥70% vs 全帧 ≤35%）"),
            ("C-15", "× Lane B 色数上限（克里姆特类缺口）；本卡 §4 P4 边界注 + §8.2-8", "色数计数口径（≤3 色 vs 金属/金箔层）"),
            ("C-16", "× Lane B 02 卡反约束；本卡 §8.2-1/-2", "反约束适用域（「没有高光的平涂」误伤平涂系）"),
            ("C-17", "× 米开朗基罗；本卡 §8.2-5", "负空间（≥20% vs ≤15%）"),
            ("C-18", "× 米开朗基罗；本卡 §4 P3 + §8.2-2", "形体塑造（平涂 vs 浮雕）"),
        ],
        "nearmiss": None,
    },
    {
        "id": "hokusai", "name": "葛饰北斋", "n": 10,
        "fingerprint": [
            "**线为骨架**：等宽、连续、无排线的轮廓线；色块贴线平涂",
            "**普鲁士蓝主导**：蓝系常占 ≥40% 面积（1830 年代「蓝色革命」）",
            "**非对称＋单条强斜线**：主体从不居中；尺度戏法（远景富士被压到 ≤ 前景 1/4）",
            "**曲线族／螺旋**：大浪生成小浪、小浪生成波纹（≥3 级嵌套）；负空间 ≥35%",
            "**人＝剪影＋极简线**（≤6 条/人）；装饰图案与写实同画面；留纸当高光",
        ],
        "conflicts": [
            ("C-07", "× 丢勒；本卡 §8.2-1/-2/-6", "表面着色系统（平涂 vs 排线）"),
            ("C-12", "× 卡拉瓦乔 / 梵高；本卡 §4 P1 + §8.2-2", "色相面积预算（蓝 ≥40% vs 土色系 / 互补对 1:1）"),
            ("C-16", "× Lane B 02 卡反约束；本卡 §8.2-1/-6", "反约束适用域（「没有高光的平涂」误伤平涂系）"),
            ("C-17", "× 米开朗基罗；本卡 §4 P6 + §8.2-6", "负空间（≥35% vs ≤15%）"),
        ],
        "nearmiss": "#5（色相上限组 → 取 ≤5）、#6（线宽恒定，与丢勒/08 卡同侧）",
    },
    {
        "id": "caravaggio", "name": "卡拉瓦乔", "n": 10,
        "fingerprint": [
            "**单光源、无反射、背景近黑**：光从画外高处来；画面内可见光源数 = 0",
            "**两级明暗（tenebrism）**：中间调被压缩（直方图双峰）；暗部非死黑——深棕底作中间调",
            "**人物贴住画面平面**：被边缘裁切；手势是叙事主语，光斑只落脸／手／道具",
            "**反理想化人体＋当代服装**：脏指甲、破衣缝当圣徒；定格瞬间（无运动模糊）",
            "**色域收窄**：赭／红棕／铅白／黑土色系；深色底参与塑形（亮部在其上「塑出」）",
        ],
        "conflicts": [
            ("C-01", "× Lane B 模板「硬阴影」禁令；本卡 §4 P1 + §8.2-1", "阴影硬度（种子案例；反约束句须改写）"),
            ("C-03", "× 达·芬奇；本卡 §4 P3 + §8.2-3", "直方图/中间调（≤25% vs ≥55%）"),
            ("C-04", "× 塞尚；本卡 §8.2-2/-3", "直方图单桶上限（暗带 ≥40% vs 无 >20%）"),
            ("C-08", "× Lane B「运动模糊」禁令；本卡 §8.2-6", "运动模糊（定格 = 全片 0 帧）"),
            ("C-11", "× 维米尔；本卡 §8.2-4", "高光计数（[2,5] vs 100+ 点）"),
            ("C-12", "× 北斋 / 梵高；本卡 §4 P5 + §8.1", "色相面积预算（土色系收窄 vs 蓝 ≥40% / 互补对 1:1）"),
            ("C-13", "× 塞尚；本卡 §4 P5 + §8.2-2/-7", "阴影色相（深棕黑 vs 蓝 ≥15%）"),
        ],
        "nearmiss": "#1/#2/#3/#8（× 维米尔，需显式取值）",
    },
    {
        "id": "vermeer", "name": "维米尔", "n": 12,
        "fingerprint": [
            "**单一左侧窗光、高调**：大面积浅灰白墙面接光",
            "**点状高光（pointillés）**：1–3mm 圆点厚涂亮点；暗部平坦（大块无变化色面）",
            "**冷调阴影**：蓝／绿而非黑；群青蓝 × 赭黄主色对，红只作小点缀",
            "**无硬线（sfumato）、细节主动省略**；材质靠高光形状区分；表面平滑（织纹不可见）",
            "**人物 1–2 人、动作冻结**；房间几何网格（地砖＋窗框单点透视）",
        ],
        "conflicts": [
            ("C-08", "× Lane B「运动模糊」禁令；本卡 §8.2-8", "运动模糊（定格 = 全片 0 帧）"),
            ("C-09", "× 梵高；本卡 §8.2-8", "运动预算（事件外 Δ≤1% vs 全画面场）"),
            ("C-11", "× 卡拉瓦乔；本卡 §4 P3 + §8.2-3", "高光计数（100+ 点 vs [2,5] 连通域）"),
        ],
        "nearmiss": "#1/#2/#3/#8（× 卡拉瓦乔）、#5（× 北斋/毕加索）、#7（× 米开朗基罗）",
    },
    {
        "id": "durer", "name": "丢勒", "n": 10,
        "fingerprint": [
            "**排线即明度**：所有「灰」由线密度合成；几乎无实心涂黑（实心填充 ≤5%）",
            "**排线随形体弯曲**（包裹形体）；线端收锋（中段鼓、端点尖）",
            "**硬轮廓、无渐变**（与达·芬奇机制相反）；细节全幅均匀（逐根毛发／逐片草叶）",
            "**微观观察视角**：对象占满画面；象征物密集堆叠（≥8 件静止陈列）",
            "**数理秩序＋签名系统**：头身比／透视可见；AD 花押与年份几乎总在版上",
        ],
        "conflicts": [
            ("C-07", "× 北斋；本卡 §4 P1/P2 + §8.2-1/-3/-7", "表面着色系统（排线 vs 平涂）"),
        ],
        "nearmiss": "#6（线宽恒定，与北斋/08 卡同侧）",
    },
]

# ---------------------------------------------------------------------------
# 抽取工具
# ---------------------------------------------------------------------------

def read_lines(p: Path):
    raw = p.read_bytes().decode("utf-8")
    lines = raw.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    return lines


def trim(seg):
    seg = list(seg)
    while seg and not seg[0].strip():
        seg.pop(0)
    while seg and (not seg[-1].strip() or seg[-1].strip() == "---"):
        seg.pop()
    return seg


def _find(lines, pred, start=0):
    for i in range(start, len(lines)):
        if pred(lines[i]):
            return i
    raise ValueError("marker not found: %r" % lines[:3])


def extract(lines, start_pred, end_pred, cut_pred=None):
    i = _find(lines, start_pred)
    j = _find(lines, end_pred, i + 1)
    seg = lines[i + 1:j]
    if cut_pred is not None:
        k = _find(seg, cut_pred)
        seg = seg[:k]
    return "\n".join(trim(seg))


def arch_81(lines):
    return extract(lines,
                   lambda l: l.startswith("### 8.1"),
                   lambda l: l.startswith("### 8.2"),
                   lambda l: l.startswith("**中文使用说明"))


def arch_82(lines):
    return extract(lines,
                   lambda l: l.startswith("### 8.2"),
                   lambda l: l.startswith("### 8.3"))


def arch_4(lines):
    return extract(lines,
                   lambda l: l.startswith("## 4."),
                   lambda l: l.startswith("## 5."))


def card_81(lines):
    i = _find(lines, lambda l: l.startswith("## 图像 prompt"))
    j = _find(lines, lambda l: l.startswith("## 代码艺术规则"), i + 1)
    seg = lines[i + 1:j]
    for k, ln in enumerate(seg):
        if ln.startswith("## §8.1b"):
            seg = seg[:k]
            break
    return "\n".join(trim(seg))


def card_82(lines):
    return extract(lines,
                   lambda l: l.startswith("## 代码艺术规则"),
                   lambda l: l.startswith("## 控制参数"))


def card_4(lines):
    return extract(lines,
                   lambda l: l.startswith("## 控制参数"),
                   lambda l: l.startswith("## 冲突注记"))


def s81b_from_card(lines):
    """卡内 §8.1b 节（若存在）——从 '## §8.1b' 起、至下一个 '## ' 级标题前（原样）。"""
    i = None
    for idx, l in enumerate(lines):
        if l.startswith("## §8.1b"):
            i = idx
            break
    if i is None:
        return None
    j = len(lines)
    for idx in range(i + 1, len(lines)):
        if lines[idx].startswith("## "):
            j = idx
            break
    return "\n".join(trim(lines[i:j]))


# ---------------------------------------------------------------------------
# 渲染
# ---------------------------------------------------------------------------

CARD_TMPL = """# {name} 模块卡 — `{id}`

> A-19 模块库 ｜ 来源：档案 `knowledge/domains/painters/dossiers/{id}.md`（§1 浓缩 + §8.1 / §8.2 / §4 原样）
> 组合与冲突：先读 `knowledge/cross/conflicts.md` 对应 C 条与 §3 N1/N3/N6；用法见本目录 `README.md`
> 逐字校验：`python _extract.py --check`（本卡 §8.1 / §8.2 / §4 与档案逐字一致）

## 视觉指纹要点（浓缩 5 条；自档案 §1 原 {n} 条）

{fp}

## 图像 prompt（§8.1 原样）

{s81}
{s81b_block}## 代码艺术规则（§8.2 原样）

{s82}

## 控制参数（§4 原样）

{s4}

## 冲突注记（→ conflicts.md）

组合前先读 `knowledge/cross/conflicts.md` 对应条目（处置口径以该文件为准；通用规则见其 §3 N1–N9）：

{conflicts}

## 来源

- 档案（唯一正本）：`knowledge/domains/painters/dossiers/{id}.md` —— 本卡抽取自其 §1（浓缩 5 条）、§8.1、§8.2、§4
- 冲突清单：`knowledge/cross/conflicts.md`（18 条 C + N1–N9 + near-miss 8 对）
- 模块库说明：`knowledge/domains/painters/modules/README.md`
"""


def render_card(a, s81, s82, s4, s81b=None):
    fp = "\n".join("%d. %s" % (i + 1, x) for i, x in enumerate(a["fingerprint"]))
    cfs = ["- **%s**（%s）：%s" % (cid, scope, axis) for cid, scope, axis in a["conflicts"]]
    if a.get("nearmiss"):
        cfs.append("- **near-miss（conflicts.md §4 表）**：%s" % a["nearmiss"])
    s81b_block = ("\n" + s81b + "\n\n") if s81b else "\n"
    return CARD_TMPL.format(name=a["name"], id=a["id"], n=a["n"], fp=fp,
                            s81=s81, s81b_block=s81b_block, s82=s82, s4=s4,
                            conflicts="\n".join(cfs))


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# 模式
# ---------------------------------------------------------------------------

def write_cards():
    count = 0
    for a in ARTISTS:
        lines = read_lines(ARCH / ("%s.md" % a["id"]))
        s81, s82, s4 = arch_81(lines), arch_82(lines), arch_4(lines)
        old = HERE / ("%s.md" % a["id"])
        s81b = s81b_from_card(read_lines(old)) if old.exists() else None
        text = render_card(a, s81, s82, s4, s81b=s81b)
        if not text.endswith("\n"):
            text += "\n"
        (HERE / ("%s.md" % a["id"])).write_bytes(text.encode("utf-8"))
        print("wrote %s.md  (§8.1 %dc · §8.2 %dc · §4 %dc%s)" %
              (a["id"], len(s81), len(s82), len(s4),
               " · §8.1b %dc" % len(s81b) if s81b else ""))
        count += 1
    print("done: %d cards -> %s" % (count, HERE))


def check_all():
    total = ok = 0
    for a in ARTISTS:
        alines = read_lines(ARCH / ("%s.md" % a["id"]))
        clines = read_lines(HERE / ("%s.md" % a["id"]))
        parts = []
        for key, xs, ys in (("§8.1", arch_81(alines), card_81(clines)),
                            ("§8.2", arch_82(alines), card_82(clines)),
                            ("§4", arch_4(alines), card_4(clines))):
            total += 1
            good = xs == ys
            ok += 1 if good else 0
            parts.append("%s %s (%dc)" % (key, "ok" if good else "FAIL", len(ys)))
            if not good:
                print("!! %s %s mismatch" % (a["id"], key))
        print("[%s] %s" % (a["id"], " · ".join(parts)))
    print("checks=%d ok=%d fail=%d   # 11 卡 × §8.1/§8.2/§4 逐字比对" % (total, ok, total - ok))


def diff_one(aid, full=False, sec=None):
    a = next((x for x in ARTISTS if x["id"] == aid), None)
    if a is None:
        print("unknown id: %s" % aid)
        return
    alines = read_lines(ARCH / ("%s.md" % aid))
    clines = read_lines(HERE / ("%s.md" % aid))
    pairs = [("81", "§8.1", arch_81(alines), card_81(clines)),
             ("82", "§8.2", arch_82(alines), card_82(clines)),
             ("4", "§4", arch_4(alines), card_4(clines))]
    for key, label, xs, ys in pairs:
        if sec and key != sec:
            continue
        print("== %s ｜ %s 逐字比对 ==" % (aid, label))
        print("  archive: %d lines / %d chars / sha256=%s" % (xs.count("\n") + 1, len(xs), sha(xs)))
        print("  card:    %d lines / %d chars / sha256=%s" % (ys.count("\n") + 1, len(ys), sha(ys)))
        print("  verdict: %s" % ("IDENTICAL（逐字一致）" if xs == ys else "DIFF（不一致！）"))
        if xs == ys:
            print("  unified-diff: (empty — 0 处差异)")
        else:
            import difflib
            for d in difflib.unified_diff(xs.split("\n"), ys.split("\n"), lineterm=""):
                print("  " + d)
        if full:
            print("  ---- 原样文本 ----")
            print(ys)
        print()


def main():
    args = sys.argv[1:]
    if not args or "--help" in args:
        print(__doc__)
        return
    if "--write" in args:
        write_cards()
    elif "--check" in args:
        check_all()
    elif "--diff" in args:
        i = args.index("--diff")
        aid = args[i + 1] if i + 1 < len(args) else ""
        sec = args[args.index("--sec") + 1] if "--sec" in args else None
        diff_one(aid, full="--full" in args, sec=sec)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
