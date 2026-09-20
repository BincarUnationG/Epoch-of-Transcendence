#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""分析 inventory2.png：定位被擦除的右上角合成区，量出可用矩形边界。"""

from pathlib import Path

from PIL import Image

REF = Path(r"C:\Users\Alice\AppData\Roaming\dsh-desktop\harness\attachments\v1\objects\82"
           r"\8233a83176959898f1559a3c7b2e050383cb2a2c6a91dcc91274f3a1ab0d3acc")

GRAY = (198, 198, 198, 255)

im = Image.open(REF).convert("RGBA")
W, H = im.size
px = im.load()
print(f"尺寸: {W} x {H}   内容包围盒: {im.getbbox()}")

# 逐行找最长的连续面板灰段（只看面板内 x<176）
print("\n--- 每行最长 #C6C6C6 连续段（y=0..90, x<176）---")
for y in range(0, 92):
    best = (0, 0, 0)
    s = None
    for x in range(0, 176):
        if px[x, y] == GRAY:
            if s is None:
                s = x
        else:
            if s is not None and x - s > best[0]:
                best = (x - s, s, x - 1)
            s = None
    if s is not None and 176 - s > best[0]:
        best = (176 - s, s, 175)
    if best[0] >= 8:
        print(f"  y={y:3d}  最长灰段 x={best[1]:3d}..{best[2]:3d}  ({best[0]}px)")

# 逐列找最长连续面板灰段（x=70..175）
print("\n--- 每列最长 #C6C6C6 连续段（x=70..175, y<100）---")
for x in range(70, 176, 2):
    best = (0, 0, 0)
    s = None
    for y in range(0, 100):
        if px[x, y] == GRAY:
            if s is None:
                s = y
        else:
            if s is not None and y - s > best[0]:
                best = (y - s, s, y - 1)
            s = None
    if s is not None and 100 - s > best[0]:
        best = (100 - s, s, 99)
    print(f"  x={x:3d}  最长灰段 y={best[1]:3d}..{best[2]:3d}  ({best[0]}px)")

# 关键行/列的全量扫描，确认左右与上下的精确边界
print("\n--- 关键扫描 ---")
for y in (8, 9, 10, 40, 70, 76, 77, 78, 79, 80, 82):
    row = []
    prev, start = px[0, y], 0
    for x in range(1, 176):
        if px[x, y] != prev:
            row.append((start, x - 1, prev))
            prev, start = px[x, y], x
    row.append((start, 175, prev))
    print(f"  y={y:3d}: " + "  ".join(f"{s}-{e}#{c[0]:02X}{c[1]:02X}{c[2]:02X}" for s, e, c in row if e - s >= 1))
