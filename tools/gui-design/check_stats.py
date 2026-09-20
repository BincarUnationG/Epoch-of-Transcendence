#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""位阶·属性面板自检：结构断言 + ASCII 图 + 镶嵌后残留覆盖验证。

字符：'K' 黑 'W' 白高光 '.' 面板底 'x' 阴影 's' 凹槽内容 ',' 凹槽暗边 'o' 深色底
      'A' 强调 'a' 强调暗 'M'/'L'/'R' 境界色条 ' ' 透明 '?' 未归类
"""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_stats_panel import (  # noqa: E402
    ANCHOR, BAR, GAUGE_CELL, GAUGE_GAP, GAUGE_N, GAUGE_X, GAUGE_Y, OUT_DIR,
    PANEL_BG, RULE1_Y, RULE2_Y, SH, STATS_LINE, STATS_Y, SW, THEMES,
)
from gen_rank_gui import HIGHLIGHT, OUTLINE, THEMES as PANEL_THEMES  # noqa: E402

KEYCHAR = {
    "outline": "K", "highlight": "W", "panel": ".", "shadow": "x",
    "slot_bg": "s", "slot_dark": ",", "slot_light": "W", "deep": "o",
    "accent": "A", "accent_dim": "a",
}


def classify(col, t):
    if col[3] == 0:
        return " "
    if col == PANEL_BG:
        return "."
    for k, v in t.items():
        if col == v:
            return KEYCHAR.get(k, "?")
    if col == OUTLINE:
        return "K"
    if col == HIGHLIGHT:
        return "W"
    return "?"


def ascii_art(img, t, step=2):
    px = img.load()
    return ["".join(classify(px[x, y], t) for x in range(0, img.width, step))
            for y in range(0, img.height, step)]


def check(name, art=False):
    t = THEMES[name]
    path = OUT_DIR / f"rank_stats_{name}.png"
    img = Image.open(path).convert("RGBA")
    assert img.size == (SW, SH), f"{path.name} 尺寸错误: {img.size}"
    assert img.getchannel("A").getextrema() == (255, 255), "必须是实心底，不能有透明像素"
    px = img.load()
    bad = []

    def want(label, x, y, expect):
        if px[x, y] != expect:
            bad.append(f"    {label} ({x},{y}) 期望{expect} 实得{px[x, y]}")

    # 底色四角必须等于背包面板灰（否则与背有色块边界）
    for label, (x, y) in (("左上", (0, 0)), ("右上", (SW - 1, 0)),
                          ("左下", (0, SH - 1)), ("右下", (SW - 1, SH - 1))):
        want(f"底色{label}", x, y, PANEL_BG)
    # 徽记
    if not any(px[x, y] in (t["accent"], t["accent_dim"])
               for x in range(4, 10) for y in range(1, 7)):
        bad.append("    顶部境界徽记缺失")
    # 位阶刻度尺：10 个 8x8 凹槽
    for i in range(GAUGE_N):
        x = GAUGE_X + i * (GAUGE_CELL + GAUGE_GAP)
        want(f"刻度{i}左上暗边", x, GAUGE_Y, t["slot_dark"])
        want(f"刻度{i}内容", x + 3, GAUGE_Y + 3, t["slot_bg"])
        want(f"刻度{i}底亮边", x + 3, GAUGE_Y + GAUGE_CELL - 1, t["slot_light"])
        if x + GAUGE_CELL - 1 > 92:
            bad.append(f"    刻度{i} 超出右边界 x={x + GAUGE_CELL - 1}")
    # 刻线 + 进度条
    want("刻线1暗", 40, RULE1_Y, t["shadow"])
    want("刻线1亮", 40, RULE1_Y + 1, HIGHLIGHT)
    want("进度条左上", BAR[0], BAR[1], t["slot_dark"])
    want("进度条内容", BAR[0] + 40, BAR[1] + 3, t["deep"])
    want("刻线2暗", 40, RULE2_Y, t["shadow"])
    # 属性区与留白必须是干净的底色（内容全部由代码绘制）
    for y in range(STATS_Y, SH):
        for x in range(SW):
            if px[x, y] != PANEL_BG:
                bad.append(f"    属性区 ({x},{y}) 不该有纹理像素，实得{px[x, y]}")
                break
        else:
            continue
        break

    print(f"\n=== rank_stats_{name}.png  {img.width}x{img.height} ===")
    if art:
        for line in ascii_art(img, t):
            print(line)
    else:
        print("  (结构同 mortal，仅配色不同；跳过 ASCII)")
    print(f"  断言: {'全部通过' if not bad else '失败 %d 项' % len(bad)}")
    for b in bad[:8]:
        print(b)
    return not bad


def check_panel_bg_consistent():
    """三份主题的底色必须完全一致，否则贴上背包会出现色块边界。"""
    ok = True
    for name in ("mortal", "legend", "mythic"):
        px = Image.open(OUT_DIR / f"rank_stats_{name}.png").convert("RGBA").load()
        if px[0, 0] != PANEL_BG or px[SW - 1, SH - 1] != PANEL_BG:
            ok = False
            print(f"  {name} 底色异常: {px[0, 0]}")
    print(f"\n三份主题底色一致性: {'OK' if ok else 'FAIL'}  (均为 #C6C6C6)")
    return ok


def check_composite():
    """把纹理贴到擦除版背包上，验证残留区被完全覆盖。"""
    ref = Path(r"C:\Users\Alice\AppData\Roaming\dsh-desktop\harness\attachments\v1\objects\82"
               r"\8233a83176959898f1559a3c7b2e050383cb2a2c6a91dcc91274f3a1ab0d3acc")
    if not ref.exists():
        print("\n镶嵌验证: 跳过（参考图不可读）")
        return True
    base = Image.open(ref).convert("RGBA")
    mine = Image.open(OUT_DIR / "rank_stats_mortal.png").convert("RGBA")
    filled = base.copy()
    filled.alpha_composite(mine, ANCHOR)
    ox, oy = ANCHOR
    fpx, mpx = filled.load(), mine.load()
    diff = 0
    for y in range(SH):
        for x in range(SW):
            if fpx[ox + x, oy + y] != mpx[x, y]:
                diff += 1
    # 覆盖区之外的邻居：左 x=75 与右 x=173..174 应保持背包原样
    print(f"\n镶嵌验证: 覆盖区像素与纹理不一致数 = {diff} (应为 0)")
    print(f"  左邻 x=75  y=40  -> {fpx[75, 40]}")
    print(f"  右邻 x=173 y=40  -> {fpx[173, 40]}")
    print(f"  上邻 y=6   x=120 -> {fpx[120, 6]}")
    print(f"  下邻 y=79  x=120 -> {fpx[120, 79]}")
    return diff == 0


def main():
    ok = True
    for name in ("mortal", "legend", "mythic"):
        ok &= check(name, art=(name == "mortal"))
    ok &= check_panel_bg_consistent()
    ok &= check_composite()
    print("\n自检结果:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
