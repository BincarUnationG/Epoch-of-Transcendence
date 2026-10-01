#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""点击导航标签后替换整个背包面板的「子面板」框架。

尺寸与原版玩家背包完全一致：176 x 166。
右上角 x=76..172 / y=7..78 留给导航标签（由 rank_nav_buttons.png 贴出），
其余区域留出两个内容凹槽，内容全部由代码绘制：

    A 标题区   (7, 7)   69 x 72    深色底 —— 当前标签名 + 大号数值
    B 主内容区 (7, 83)  162 x 76   凹槽底 —— 具体内容列表

产物：rank_tab_panel.png   176 x 166

用法：
    g.blit(PANEL, guiLeft, guiTop, 0, 0, 176, 166);   // 替换整块背包面板
    // 再贴导航按钮与进度条，最后在 A / B 区里画内容
"""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_rank_gui import Canvas, HIGHLIGHT, inset  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "common" / "src" / "main" / "resources" / "assets" / "epoch_of_transcendence" / "textures" / "gui"
PREVIEW_DIR = Path(__file__).resolve().parent / "preview"

W, H = 176, 166
BLACK = (0, 0, 0, 255)
SHADOW = (85, 85, 85, 255)
PANEL_BG = (198, 198, 198, 255)
SLOT_DARK = (55, 55, 55, 255)
DEEP = (33, 33, 33, 255)

# 内容凹槽
AREA_A = (7, 7, 69, 72)          # x, y, w, h  标题区（深色底）
AREA_B = (7, 83, 162, 76)        # x, y, w, h  主内容区（凹槽底）

# 与 gen_nav_buttons 保持一致的导航区（代码贴按钮用）
NAV_REGION = (76, 7, 97, 72)

T = {"slot_dark": SLOT_DARK, "slot_light": HIGHLIGHT}


def make_panel():
    c = Canvas(W, H)
    # 原版面板边框：1px 黑描边 + 2px 白高光(顶/左) + 2px 深灰阴影(底/右) + 4px 边距
    c.rect(0, 0, W - 1, H - 1, BLACK)
    c.rect(1, 1, W - 2, H - 2, HIGHLIGHT)
    c.rect(3, 3, W - 4, H - 4, PANEL_BG)
    c.rect(W - 3, 1, W - 2, H - 2, SHADOW)
    c.rect(1, H - 3, W - 2, H - 2, SHADOW)

    # 内容凹槽 A（深色底，放标题与数值）
    x, y, w, h = AREA_A
    inset(c, T, x, y, w, h, DEEP)
    # 内容凹槽 B（凹槽底，放内容）
    x, y, w, h = AREA_B
    inset(c, T, x, y, w, h, (139, 139, 139, 255))
    return c.img


def build_preview(panel, nav_atlas, scale=3, level=3):
    """合成「点击位阶后」的界面：面板 + 导航标签 + 内容示意。"""
    from PIL import ImageDraw
    from gen_nav_buttons import LABELS, button_rect, draw_labels

    shot = panel.copy()
    # 贴导航按钮（常态）与进度条
    for row, col, label, wide in LABELS:
        bx, by, bw, bh = button_rect(row, col, wide)
        src_y = 0 if wide else 12
        tile = nav_atlas.crop((0, src_y, bw, src_y + bh))
        shot.alpha_composite(tile, (NAV_REGION[0] + bx, NAV_REGION[1] + by))
    bar_tile = nav_atlas.crop((0, 24, 84, 30))
    shot.alpha_composite(bar_tile, (NAV_REGION[0] + 7, NAV_REGION[1] + 62))
    shot.paste((74, 162, 74, 255), (NAV_REGION[0] + 8, NAV_REGION[1] + 63,
                                    NAV_REGION[0] + 8 + 29, NAV_REGION[1] + 67))
    draw_labels(shot, NAV_REGION[0], NAV_REGION[1], rank_level=level)

    d = ImageDraw.Draw(shot)
    font = _font(8)
    big = _font(24)
    if font and big:
        # A 区：标签名 + 大号等级
        ax, ay, aw, ah = AREA_A
        d.text((ax + 8, ay + 10), "位阶", font=font, fill=(160, 160, 160, 255))
        num = str(level)
        nw = d.textlength(num, font=big)
        d.text((ax + (aw - nw) / 2 - 2, ay + 22), num, font=big, fill=(255, 255, 255, 255))
        d.text((ax + (aw - nw) / 2, ay + 48), "阶", font=font, fill=(180, 180, 180, 255))
        # B 区：内容示意
        bx, by, bw, bh = AREA_B
        rows = [("境界", "传说 · 3 阶"), ("修为", "1234 / 2000"),
                ("攻击", "+12"), ("防御", "+8"), ("生命", "+20"), ("灵力", "+15")]
        for i, (k, v) in enumerate(rows):
            ry = by + 6 + i * 11
            d.text((bx + 8, ry), k, font=font, fill=(60, 60, 60, 255))
            d.text((bx + 40, ry), v, font=font, fill=(255, 255, 255, 255))
    return shot.resize((W * scale, H * scale), Image.NEAREST)


def _font(size):
    from PIL import ImageFont
    for name in ("msyh.ttc", "simsun.ttc", "simhei.ttf"):
        p = Path(r"C:\Windows\Fonts") / name
        if p.exists():
            try:
                return ImageFont.truetype(str(p), size)
            except OSError:
                continue
    return None


def main():
    print("生成子面板框架 ->", OUT_DIR)
    panel = make_panel()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    p = OUT_DIR / "rank_tab_panel.png"
    panel.save(p)
    print(f"  {p.name:26s} {panel.width}x{panel.height}  alpha={panel.getchannel('A').getextrema()}")

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    panel.resize((W * 3, H * 3), Image.NEAREST).save(PREVIEW_DIR / "rank_tab_panel_3x.png")

    nav = OUT_DIR / "rank_nav_buttons.png"
    if nav.exists():
        atlas = Image.open(nav).convert("RGBA")
        shot = build_preview(panel, atlas)
        shot.save(PREVIEW_DIR / "tab_panel_rank_3x.png")
        print("  子面板预览 ->", PREVIEW_DIR / "tab_panel_rank_3x.png")


if __name__ == "__main__":
    main()
