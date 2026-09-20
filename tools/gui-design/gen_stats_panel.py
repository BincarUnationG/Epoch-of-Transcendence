#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""位阶·属性面板 —— 嵌进原版背包右上角被擦除的合成区。

可用区域实测（基于 inventory2.png 逐像素扫描）：
    x = 76..172, y = 7..78   →  97 x 72
    左界 x = 75 是玩家预览区边框；右界 x = 173..174 是面板阴影 #555555
    原合成区被擦除后仍留有 #C5C5C5 与零散单像素残留（x=82/90/93/125/144/153/170 一带）
    → 本纹理是「实心底」，贴上去可把残留一并覆盖

像素语言沿用原版 inventory.png：
    面板底 #C6C6C6（三份主题统一，否则会与背包出现色块边界）
    凹槽 = 左上 1px 暗边 + 内容 + 右下 1px 亮边
    刻线 = 1px #555555 + 1px #FFFFFF

面板内部布局（相对坐标，97 x 72）：
    y = 0..7     顶部：境界徽记（文字「位阶 · 传说 3/9」由代码绘制在 x=12 起）
    y = 10..17   位阶刻度尺：10 个 8x8 凹槽，x = 4 + i*9（i=0 是最左）
    y = 19..20   刻线
    y = 22..28   晋升进度条凹槽（89 x 7，代码填进度）
    y = 30..31   刻线
    y = 32..67   属性区：4 行（每行 9px），两列文字起点 x = 4 与 x = 48
    y = 68..71   留白

刻度尺方向：最左 = 9 阶（起点），最右 = 0 阶（目标）。
玩家 level 越小越强，所以「已走过」在左侧、「未达到」在右侧，读起来就是一条自左向右的进度。

生成物（common/src/main/resources/assets/epoch_of_transcendence/textures/gui/）：
    rank_stats_mortal.png    97x72
    rank_stats_legend.png    97x72
    rank_stats_mythic.png    97x72

用法：g.blit(tex, guiLeft + 76, guiTop + 7, 0, 0, 97, 72);
"""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_rank_gui import Canvas, HIGHLIGHT, THEMES, glyph, inset  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "common" / "src" / "main" / "resources" / "assets" / "epoch_of_transcendence" / "textures" / "gui"
PREVIEW_DIR = Path(__file__).resolve().parent / "preview"

# ---------------------------------------------------------------- 布局常量
SW, SH = 97, 72                  # 纹理尺寸 = 可用区域尺寸
ANCHOR = (76, 7)                 # 在 176x166 背包面板中的 blit 坐标

PANEL_BG = (198, 198, 198, 255)  # 必须与背包面板一致

GLYPH_X, GLYPH_Y = 4, 1          # 境界徽记 6x6
GAUGE_X, GAUGE_Y = 4, 10         # 刻度尺起点
GAUGE_N, GAUGE_CELL, GAUGE_GAP = 10, 8, 1
RULE_X0, RULE_X1 = 4, 92
RULE1_Y = 19
BAR = (4, 22, 89, 7)             # x, y, w, h
RULE2_Y = 30
STATS_Y = 32                     # 属性区首行 y
STATS_LINE = 9                   # 行距（= MC 字体 lineHeight）
STAT_COL_X = (4, 48)             # 两列文字起点


def rule(c, t, y):
    c.hline(RULE_X0, RULE_X1, y, t["shadow"])
    c.hline(RULE_X0, RULE_X1, y + 1, HIGHLIGHT)


def make_stats(name):
    t = THEMES[name]
    c = Canvas(SW, SH)
    # 实心底：与背包面板同色，同时覆盖擦除残留
    c.rect(0, 0, SW - 1, SH - 1, PANEL_BG)
    # 顶部境界徽记
    glyph(c, name, GLYPH_X, GLYPH_Y, t["accent"], t["accent_dim"])
    # 位阶刻度尺：10 个 8x8 凹槽
    for i in range(GAUGE_N):
        inset(c, t, GAUGE_X + i * (GAUGE_CELL + GAUGE_GAP), GAUGE_Y,
              GAUGE_CELL, GAUGE_CELL, t["slot_bg"])
    rule(c, t, RULE1_Y)
    # 进度条凹槽
    inset(c, t, BAR[0], BAR[1], BAR[2], BAR[3], t["deep"])
    rule(c, t, RULE2_Y)
    return c.img


def save(img, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    print(f"  {path.name:26s} {img.width}x{img.height}  alpha={img.getchannel('A').getextrema()}")


def build_preview(ref_path, mine, scale=3):
    """把属性面板贴到擦除版背包上，3 倍放大展示实际镶嵌效果（左：擦除前 / 右：嵌入后）。"""
    crop = (0, 0, 200, 110)
    base = Image.open(ref_path).convert("RGBA").crop(crop)
    filled = base.copy()
    filled.alpha_composite(mine, ANCHOR)
    w, h = base.size
    gap = 10
    out = Image.new("RGBA", (w * scale * 2 + gap * 3, h * scale + gap * 2), (24, 24, 28, 255))
    out.alpha_composite(base.resize((w * scale, h * scale), Image.NEAREST), (gap, gap))
    out.alpha_composite(filled.resize((w * scale, h * scale), Image.NEAREST), (gap * 2 + w * scale, gap))
    return out


def main():
    print("生成位阶·属性面板（嵌入背包右上角 97x72）->", OUT_DIR)
    imgs = {}
    for name in ("mortal", "legend", "mythic"):
        imgs[name] = make_stats(name)
        save(imgs[name], OUT_DIR / f"rank_stats_{name}.png")

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    solo = imgs["mortal"]
    p1 = PREVIEW_DIR / "rank_stats_mortal_4x.png"
    solo.resize((SW * 4, SH * 4), Image.NEAREST).save(p1)
    print("  单图放大 ->", p1)

    ref = Path(r"C:\Users\Alice\AppData\Roaming\dsh-desktop\harness\attachments\v1\objects\82"
               r"\8233a83176959898f1559a3c7b2e050383cb2a2c6a91dcc91274f3a1ab0d3acc")
    if ref.exists():
        p2 = PREVIEW_DIR / "stats_in_inventory_3x.png"
        build_preview(ref, imgs["mortal"]).save(p2)
        print("  镶嵌预览（左=擦除版 右=嵌入后）->", p2)


if __name__ == "__main__":
    main()
