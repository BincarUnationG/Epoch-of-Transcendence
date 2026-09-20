#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《超验纪元》位阶(Rank)标签页 GUI 纹理生成器 —— 原版背包像素语言。

像素结构严格对齐原版 textures/gui/container/inventory.png（实测采样）：
    1px 黑描边  →  2px 白高光(顶/左)  |  2px 深灰阴影(底/右)
    4px 面板边距  →  内容区 x = 7..168, y = 7..162
    凹槽 18x18  = 1px 暗边(左上) + 16x16 内容(#8B8B8B) + 1px 亮边(右下)
基准调色板（原版实测）：panel #C6C6C6 · shadow #555555 · slot #8B8B8B
                        slot dark #373737 · deep #212121 · highlight #FFFFFF

尺寸与原版玩家背包 GUI 完全一致：176 x 166。

生成物（common/src/main/resources/assets/epoch_of_transcendence/textures/gui/）：
    rank_panel_mortal.png    176x166   凡尘（标准原版灰，与背包零色差）
    rank_panel_legend.png    176x166   传说（淡紫灰）
    rank_panel_mythic.png    176x166   神话（淡金灰）
    rank_tab.png              28x32    位阶标签页按钮（未选中）
    rank_tab_selected.png     28x32    位阶标签页按钮（选中）

用法：python tools/gui-design/gen_rank_gui.py
"""

from pathlib import Path

from PIL import Image

W, H = 176, 166

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "common" / "src" / "main" / "resources" / "assets" / "epoch_of_transcendence" / "textures" / "gui"
PREVIEW_DIR = Path(__file__).resolve().parent / "preview"

# ---------------------------------------------------------------- 布局常量
TITLE = (7, 7, 168, 24)          # 标题凹槽 x0,y0,x1,y1（18px 高，与一个格子等高）
SLOT_COL_X = (7, 93)             # 两列等级槽的 x0（列宽 76，列间距 10）
SLOT_W, SLOT_H = 76, 18
SLOT_ROW_Y = 29                  # 首行 y0
SLOT_STEP = 22                   # 18 高 + 4 间隔
BAR = (7, 141, 168, 150)         # 进度条凹槽
RULE_Y = 153                     # 底部刻线

SLOT_LEVELS = [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]

REALM_COLOR = {                  # 槽左缘境界色条（三份主题统一，保证语义一致）
    "mythic": (184, 134, 11, 255),    # 暗金
    "legend": (123, 94, 167, 255),    # 紫
    "mortal": (138, 110, 75, 255),    # 铜
}


def realm_of(level: int) -> str:
    if level >= 5:
        return "mortal"
    if level >= 3:
        return "legend"
    return "mythic"


# ---------------------------------------------------------------- 色板
OUTLINE = (0, 0, 0, 255)
HIGHLIGHT = (255, 255, 255, 255)

THEMES = {
    "mortal": {                       # 凡尘 · 标准原版灰（与背包零色差）
        "panel": (198, 198, 198, 255),
        "shadow": (85, 85, 85, 255),
        "slot_bg": (139, 139, 139, 255),
        "slot_dark": (55, 55, 55, 255),
        "slot_light": (255, 255, 255, 255),
        "deep": (33, 33, 33, 255),
        "accent": (138, 110, 75, 255),
        "accent_dim": (94, 75, 51, 255),
    },
    "legend": {                       # 传说 · 淡紫灰
        "panel": (194, 186, 218, 255),
        "shadow": (78, 70, 104, 255),
        "slot_bg": (138, 131, 160, 255),
        "slot_dark": (56, 50, 74, 255),
        "slot_light": (255, 255, 255, 255),
        "deep": (33, 30, 48, 255),
        "accent": (123, 94, 167, 255),
        "accent_dim": (84, 64, 114, 255),
    },
    "mythic": {                       # 神话 · 淡金灰
        "panel": (210, 198, 168, 255),
        "shadow": (94, 82, 64, 255),
        "slot_bg": (152, 140, 114, 255),
        "slot_dark": (60, 53, 40, 255),
        "slot_light": (255, 255, 255, 255),
        "deep": (36, 32, 26, 255),
        "accent": (168, 133, 58, 255),
        "accent_dim": (112, 88, 38, 255),
    },
}

TAB_OFF = {                           # 标签页未选中态（整体压暗一档）
    "panel": (160, 160, 160, 255),
    "shadow": (74, 74, 74, 255),
    "slot_dark": (48, 48, 48, 255),
    "slot_light": (216, 216, 216, 255),
    "deep": (44, 44, 44, 255),
    "accent": (146, 122, 88, 255),
    "accent_dim": (104, 88, 64, 255),
}


def dim(col, k):
    return (int(col[0] * k), int(col[1] * k), int(col[2] * k), col[3])


# ---------------------------------------------------------------- 画布原语
class Canvas:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        self.p = self.img.load()

    def set(self, x, y, col):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.p[x, y] = col

    def rect(self, x0, y0, x1, y1, col):
        if x0 > x1:
            x0, x1 = x1, x0
        if y0 > y1:
            y0, y1 = y1, y0
        for y in range(max(0, y0), min(self.h - 1, y1) + 1):
            for x in range(max(0, x0), min(self.w - 1, x1) + 1):
                self.p[x, y] = col

    def hline(self, x0, x1, y, col):
        self.rect(x0, y, x1, y, col)

    def vline(self, x, y0, y1, col):
        self.rect(x, y0, x, y1, col)


def panel_frame(c, t, w, h):
    """原版面板边框：黑描边 + 2px 白高光(顶/左) + 2px 深灰阴影(底/右) + 4px 边距。"""
    c.rect(0, 0, w - 1, h - 1, OUTLINE)
    c.rect(1, 1, w - 2, h - 2, HIGHLIGHT)
    c.rect(3, 3, w - 4, h - 4, t["panel"])
    c.rect(w - 3, 1, w - 2, h - 2, t["shadow"])
    c.rect(1, h - 3, w - 2, h - 2, t["shadow"])


def inset(c, t, x, y, w, h, fill):
    """原版凹槽：左上 1px 暗边，右下 1px 亮边。"""
    c.rect(x, y, x + w - 1, y + h - 1, fill)
    c.hline(x, x + w - 1, y, t["slot_dark"])
    c.vline(x, y + 1, y + h - 2, t["slot_dark"])
    c.hline(x, x + w - 1, y + h - 1, t["slot_light"])
    c.vline(x + w - 1, y + 1, y + h - 1, t["slot_light"])


def node(c, t, x, y, size=12):
    """节点凹槽：更深一档，留给代码点亮。"""
    c.rect(x, y, x + size - 1, y + size - 1, t["deep"])
    c.hline(x, x + size - 1, y, OUTLINE)
    c.vline(x, y + 1, y + size - 2, OUTLINE)
    c.hline(x, x + size - 1, y + size - 1, t["shadow"])
    c.vline(x + size - 1, y + 1, y + size - 1, t["shadow"])


def glyph(c, name, ox, oy, main, dim_col):
    """6x6 境界徽记（标题带两端）。"""
    if name == "mortal":              # 山
        rows = ["..X...", ".XXX..", ".XXX..", "XXXXX.", "XXX.X.", "XX...X"]
    elif name == "legend":            # 四芒星
        rows = ["..X...", "..X...", "XXXXX.", "XXXXX.", "..X...", ".X.X.."]
    else:                             # 八芒星
        rows = ["..X...", ".XXX..", "XXXXX.", ".XXX..", "..X...", "X...X."]
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch == "X":
                c.set(ox + x, oy + y, main if (x + y) % 2 == 0 else dim_col)


# ---------------------------------------------------------------- 面板
def draw_slot(c, t, x, y, level):
    inset(c, t, x, y, SLOT_W, SLOT_H, t["slot_bg"])
    # 左缘 2px 境界色条
    rc = REALM_COLOR[realm_of(level)]
    c.rect(x + 1, y + 3, x + 2, y + 14, rc)
    c.hline(x + 1, x + 2, y + 3, dim(rc, 0.6))
    c.hline(x + 1, x + 2, y + 14, dim(rc, 1.35))
    # 节点凹槽（代码点亮）
    node(c, t, x + 5, y + 3, 12)


def make_panel(name):
    t = THEMES[name]
    c = Canvas(W, H)
    panel_frame(c, t, W, H)

    # 标题凹槽：代码在此居中绘制「境界 · 位阶」
    inset(c, t, TITLE[0], TITLE[1], TITLE[2] - TITLE[0] + 1, TITLE[3] - TITLE[1] + 1, t["deep"])
    glyph(c, name, 11, 12, t["accent"], t["accent_dim"])
    glyph(c, name, 159, 12, t["accent"], t["accent_dim"])

    # 10 个等级槽
    for row, levels in enumerate(SLOT_LEVELS):
        y = SLOT_ROW_Y + row * SLOT_STEP
        for col, lv in enumerate(levels):
            draw_slot(c, t, SLOT_COL_X[col], y, lv)

    # 进度条凹槽（代码填进度）
    inset(c, t, BAR[0], BAR[1], BAR[2] - BAR[0] + 1, BAR[3] - BAR[1] + 1, t["deep"])

    # 底部刻线
    c.hline(7, 168, RULE_Y, t["shadow"])
    c.hline(7, 168, RULE_Y + 1, HIGHLIGHT)
    return c.img


# ---------------------------------------------------------------- 标签页
def make_tab(selected):
    """标签页按钮。与面板的「无缝相接」由 Java 侧用面板底色覆盖底边实现。"""
    if selected:
        t = THEMES["mortal"]
    else:
        t = TAB_OFF
    tw, th = 28, 32
    c = Canvas(tw, th)
    c.rect(0, 0, tw - 1, th - 1, OUTLINE)
    c.rect(1, 1, tw - 2, th - 2, t["slot_light"] if selected else t["slot_light"])
    c.rect(3, 3, tw - 4, th - 4, t["panel"])
    c.rect(tw - 3, 1, tw - 2, th - 2, t["shadow"])
    c.rect(1, th - 3, tw - 2, th - 2, t["shadow"])
    if selected:
        # 选中态：底部 2 行不画描边/阴影，交给面板底色衔接
        c.rect(1, th - 2, tw - 2, th - 1, t["panel"])
        c.rect(tw - 3, 1, tw - 2, th - 3, t["shadow"])
    # 阶梯塔图标 16x16，居中
    ox, oy = (tw - 16) // 2, (th - 16) // 2
    dk = t["slot_dark"]
    mid = t["shadow"]
    c.rect(ox + 1, oy + 12, ox + 14, oy + 13, dk)
    c.hline(ox + 1, ox + 14, oy + 14, mid)
    c.rect(ox + 3, oy + 9, ox + 12, oy + 10, dk)
    c.hline(ox + 3, ox + 12, oy + 11, mid)
    c.rect(ox + 5, oy + 6, ox + 10, oy + 7, dk)
    c.hline(ox + 5, ox + 10, oy + 8, mid)
    c.rect(ox + 6, oy + 4, ox + 9, oy + 5, dk)
    # 顶端星（境界金）
    c.set(ox + 7, oy + 1, t["accent"])
    c.hline(ox + 6, ox + 9, oy + 2, t["accent"])
    c.hline(ox + 5, ox + 10, oy + 3, t["accent"])
    c.set(ox + 7, oy + 3, t["accent_dim"])
    return c.img


# ---------------------------------------------------------------- 输出
def save(img, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    print(f"  {path.name:26s} {img.width}x{img.height}  alpha={img.getchannel('A').getextrema()}")


def build_preview(panels, tabs, scale=3):
    gap = 14
    cols = len(panels) * (W * scale + gap) + len(tabs) * (28 * scale + gap) + gap
    rows = H * scale + gap * 2
    out = Image.new("RGBA", (cols, rows), (24, 24, 28, 255))
    x = gap
    for p in panels:
        out.alpha_composite(p.resize((p.width * scale, p.height * scale), Image.NEAREST), (x, gap))
        x += W * scale + gap
    for tb in tabs:
        out.alpha_composite(tb.resize((tb.width * scale, tb.height * scale), Image.NEAREST), (x, gap))
        x += 28 * scale + gap
    return out


def build_compare(ref_path, mine, scale=2):
    """与参考背包并排对比（各取 176x166 逻辑区域）。"""
    ref = Image.open(ref_path).convert("RGBA").crop((0, 0, W, H))
    gap = 16
    cols = W * scale * 2 + gap * 3
    rows = H * scale + gap * 2
    out = Image.new("RGBA", (cols, rows), (24, 24, 28, 255))
    out.alpha_composite(ref.resize((W * scale, H * scale), Image.NEAREST), (gap, gap))
    out.alpha_composite(mine.resize((W * scale, H * scale), Image.NEAREST), (gap * 2 + W * scale, gap))
    return out


def main():
    print("生成位阶 GUI 纹理（原版背包像素语言）->", OUT_DIR)
    panels = {n: make_panel(n) for n in ("mortal", "legend", "mythic")}
    tabs = {"tab": make_tab(False), "tab_selected": make_tab(True)}

    for n, img in panels.items():
        save(img, OUT_DIR / f"rank_panel_{n}.png")
    save(tabs["tab"], OUT_DIR / "rank_tab.png")
    save(tabs["tab_selected"], OUT_DIR / "rank_tab_selected.png")

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    p1 = PREVIEW_DIR / "rank_gui_preview_3x.png"
    build_preview(list(panels.values()), list(tabs.values())).save(p1)
    print("  预览图 ->", p1)

    ref = Path(r"C:\Users\Alice\AppData\Roaming\dsh-desktop\harness\attachments\v1\objects\19"
               r"\1952f9978a96e15197ad58d998a40840a86f41b1c8cd4323e04fd8eeff9f7337")
    if ref.exists():
        p2 = PREVIEW_DIR / "compare_with_inventory_2x.png"
        build_compare(ref, panels["mortal"]).save(p2)
        print("  对比图（左=原版背包 右=位阶面板）->", p2)


if __name__ == "__main__":
    main()
