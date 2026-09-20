#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""采样参考 GUI（原版 inventory.png）的尺寸、调色板与网格结构。"""

from collections import Counter
from pathlib import Path

from PIL import Image

REF = Path(r"C:\Users\Alice\AppData\Roaming\dsh-desktop\harness\attachments\v1\objects\19"
           r"\1952f9978a96e15197ad58d998a40840a86f41b1c8cd4323e04fd8eeff9f7337")

im = Image.open(REF).convert("RGBA")
W, H = im.size
px = im.load()
print(f"尺寸: {W} x {H}")

# 非透明包围盒
bbox = im.getbbox()
print(f"内容包围盒: {bbox}")

cnt = Counter(im.getdata())
print(f"\n独有颜色数: {len(cnt)}")
print("Top 18 颜色:")
for col, n in cnt.most_common(18):
    print(f"  RGBA{col}  #{col[0]:02X}{col[1]:02X}{col[2]:02X}  占比 {n / (W * H) * 100:5.2f}%")

# 水平扫描：找出格子边界（在 y=200 附近扫一行）
for y in (60, 100, 150, 200):
    row = [px[x, y] for x in range(W)]
    runs = []
    prev, start = row[0], 0
    for x in range(1, W):
        if row[x] != prev:
            runs.append((start, x - 1, prev))
            prev, start = row[x], x
    runs.append((start, W - 1, prev))
    long_runs = [r for r in runs if r[1] - r[0] >= 1]
    print(f"\ny={y} 段数={len(runs)} （仅列长度>=2的段）:")
    for s, e, c in long_runs[:24]:
        print(f"  x {s:3d}-{e:3d} ({e - s + 1:2d}px)  #{c[0]:02X}{c[1]:02X}{c[2]:02X}")

# 垂直扫描：定位面板顶/底与格子的 y 边界
x = 20
col = [px[x, y] for y in range(H)]
runs = []
prev, start = col[0], 0
for y in range(1, H):
    if col[y] != prev:
        runs.append((start, y - 1, prev))
        prev, start = col[y], y
runs.append((start, H - 1, prev))
print(f"\nx={x} 垂直扫描:")
for s, e, c in runs[:30]:
    print(f"  y {s:3d}-{e:3d} ({e - s + 1:2d}px)  #{c[0]:02X}{c[1]:02X}{c[2]:02X}")
