#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成可直接打开的设计稿 HTML（单文件自包含，图片以 base64 内嵌）。

输出：tools/gui-design/preview/rank-gui-design.html
"""

import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREVIEW = HERE / "preview"
OUT = PREVIEW / "rank-gui-design.html"


def uri(name: str) -> str:
    p = PREVIEW / name
    if not p.exists():
        return ""
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode("ascii")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>位阶 GUI 设计稿 · Epoch of Transcendence</title>
<style>
:root{color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:#141118;color:#E8DCC8;font-family:'Microsoft YaHei','Noto Sans SC',system-ui,sans-serif;font-size:14px;line-height:1.75}
.wrap{max-width:1200px;margin:0 auto;padding:30px 22px 70px}
h1{font-size:22px;margin:0 0 4px;color:#E8B254;letter-spacing:1px}
.sub{color:#9A8A72;font-size:13px;margin:0 0 28px}
h2{font-size:15px;margin:36px 0 12px;color:#C49054;border-left:3px solid #5C4127;padding-left:10px;letter-spacing:.5px}
p{margin:0 0 10px;color:#C9BCA6}
.card{background:#1C140C;border:1px solid #3E2A18;border-radius:6px;padding:14px;margin-bottom:12px}
.card.pad0{padding:8px;text-align:center;background:#0E0C12}
img{max-width:100%;display:block;margin:0 auto;border-radius:4px;image-rendering:pixelated}
table{width:100%;border-collapse:collapse;font-size:13px;margin-bottom:14px}
th{background:#241A10;color:#C49054;text-align:left;padding:7px 10px;border:1px solid #3E2A18;font-weight:600}
td{padding:6px 10px;border:1px solid #2A1E14;color:#C9BCA6}
code{font-family:Consolas,'Courier New',monospace;color:#D8B98A;background:#241A10;padding:1px 5px;border-radius:3px;font-size:12.5px}
pre{background:#0B0806;border:1px solid #3E2A18;border-radius:6px;padding:14px 16px;overflow-x:auto;margin:0 0 14px}
pre code{background:none;padding:0;color:#C9B896;font-size:12.5px;line-height:1.65}
.warn{border-left:3px solid #B8860B;background:#241A10;padding:11px 14px;border-radius:0 5px 5px 0;color:#D8C9A8;font-size:13px;margin-bottom:16px}
ul{padding-left:20px;color:#C9BCA6;margin:0}
li{margin:4px 0}
.cap{font-size:12px;color:#8A7A62;margin:8px 0 18px;text-align:center}
.cm{color:#7A6A52}
.kw{color:#B8860B}
</style>
</head>
<body>
<div class="wrap">
<h1>位阶 · 属性面板 — 设计稿</h1>
<div class="sub">Epoch of Transcendence · 原版背包像素语言 · 嵌入被擦除的合成区（97 × 72）</div>

<h2>一 · 镶嵌预览</h2>
<div class="card pad0"><img src="{{IMG_COMPOSITE}}" alt="镶嵌预览"></div>
<div class="cap">左：擦除合成区后的背包　·　右：嵌入位阶属性面板后（3 倍放大，金色虚线为新面板范围）</div>

<h2>二 · 可用区域实测</h2>
<table>
<tr><th>边界</th><th>位置</th><th>说明</th></tr>
<tr><td>左</td><td>x = 76</td><td>x=75 是玩家预览区边框，不能再左</td></tr>
<tr><td>右</td><td>x = 172</td><td>x=173..174 是面板阴影 <code>#555555</code>，不能再右</td></tr>
<tr><td>上</td><td>y = 7</td><td>y=3..6 是面板 4px 内边距</td></tr>
<tr><td>下</td><td>y = 78</td><td>y=79..82 是 4px 灰带，y=83 起是主背包</td></tr>
<tr><td><strong>结论</strong></td><td colspan="2"><strong>97 × 72</strong> — 正好与原版合成区同尺寸</td></tr>
</table>
<div class="warn"><strong>擦除残留：</strong>逐像素扫描发现 y=17..78 之间散落着 <code>#C5C5C5</code>（比面板灰暗 1 阶）与单像素杂点，集中在 x = 82 / 90 / 93 / 125 / 144 / 153 / 170 一带，应是原合成格边框的抗锯齿痕迹。本面板为<strong>实心底</strong>，贴上去可将其一并覆盖。</div>

<h2>三 · 面板内部设计稿（97 × 72）</h2>
<div class="card pad0"><img src="{{IMG_SOLO}}" alt="面板 4x 放大"></div>
<div class="cap">rank_stats_mortal.png · 4 倍放大（最近邻）</div>
<div class="card pad0">
<svg width="462" height="296" viewBox="0 0 462 296" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
<defs><g id="c8b">
<rect width="8" height="8" fill="#8B8B8B"/><rect width="8" height="1" fill="#373737"/><rect y="1" width="1" height="6" fill="#373737"/><rect y="7" width="8" height="1" fill="#FFFFFF"/><rect x="7" y="1" width="1" height="7" fill="#FFFFFF"/>
</g></defs>
<g transform="translate(14,26) scale(3)">
<rect width="97" height="72" fill="#C6C6C6"/>
<rect x="4" y="1" width="6" height="1" fill="#8A6E4B"/><rect x="5" y="2" width="4" height="1" fill="#8A6E4B"/><rect x="6" y="3" width="2" height="1" fill="#8A6E4B"/>
<text x="12" y="7" font-size="6" fill="#212121" font-family="Consolas,monospace" font-weight="bold">位阶 · 传说</text>
<text x="93" y="7" font-size="6" fill="#555555" font-family="Consolas,monospace" text-anchor="end">3 / 9</text>
<use href="#c8b" x="4" y="10"/><use href="#c8b" x="13" y="10"/><use href="#c8b" x="22" y="10"/><use href="#c8b" x="31" y="10"/><use href="#c8b" x="40" y="10"/><use href="#c8b" x="49" y="10"/><use href="#c8b" x="58" y="10"/><use href="#c8b" x="67" y="10"/><use href="#c8b" x="76" y="10"/><use href="#c8b" x="85" y="10"/>
<rect x="4" y="19" width="89" height="1" fill="#555555"/><rect x="4" y="20" width="89" height="1" fill="#FFFFFF"/>
<rect x="4" y="22" width="89" height="7" fill="#212121"/><rect x="4" y="22" width="89" height="1" fill="#373737"/><rect x="4" y="23" width="1" height="5" fill="#373737"/><rect x="4" y="28" width="89" height="1" fill="#FFFFFF"/><rect x="92" y="23" width="1" height="6" fill="#FFFFFF"/>
<rect x="4" y="30" width="89" height="1" fill="#555555"/><rect x="4" y="31" width="89" height="1" fill="#FFFFFF"/>
<text x="4" y="39" font-size="6" fill="#555555" font-family="Consolas,monospace">攻击</text><text x="22" y="39" font-size="6" fill="#212121" font-family="Consolas,monospace">+12</text>
<text x="48" y="39" font-size="6" fill="#555555" font-family="Consolas,monospace">防御</text><text x="66" y="39" font-size="6" fill="#212121" font-family="Consolas,monospace">+8</text>
<text x="4" y="48" font-size="6" fill="#555555" font-family="Consolas,monospace">生命</text><text x="22" y="48" font-size="6" fill="#212121" font-family="Consolas,monospace">+20</text>
<text x="48" y="48" font-size="6" fill="#555555" font-family="Consolas,monospace">灵力</text><text x="66" y="48" font-size="6" fill="#212121" font-family="Consolas,monospace">+15</text>
<text x="4" y="57" font-size="6" fill="#555555" font-family="Consolas,monospace">修为</text><text x="22" y="57" font-size="6" fill="#212121" font-family="Consolas,monospace">1234</text>
<text x="48" y="57" font-size="6" fill="#555555" font-family="Consolas,monospace">悟性</text><text x="66" y="57" font-size="6" fill="#212121" font-family="Consolas,monospace">+3</text>
<text x="4" y="66" font-size="6" fill="#555555" font-family="Consolas,monospace">本源</text><text x="22" y="66" font-size="6" fill="#212121" font-family="Consolas,monospace">+5</text>
<text x="48" y="66" font-size="6" fill="#555555" font-family="Consolas,monospace">气运</text><text x="66" y="66" font-size="6" fill="#212121" font-family="Consolas,monospace">+2</text>
</g>
<line x1="307" y1="38" x2="317" y2="38" stroke="#373737" stroke-width="1"/><text x="321" y="42" fill="#212121" font-family="Consolas,monospace" font-size="11">位阶文字 y=0..7</text>
<line x1="307" y1="68" x2="317" y2="68" stroke="#373737" stroke-width="1"/><text x="321" y="72" fill="#212121" font-family="Consolas,monospace" font-size="11">刻度尺 y=10..17</text>
<line x1="307" y1="101" x2="317" y2="101" stroke="#373737" stroke-width="1"/><text x="321" y="105" fill="#212121" font-family="Consolas,monospace" font-size="11">进度条 y=22..28</text>
<line x1="307" y1="176" x2="317" y2="176" stroke="#373737" stroke-width="1"/><text x="321" y="180" fill="#212121" font-family="Consolas,monospace" font-size="11">属性区 y=32..67</text>
<text x="321" y="196" fill="#555555" font-family="Consolas,monospace" font-size="11">4 行 × 9px，两列</text>
<text x="14" y="286" fill="#373737" font-family="Consolas,monospace" font-size="11">97 × 72 · 文字全部由代码绘制，纹理只提供凹槽与刻线</text>
</svg>
</div>
<div class="cap">布局蓝图 — 坐标即代码可用常量</div>

<h2>四 · 刻度尺渲染规则（别搞反）</h2>
<p>纹理里那 10 个 8×8 凹槽是「没点的灯」。最左格 = <strong>9 阶</strong>（起点），最右格 = <strong>0 阶</strong>（目标）—— 因为玩家 level 是一路<em>减少</em>的，这样排布读起来才是一条自左向右推进的进度条。</p>
<div class="card pad0">
<svg width="460" height="120" viewBox="0 0 460 120" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
<defs><g id="cellx">
<rect width="24" height="24" fill="#8B8B8B"/><rect width="24" height="3" fill="#373737"/><rect y="3" width="3" height="18" fill="#373737"/><rect y="21" width="24" height="3" fill="#FFFFFF"/><rect x="21" y="3" width="3" height="21" fill="#FFFFFF"/>
</g></defs>
<text x="20" y="18" fill="#8A7A62" font-family="Consolas,monospace" font-size="11">格子 i</text>
<g>
<rect x="20" y="30" width="24" height="24" fill="#6B5540"/><rect x="23" y="33" width="18" height="18" fill="#8A6E4B"/>
<rect x="50" y="30" width="24" height="24" fill="#6B5540"/><rect x="53" y="33" width="18" height="18" fill="#8A6E4B"/>
<rect x="80" y="30" width="24" height="24" fill="#6B5540"/><rect x="83" y="33" width="18" height="18" fill="#8A6E4B"/>
<rect x="110" y="30" width="24" height="24" fill="#000000"/><rect x="113" y="33" width="18" height="18" fill="#7B5EA7"/>
<rect x="140" y="30" width="24" height="24" fill="#8B8B8B"/><rect x="140" y="30" width="24" height="3" fill="#373737"/><rect y="30" x="140" width="3" height="24" fill="#373737"/><rect x="140" y="51" width="24" height="3" fill="#FFFFFF"/>
<rect x="170" y="30" width="24" height="24" fill="#8B8B8B"/><rect x="170" y="30" width="24" height="3" fill="#373737"/><rect y="30" x="170" width="3" height="24" fill="#373737"/><rect x="170" y="51" width="24" height="3" fill="#FFFFFF"/>
<rect x="200" y="30" width="24" height="24" fill="#8B8B8B"/><rect x="200" y="30" width="24" height="3" fill="#373737"/><rect y="30" x="200" width="3" height="24" fill="#373737"/><rect x="200" y="51" width="24" height="3" fill="#FFFFFF"/>
<rect x="230" y="30" width="24" height="24" fill="#8B8B8B"/><rect x="230" y="30" width="24" height="3" fill="#373737"/><rect y="30" x="230" width="3" height="24" fill="#373737"/><rect x="230" y="51" width="24" height="3" fill="#FFFFFF"/>
<rect x="260" y="30" width="24" height="24" fill="#8B8B8B"/><rect x="260" y="30" width="24" height="3" fill="#373737"/><rect y="30" x="260" width="3" height="24" fill="#373737"/><rect x="260" y="51" width="24" height="3" fill="#FFFFFF"/>
<rect x="290" y="30" width="24" height="24" fill="#8B8B8B"/><rect x="290" y="30" width="24" height="3" fill="#373737"/><rect y="30" x="290" width="3" height="24" fill="#373737"/><rect x="290" y="51" width="24" height="3" fill="#FFFFFF"/>
</g>
<text x="20" y="72" fill="#8A7A62" font-family="Consolas,monospace" font-size="11">level</text>
<text x="26" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">9</text><text x="56" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">8</text><text x="86" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">7</text><text x="116" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">6</text><text x="146" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">5</text><text x="176" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">4</text><text x="206" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">3</text><text x="236" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">2</text><text x="266" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">1</text><text x="296" y="90" fill="#C49054" font-family="Consolas,monospace" font-size="12">0</text>
<text x="20" y="112" fill="#8A7A62" font-family="Consolas,monospace" font-size="11">玩家 7 阶：i=0,1 已走过　i=2 当前　i=3..9 未达到</text>
</svg>
</div>
<div class="cap">示例为玩家 level = 7（凡尘）</div>
<table>
<tr><th>格子 i（自左）</th><th>对应 level</th><th>画法</th></tr>
<tr><td>i = 0 … 8 - 玩家level</td><td>9 … 玩家level+1</td><td>已走过 — 内部 6×6 填暗一档的境界色</td></tr>
<tr><td>i = 9 - 玩家level</td><td>= 玩家level</td><td>当前 — 填满境界色 + 1px <code>#000000</code> 描框</td></tr>
<tr><td>i 更大</td><td>玩家level-1 … 0</td><td>未达到 — 什么都不画，保持纹理原样</td></tr>
</table>

<h2>五 · 接入常量</h2>
<pre><code><span class="cm">// 面板 blit（位置由实测得出）</span>
g.blit(tex, guiLeft + <span class="kw">76</span>, guiTop + <span class="kw">7</span>, <span class="kw">0</span>, <span class="kw">0</span>, <span class="kw">97</span>, <span class="kw">72</span>);

REGION      (76, 7) .. (172, 78)      97 x 72
GLYPH       (4, 1)   6 x 6            境界徽记（纹理已画）
TITLE_TEXT  (12, 0)                   位阶文字起点
GAUGE_X     4 + i * 9   i = 0..9      10 个 8x8 凹槽
GAUGE_Y     10
BAR         (4, 22, 89, 7)            进度条凹槽（内区 6..92 x 23..27）
RULE1_Y     19 / 20                   刻线（暗 / 亮）
RULE2_Y     30 / 31
STATS_Y     32        STATS_LINE 9    属性区 4 行
STAT_COL_X  (4, 48)                   两列文字起点</code></pre>
<pre><code><span class="cm">// 刻度尺：最左 = 9 阶，最右 = 0 阶</span>
<span class="kw">for</span> (<span class="kw">int</span> i = <span class="kw">0</span>; i &lt; <span class="kw">10</span>; i++) {
    <span class="kw">int</span> lv = <span class="kw">9</span> - i;                              <span class="cm">// 反向映射</span>
    <span class="kw">int</span> gx = guiLeft + <span class="kw">80</span> + i * <span class="kw">9</span>;
    <span class="kw">int</span> gy = guiTop + <span class="kw">17</span>;
    <span class="kw">if</span> (lv &gt; rank.level()) {
        g.fill(gx + <span class="kw">1</span>, gy + <span class="kw">1</span>, gx + <span class="kw">7</span>, gy + <span class="kw">7</span>, <span class="kw">0xFF6B5540</span>);      <span class="cm">// 已走过</span>
    } <span class="kw">else if</span> (lv == rank.level()) {
        g.fill(gx + <span class="kw">1</span>, gy + <span class="kw">1</span>, gx + <span class="kw">7</span>, gy + <span class="kw">7</span>, realmColor);
        g.renderOutline(gx, gy, <span class="kw">8</span>, <span class="kw">8</span>, <span class="kw">0xFF000000</span>);         <span class="cm">// 当前</span>
    }
}

<span class="cm">// 进度条：内区 (81, 30) .. (92+76, 35)</span>
g.fill(guiLeft + <span class="kw">81</span>, guiTop + <span class="kw">30</span>, guiLeft + <span class="kw">81</span> + (<span class="kw">int</span>)(p * <span class="kw">87</span>), guiTop + <span class="kw">35</span>, <span class="kw">0xFF4AA24A</span>);</code></pre>

<h2>六 · 交付文件</h2>
<ul>
<li><code>textures/gui/rank_stats_mortal.png</code> — 97×72 凡尘（标准原版灰）</li>
<li><code>textures/gui/rank_stats_legend.png</code> — 97×72 传说</li>
<li><code>textures/gui/rank_stats_mythic.png</code> — 97×72 神话</li>
<li><code>tools/gui-design/gen_stats_panel.py</code> — 生成脚本（色板与布局常量在顶部）</li>
<li><code>tools/gui-design/check_stats.py</code> — 自检（结构断言 + 底色一致性 + 镶嵌覆盖验证）</li>
<li><code>tools/gui-design/preview/</code> — 本设计稿与各倍率预览图</li>
</ul>
<div class="card" style="margin-top:14px">
<p style="margin:0"><strong>三份主题底色强制统一为 <code>#C6C6C6</code></strong>（自检项）。若给传说/神话也染底，贴上背包会形成一块泾渭分明的色斑；主题差异只体现在凹槽线色与徽记色上。</p>
</div>
</div>
</body>
</html>
"""


def main():
    html = (TEMPLATE
            .replace("{{IMG_COMPOSITE}}", uri("stats_in_inventory_3x.png"))
            .replace("{{IMG_SOLO}}", uri("rank_stats_mortal_4x.png")))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"设计稿已生成: {OUT}")
    print(f"  大小: {OUT.stat().st_size / 1024:.1f} KB（图片已 base64 内嵌，单文件自包含）")


if __name__ == "__main__":
    main()
