#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""分析 inventory3.png 右上角导航标签的布局（区域 x=76..172, y=7..78）。"""

from collections import Counter
from pathlib import Path

from PIL import Image

REF = Path(r"C:\Users\Alice\AppData\Roaming\dsh-desktop\harness\attachments\v1\objects\4f"
           r"\4ff5f5892abc3f8187493f3b0aff27678962a0c2522532c60001bebf5877e355")

X0, Y0, X1, Y1 = 76, 7, 173, 79          # 可用区域
im = Image.open(REF).convert("RGB")
print(f"图片尺寸: {im.size}  模式: {im.mode}")

crop = im.crop((X0, Y0, X1, Y1))
W, H = crop.size
print(f"截取区域: {W} x {H}")


def lum(p):
    return 0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2]


def ch(p):
    l = lum(p)
    if l > 185:
        return " "
    if l > 150:
        return "."
    if l > 115:
        return ":"
    if l > 80:
        return "-"
    if l > 50:
        return "="
    if l > 28:
        return "+"
    return "#"


px = crop.load()
print("\n--- ASCII 结构图（每字符 1 像素，越暗字符越重）---")
print("    " + "".join(str(x % 10) for x in range(W)))
for y in range(H):
    print(f"{y:3d} " + "".join(ch(px[x, y]) for x in range(W)))

print("\n--- 颜色直方图（量化到 8 级）---")
q = Counter()
for y in range(H):
    for x in range(W):
        p = px[x, y]
        q[(p[0] // 16 * 16, p[1] // 16 * 16, p[2] // 16 * 16)] += 1
for col, n in q.most_common(14):
    print(f"  #{col[0]:02X}{col[1]:02X}{col[2]:02X}  {n:5d}  ({n / (W * H) * 100:5.2f}%)")
