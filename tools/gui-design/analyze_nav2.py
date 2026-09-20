#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""细化分析：区分「比面板底更亮」的元素（标签边框/底）与文字。"""

from pathlib import Path

from PIL import Image

REF = Path(r"C:\Users\Alice\AppData\Roaming\dsh-desktop\harness\attachments\v1\objects\4f"
           r"\4ff5f5892abc3f8187493f3b0aff27678962a0c2522532c60001bebf5877e355")

X0, Y0, X1, Y1 = 76, 7, 173, 79
crop = Image.open(REF).convert("RGB").crop((X0, Y0, X1, Y1))
W, H = crop.size
px = crop.load()


def lum(p):
    return 0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2]


def ch(p):
    l = lum(p)
    if l > 230:
        return "W"        # 近白：标签底/高光边
    if l > 205:
        return "o"        # 略亮于面板
    if l > 185:
        return " "        # 面板底 #C6C6C6
    if l > 155:
        return "."
    if l > 120:
        return ":"
    if l > 85:
        return "-"
    if l > 50:
        return "="
    if l > 25:
        return "+"
    return "#"


print("--- 细化结构图（W=近白 o=略亮 空=面板底 越往后越暗）---")
print("    " + "".join(str(x % 10) for x in range(W)))
for y in range(H):
    print(f"{y:3d} " + "".join(ch(px[x, y]) for x in range(W)))

print("\n--- 每一行「亮于面板」像素的 x 范围（可能的标签框线）---")
for y in range(H):
    xs = [x for x in range(W) if lum(px[x, y]) > 205]
    if xs:
        # 压缩为连续段
        segs, s = [], xs[0]
        for a, b in zip(xs, xs[1:]):
            if b - a > 1:
                segs.append((s, a))
                s = b
        segs.append((s, xs[-1]))
        print(f"  y={y:2d}  " + "  ".join(f"{a}-{b}" for a, b in segs))

print("\n--- 每一列「亮于面板」像素的 y 范围 ---")
for x in range(W):
    ys = [y for y in range(H) if lum(px[x, y]) > 205]
    if len(ys) >= 3:
        segs, s = [], ys[0]
        for a, b in zip(ys, ys[1:]):
            if b - a > 1:
                segs.append((s, a))
                s = b
        segs.append((s, ys[-1]))
        print(f"  x={x:2d}  " + "  ".join(f"{a}-{b}" for a, b in segs))
