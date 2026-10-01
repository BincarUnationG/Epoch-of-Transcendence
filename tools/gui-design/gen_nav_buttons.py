#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""右上角导航标签按钮 + 晋升进度条。

布局依据 inventory3.png 实测（区域 x=76..172, y=7..78 → 97 x 72）：
    「位阶」独占一行（全宽）  「境界」+「职业」一行  「加成面板」+「已学法术」一行
    「知识原理」独占一行（全宽） 最下方一条晋升进度条（同宽）

为容纳进度条，按钮压到 12px 高、行距 3px，底部让出 6px。
坐标已规范化对齐（原图手工绘制有 1~3px 抖动）。

产物：
    rank_nav_buttons.png    252 x 30   图集
        y=0..11   宽按钮 84x12   x = 0(常态) / 84(悬停) / 168(激活)
        y=12..23  窄按钮 40x12   x = 0(常态) / 40(悬停) / 80(激活)
        y=24..29  进度条 84x6    x = 0

用法：
    g.blit(TEX, x, y, state * 84,  0,  84, 12);   // 宽按钮
    g.blit(TEX, x, y, state * 40,  12, 40, 12);   // 窄按钮
    g.blit(TEX, x, y, 0,           24, 84, 6);    // 进度条凹槽
"""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_rank_gui import Canvas  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "common" / "src" / "main" / "resources" / "assets" / "epoch_of_transcendence" / "textures" / "gui"
PREVIEW_DIR = Path(__file__).resolve().parent / "preview"

# ---------------------------------------------------------------- 布局
REGION = (76, 7, 97, 72)          # 在 176x166 背包面板中的位置与尺寸
ROW_Y = (2, 17, 32, 47)           # 四行的 y（行高 12，行距 3）
WIDE_W, NARROW_W, BTN_H = 84, 40, 12
COL_X = (7, 51)
BOX_X = 7
BAR = (7, 62, 84, 6)              # 进度条 x, y, w, h

LABELS = [
    (0, 0, "位阶", True),
    (1, 0, "境界", False),
    (1, 1, "职业", False),
    (2, 0, "加成面板", False),
    (2, 1, "已学法术", False),
    (3, 0, "知识原理", True),
]

# 扁平标签：不用斜面，仅靠「平面底色 + 1px 边框」区分状态
STATES = {
    "idle":   {"face": (198, 198, 198, 255), "border": (255, 255, 255, 255)},
    "hover":  {"face": (214, 214, 214, 255), "border": (255, 255, 255, 255)},
    "active": {"face": (255, 255, 255, 255), "border": (255, 255, 255, 255)},
}
TEXT_COLOR = {"idle": 0x3C3C3C, "hover": 0x1A1A1A, "active": 0x000000}

ATLAS_W = 252
ATLAS_H = 30
STATE_ORDER = ("idle", "hover", "active")

# 进度条配色（凹槽 + 建议填充色）
BAR_BG = (33, 33, 33, 255)
BAR_DARK = (55, 55, 55, 255)
BAR_FILL_SUGGEST = (74, 162, 74, 255)     # 原版经验条的绿


def draw_button(c, x, y, w, state):
    """扁平标签：平面底色 + 1px 全边框（无斜面、无投影）。"""
    s = STATES[state]
    c.rect(x, y, x + w - 1, y + BTN_H - 1, s["face"])
    c.hline(x, x + w - 1, y, s["border"])
    c.hline(x, x + w - 1, y + BTN_H - 1, s["border"])
    c.vline(x, y + 1, y + BTN_H - 2, s["border"])
    c.vline(x + w - 1, y + 1, y + BTN_H - 2, s["border"])


def draw_bar(c, x, y, w, h):
    """晋升进度条凹槽：内部深色，左上暗边、右下亮边。填充由代码绘制。"""
    c.rect(x, y, x + w - 1, y + h - 1, BAR_BG)
    c.hline(x, x + w - 1, y, BAR_DARK)
    c.vline(x, y + 1, y + h - 2, BAR_DARK)
    c.hline(x, x + w - 1, y + h - 1, (255, 255, 255, 255))
    c.vline(x + w - 1, y + 1, y + h - 1, (255, 255, 255, 255))


def build_atlas():
    c = Canvas(ATLAS_W, ATLAS_H)
    for i, st in enumerate(STATE_ORDER):
        draw_button(c, i * WIDE_W, 0, WIDE_W, st)
        draw_button(c, i * NARROW_W, BTN_H, NARROW_W, st)
    draw_bar(c, 0, BTN_H * 2, WIDE_W, BAR[3])
    return c.img


def button_rect(row, col, wide):
    y = ROW_Y[row]
    if wide:
        return BOX_X, y, WIDE_W, BTN_H
    return COL_X[col], y, NARROW_W, BTN_H


def build_preview(atlas, ref_path, scale=3, bar_fill=0.35):
    """把按钮与进度条贴到擦除后的背包上，模拟实际效果。"""
    base = Image.open(ref_path).convert("RGBA").crop((0, 0, 200, 120))
    rx, ry, rw, rh = REGION
    base.paste((198, 198, 198, 255), (rx, ry, rx + rw, ry + rh))

    for row, col, label, wide in LABELS:
        bx, by, bw, bh = button_rect(row, col, wide)
        src_y = 0 if wide else BTN_H
        tile = atlas.crop((0, src_y, bw, src_y + bh))
        base.alpha_composite(tile, (rx + bx, ry + by))

    # 进度条：凹槽 + 填充
    bx, by, bw, bh = BAR
    tile = atlas.crop((0, BTN_H * 2, bw, BTN_H * 2 + bh))
    base.alpha_composite(tile, (rx + bx, ry + by))
    filled = int((bw - 2) * bar_fill)
    if filled > 0:
        base.paste(BAR_FILL_SUGGEST, (rx + bx + 1, ry + by + 1, rx + bx + 1 + filled, ry + by + bh - 1))

    draw_labels(base, rx, ry)
    w, h = base.size
    return base.resize((w * scale, h * scale), Image.NEAREST)


def _load_font():
    from PIL import ImageFont
    for name in ("msyh.ttc", "simsun.ttc", "simhei.ttf"):
        p = Path(r"C:\Windows\Fonts") / name
        if p.exists():
            try:
                return ImageFont.truetype(str(p), 8)
            except OSError:
                continue
    return None


def draw_labels(img, rx, ry, rank_level=3):
    """预览文字。「位阶」栏特殊：左边栏名、右边直接显示 Rank level。"""
    from PIL import ImageDraw
    d = ImageDraw.Draw(img)
    font = _load_font()
    if font is None:
        return
    for row, col, label, wide in LABELS:
        bx, by, bw, bh = button_rect(row, col, wide)
        ty = ry + by + (bh - 8) / 2 - 1
        if label == "位阶":
            # 左：栏名　右：当前 Rank level（直接显示，不必点进去）
            d.text((rx + bx + 5, ty), label, font=font, fill=(33, 33, 33, 255))
            val = f"{rank_level} 阶"
            vw = d.textlength(val, font=font)
            d.text((rx + bx + bw - 5 - vw, ty), val, font=font, fill=(0, 0, 0, 255))
        else:
            tw = d.textlength(label, font=font)
            d.text((rx + bx + (bw - tw) / 2, ty), label, font=font, fill=(33, 33, 33, 255))


def main():
    print("生成导航标签按钮 + 进度条图集 ->", OUT_DIR)
    atlas = build_atlas()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    p = OUT_DIR / "rank_nav_buttons.png"
    atlas.save(p)
    print(f"  {p.name:26s} {atlas.width}x{atlas.height}  alpha={atlas.getchannel('A').getextrema()}")

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    atlas.resize((ATLAS_W * 4, ATLAS_H * 4), Image.NEAREST).save(
        PREVIEW_DIR / "rank_nav_atlas_4x.png")
    print("  图集放大 ->", PREVIEW_DIR / "rank_nav_atlas_4x.png")

    ref = Path(r"C:\Users\Alice\AppData\Roaming\dsh-desktop\harness\attachments\v1\objects\4f"
               r"\4ff5f5892abc3f8187493f3b0aff27678962a0c2522532c60001bebf5877e355")
    if ref.exists():
        build_preview(atlas, ref).save(PREVIEW_DIR / "nav_in_inventory_3x.png")
        print("  镶嵌预览 ->", PREVIEW_DIR / "nav_in_inventory_3x.png")


if __name__ == "__main__":
    main()
