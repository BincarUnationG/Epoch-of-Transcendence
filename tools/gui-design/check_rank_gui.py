#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""位阶 GUI 纹理自检（原版背包像素语言）：逐像素分类 -> ASCII 结构图 + 坐标断言。

字符含义：
    'K' 黑描边   'W' 白高光/凹槽亮边   '.' 面板底   'x' 面板阴影
    's' 凹槽内容 ',' 凹槽暗边          'o' 深色底(节点/标题/进度槽)
    'A' 境界强调 'a' 强调暗色          'M'/'L'/'R' 神话/传说/凡尘 色条
    ' ' 透明     '?' 未归类
"""

import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_rank_gui import (  # noqa: E402
    H, HIGHLIGHT, OUTLINE, OUT_DIR, REALM_COLOR, SLOT_COL_X, SLOT_H, SLOT_LEVELS,
    SLOT_ROW_Y, SLOT_STEP, SLOT_W, TAB_OFF, THEMES, W, realm_of,
)

KEYCHAR = {
    "outline": "K", "highlight": "W", "panel": ".", "shadow": "x",
    "slot_bg": "s", "slot_dark": ",", "slot_light": "W", "deep": "o",
    "accent": "A", "accent_dim": "a",
}
REALMCHAR = {REALM_COLOR["mythic"]: "M", REALM_COLOR["legend"]: "L", REALM_COLOR["mortal"]: "R"}


def classify(col, t):
    if col[3] == 0:
        return " "
    for k, v in t.items():
        if col == v:
            return KEYCHAR.get(k, "?")
    if col == OUTLINE:
        return "K"
    if col == HIGHLIGHT:
        return "W"
    if col in REALMCHAR:
        return REALMCHAR[col]
    return "?"


def ascii_art(img, t, step=2):
    px = img.load()
    return ["".join(classify(px[x, y], t) for x in range(0, img.width, step))
            for y in range(0, img.height, step)]


def check(name, art=True):
    t = THEMES[name]
    path = OUT_DIR / f"rank_panel_{name}.png"
    img = Image.open(path).convert("RGBA")
    assert img.size == (W, H), f"{path.name} 尺寸错误: {img.size}"
    assert img.getchannel("A").getextrema() == (255, 255), "面板存在透明像素"
    px = img.load()
    bad = []

    def want(label, x, y, expect):
        if px[x, y] != expect:
            bad.append(f"    {label} ({x},{y}) 期望{expect} 实得{px[x, y]}")

    # 边框（对照原版 inventory.png 实测）
    want("外描边", 0, 0, (0, 0, 0, 255))
    want("顶高光1", 40, 1, (255, 255, 255, 255))
    want("顶高光2", 40, 2, (255, 255, 255, 255))
    want("面板底", 40, 3, t["panel"])
    want("左边距", 5, 5, t["panel"])
    want("底阴影", 40, H - 2, t["shadow"])
    want("右阴影", W - 2, 40, t["shadow"])
    want("右下描边", W - 1, H - 1, (0, 0, 0, 255))
    # 标题带
    want("标题槽底", 87, 15, t["deep"])
    want("标题槽暗边", 87, 7, t["slot_dark"])
    want("标题槽亮边", 87, 24, t["slot_light"])
    # 进度条
    want("进度槽底", 87, 145, t["deep"])
    want("底部刻线", 87, 153, t["shadow"])
    want("刻线高光", 87, 154, (255, 255, 255, 255))

    # 逐槽校验：10 个槽都在正确坐标，且凹槽四边成立
    for row, levels in enumerate(SLOT_LEVELS):
        y = SLOT_ROW_Y + row * SLOT_STEP
        for col, lv in enumerate(levels):
            x = SLOT_COL_X[col]
            want(f"槽lv{lv}左上暗边", x, y, t["slot_dark"])
            want(f"槽lv{lv}底亮边", x + 30, y + SLOT_H - 1, t["slot_light"])
            want(f"槽lv{lv}内容", x + 30, y + SLOT_H // 2, t["slot_bg"])
            want(f"槽lv{lv}节点", x + 11, y + 9, t["deep"])
            # 境界色条（x+1..x+2）
            rc = REALM_COLOR[realm_of(lv)]
            if px[x + 1, y + 8] != rc:
                bad.append(f"    槽lv{lv}境界色条 ({x + 1},{y + 8}) 期望{rc} 实得{px[x + 1, y + 8]}")

    print(f"\n=== rank_panel_{name}.png  {img.width}x{img.height} ===")
    if art:
        for line in ascii_art(img, t):
            print(line)
    else:
        print("  (结构同 mortal，仅配色不同；跳过 ASCII)")
    print(f"  断言: {'全部通过' if not bad else '失败 %d 项' % len(bad)}")
    for b in bad:
        print(b)
    return not bad


def check_tabs():
    ok = True
    for fname, sel in (("rank_tab.png", False), ("rank_tab_selected.png", True)):
        t = THEMES["mortal"] if sel else TAB_OFF
        img = Image.open(OUT_DIR / fname).convert("RGBA")
        px = img.load()
        assert img.size == (28, 32), f"{fname} 尺寸错误: {img.size}"
        bad = []
        if px[0, 0] != (0, 0, 0, 255):
            bad.append("    缺黑描边")
        if px[14, 5] != t["panel"]:
            bad.append(f"    面板底 期望{t['panel']} 实得{px[14, 5]}")
        print(f"\n=== {fname}  28x32  corner_alpha={img.getchannel('A').getextrema()} ===")
        for line in ascii_art(img, t, step=1):
            print(line)
        if bad:
            ok = False
            print("  断言失败:")
            for b in bad:
                print(b)
        else:
            print("  断言通过")
    return ok


def main():
    ok = True
    for name in ("mortal", "legend", "mythic"):
        ok &= check(name, art=(name == "mortal"))
    ok &= check_tabs()
    print("\n自检结果:", "PASS" if ok else "FAIL")


if __name__ == "__main__":
    main()
