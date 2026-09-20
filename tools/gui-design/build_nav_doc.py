#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成右上角导航标签 + 进度条的设计稿 HTML（单文件自包含）。

输出：tools/gui-design/preview/rank-nav-design.html
"""

import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREVIEW = HERE / "preview"
OUT = PREVIEW / "rank-nav-design.html"


def uri(name):
    p = PREVIEW / name
    if not p.exists():
        return ""
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode("ascii")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>右上角导航标签 + 进度条 · 设计稿</title>
<style>
:root{color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:#141118;color:#E8DCC8;font-family:'Microsoft YaHei','Noto Sans SC',system-ui,sans-serif;font-size:14px;line-height:1.75}
.wrap{max-width:1180px;margin:0 auto;padding:30px 22px 70px}
h1{font-size:22px;margin:0 0 4px;color:#E8B254;letter-spacing:1px}
.sub{color:#9A8A72;font-size:13px;margin:0 0 28px}
h2{font-size:15px;margin:36px 0 12px;color:#C49054;border-left:3px solid #5C4127;padding-left:10px}
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
.cap{font-size:12px;color:#8A7A62;margin:8px 0 18px;text-align:center}
.cm{color:#7A6A52}
.kw{color:#B8860B}
.ask{border-left:3px solid #B8860B;background:#241A10;padding:12px 16px;border-radius:0 5px 5px 0;margin-bottom:12px}
.ask ol{margin:6px 0 0;padding-left:20px;color:#D8C9A8}
.ask li{margin:5px 0}
.done{border-left:3px solid #55A24A;background:#16210F;padding:10px 16px;border-radius:0 5px 5px 0;margin-bottom:16px;font-size:13px;color:#B8D8A8}
</style>
</head>
<body>
<div class="wrap">
<h1>右上角导航标签 + 晋升进度条 — 设计稿</h1>
<div class="sub">位阶 / 境界 / 职业 / 加成面板 / 已学法术 / 知识原理 · 嵌入被擦除的合成区（97 × 72）</div>

<div class="done"><strong>已更新：</strong>「知识原理」下方那条细框按你说的做成<strong>晋升进度条</strong>。原来 4 行按钮正好占满 72px，为塞下进度条，按钮从 14px 压到 12px、行距压到 3px，底部让出 6px。</div>

<h2>一 · 镶嵌效果</h2>
<div class="card pad0"><img src="{{IMG_SHOT}}" alt="镶嵌预览"></div>
<div class="cap">3 倍放大 · 底部绿色条即进度条（预览里填充约 35%；文字用系统中文小字模拟，游戏内由 MC 字体绘制）</div>

<h2>二 · 布局与坐标</h2>
<div class="card pad0">
<svg width="470" height="330" viewBox="0 0 470 330" xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges">
<defs>
<g id="b84"><rect width="84" height="12" fill="#8B8B8B"/><rect width="84" height="1" fill="#FFFFFF"/><rect y="1" width="1" height="10" fill="#FFFFFF"/><rect y="11" width="84" height="1" fill="#555555"/><rect x="83" y="1" width="1" height="11" fill="#555555"/></g>
<g id="b40"><rect width="40" height="12" fill="#8B8B8B"/><rect width="40" height="1" fill="#FFFFFF"/><rect y="1" width="1" height="10" fill="#FFFFFF"/><rect y="11" width="40" height="1" fill="#555555"/><rect x="39" y="1" width="1" height="11" fill="#555555"/></g>
</defs>
<g transform="translate(16,30) scale(4)">
<rect width="97" height="72" fill="#C6C6C6"/>
<use href="#b84" x="7" y="2"/>
<use href="#b40" x="7" y="17"/><use href="#b40" x="51" y="17"/>
<use href="#b40" x="7" y="32"/><use href="#b40" x="51" y="32"/>
<use href="#b84" x="7" y="47"/>
<rect x="7" y="62" width="84" height="6" fill="#212121"/>
<rect x="7" y="62" width="84" height="1" fill="#373737"/>
<rect x="7" y="63" width="1" height="4" fill="#373737"/>
<rect x="7" y="67" width="84" height="1" fill="#FFFFFF"/>
<rect x="90" y="63" width="1" height="5" fill="#FFFFFF"/>
<rect x="8" y="63" width="28" height="4" fill="#4AA24A"/>
<text x="49" y="11" font-size="7" fill="#212121" font-family="Consolas,monospace" text-anchor="middle">位阶</text>
<text x="27" y="26" font-size="7" fill="#212121" font-family="Consolas,monospace" text-anchor="middle">境界</text>
<text x="71" y="26" font-size="7" fill="#212121" font-family="Consolas,monospace" text-anchor="middle">职业</text>
<text x="27" y="41" font-size="7" fill="#212121" font-family="Consolas,monospace" text-anchor="middle">加成面板</text>
<text x="71" y="41" font-size="7" fill="#212121" font-family="Consolas,monospace" text-anchor="middle">已学法术</text>
<text x="49" y="56" font-size="7" fill="#212121" font-family="Consolas,monospace" text-anchor="middle">知识原理</text>
</g>
<line x1="270" y1="60" x2="286" y2="60" stroke="#373737" stroke-width="1"/><text x="290" y="64" fill="#212121" font-family="Consolas,monospace" font-size="11">y=2 全宽 84×12</text>
<line x1="270" y1="120" x2="286" y2="120" stroke="#373737" stroke-width="1"/><text x="290" y="124" fill="#212121" font-family="Consolas,monospace" font-size="11">y=17 两个 40×12</text>
<line x1="270" y1="180" x2="286" y2="180" stroke="#373737" stroke-width="1"/><text x="290" y="184" fill="#212121" font-family="Consolas,monospace" font-size="11">y=32 两个 40×12</text>
<line x1="270" y1="240" x2="286" y2="240" stroke="#373737" stroke-width="1"/><text x="290" y="244" fill="#212121" font-family="Consolas,monospace" font-size="11">y=47 全宽 84×12</text>
<line x1="270" y1="300" x2="286" y2="300" stroke="#373737" stroke-width="1"/><text x="290" y="304" fill="#212121" font-family="Consolas,monospace" font-size="11">y=62 进度条 84×6</text>
<text x="16" y="318" fill="#373737" font-family="Consolas,monospace" font-size="11">区域 97 × 72 · 按钮组左右居中（边距 7 / 6），文字与进度填充由代码绘制</text>
</svg>
</div>
<div class="cap">布局蓝图 — 坐标相对面板原点（面板本身在 guiLeft+76, guiTop+7）</div>
<table>
<tr><th>行</th><th>标签</th><th>x</th><th>y</th><th>尺寸</th></tr>
<tr><td>1</td><td>位阶</td><td>7</td><td>2</td><td>84 × 12（全宽）</td></tr>
<tr><td>2</td><td>境界</td><td>7</td><td>17</td><td>40 × 12</td></tr>
<tr><td>2</td><td>职业</td><td>51</td><td>17</td><td>40 × 12</td></tr>
<tr><td>3</td><td>加成面板</td><td>7</td><td>32</td><td>40 × 12</td></tr>
<tr><td>3</td><td>已学法术</td><td>51</td><td>32</td><td>40 × 12</td></tr>
<tr><td>4</td><td>知识原理</td><td>7</td><td>47</td><td>84 × 12（全宽）</td></tr>
<tr><td>—</td><td><strong>晋升进度条</strong></td><td>7</td><td>62</td><td>84 × 6（凹槽）</td></tr>
</table>

<h2>三 · 三态样式</h2>
<div class="card pad0"><img src="{{IMG_ATLAS}}" alt="按钮图集"></div>
<div class="cap">rank_nav_buttons.png · 4 倍放大 · 第 1 排宽按钮 84×12，第 2 排窄按钮 40×12（每排三态：常态/悬停/激活），第 3 排进度条凹槽 84×6</div>

<h2>四 · 进度条</h2>
<p>凹槽内区是 <code>(8, 63) .. (89, 66)</code>，即 <strong>82 × 4</strong>。填充由代码按比例画：</p>
<pre><code><span class="cm">// 凹槽</span>
g.blit(TEX, ox + <span class="kw">7</span>, oy + <span class="kw">62</span>, <span class="kw">0</span>, <span class="kw">24</span>, <span class="kw">84</span>, <span class="kw">6</span>);
<span class="cm">// 填充：内区 x 从 8 宽 82，y 从 63 高 4</span>
<span class="kw">int</span> w = (<span class="kw">int</span>)(progress * <span class="kw">82</span>);           <span class="cm">// progress = 0f..1f</span>
<span class="kw">if</span> (w &gt; <span class="kw">0</span>) g.fill(ox + <span class="kw">8</span>, oy + <span class="kw">63</span>, ox + <span class="kw">8</span> + w, oy + <span class="kw">67</span>, <span class="kw">0xFF4AA24A</span>);</code></pre>
<p>建议填充色 <code>#4AA24A</code>（柔和绿）。想更接近原版经验条那种亮绿，可换 <code>#80FF20</code>，但在灰色面板上会比较扎眼 —— 也可以按境界染色（凡尘铜 / 传说紫 / 神话金）。</p>

<h2>五 · 完整代码用法</h2>
<pre><code><span class="kw">private static final int</span>[] STATE_X_WIDE   = { <span class="kw">0</span>, <span class="kw">84</span>, <span class="kw">168</span> };
<span class="kw">private static final int</span>[] STATE_X_NARROW = { <span class="kw">0</span>, <span class="kw">40</span>, <span class="kw">80</span>  };
<span class="cm">// state: 0 = 常态, 1 = 悬停, 2 = 激活</span>

<span class="kw">int</span> ox = guiLeft + <span class="kw">76</span>, oy = guiTop + <span class="kw">7</span>;

g.blit(TEX, ox + <span class="kw">7</span>,  oy + <span class="kw">2</span>,  STATE_X_WIDE[state],   <span class="kw">0</span>,  <span class="kw">84</span>, <span class="kw">12</span>);   <span class="cm">// 位阶</span>
g.blit(TEX, ox + <span class="kw">7</span>,  oy + <span class="kw">17</span>, STATE_X_NARROW[state], <span class="kw">12</span>, <span class="kw">40</span>, <span class="kw">12</span>);   <span class="cm">// 境界</span>
g.blit(TEX, ox + <span class="kw">51</span>, oy + <span class="kw">17</span>, STATE_X_NARROW[state], <span class="kw">12</span>, <span class="kw">40</span>, <span class="kw">12</span>);   <span class="cm">// 职业</span>
g.blit(TEX, ox + <span class="kw">7</span>,  oy + <span class="kw">32</span>, STATE_X_NARROW[state], <span class="kw">12</span>, <span class="kw">40</span>, <span class="kw">12</span>);   <span class="cm">// 加成面板</span>
g.blit(TEX, ox + <span class="kw">51</span>, oy + <span class="kw">32</span>, STATE_X_NARROW[state], <span class="kw">12</span>, <span class="kw">40</span>, <span class="kw">12</span>);   <span class="cm">// 已学法术</span>
g.blit(TEX, ox + <span class="kw">7</span>,  oy + <span class="kw">47</span>, STATE_X_WIDE[state],   <span class="kw">0</span>,  <span class="kw">84</span>, <span class="kw">12</span>);   <span class="cm">// 知识原理</span>
g.blit(TEX, ox + <span class="kw">7</span>,  oy + <span class="kw">62</span>, <span class="kw">0</span>,                     <span class="kw">24</span>, <span class="kw">84</span>, <span class="kw">6</span>);    <span class="cm">// 进度条凹槽</span>

<span class="cm">// 文字：水平居中，垂直 y = 按钮y + 2（按钮高 12，字高 8）</span>
g.drawCenteredString(font, <span class="kw">"位阶"</span>, ox + <span class="kw">7</span> + <span class="kw">42</span>, oy + <span class="kw">4</span>, TEXT_COLOR[state]);</code></pre>

<h2>六 · 待你确认</h2>
<div class="ask">
<ol>
<li><strong>按钮样式</strong>：参考图是「浅底 + 黑字 + 亮边框」，我按 MC 原版改成了斜面凸起。<strong>如果你就想要那种扁平标签感</strong>，我可以换一版。</li>
<li><strong>点击后内容显示在哪</strong>：替换整个背包面板（标签页式），还是别处弹窗？这决定要不要给每个标签配各自的子面板背景。</li>
<li><strong>「加成面板」4 个字塞在 40px 按钮里</strong>，左右各只剩 4px。要不要把两列加宽到 42px（间距 0），或把字号压到 6px？</li>
<li><strong>进度条显示的是什么进度</strong>？当前阶位的晋升进度（所以进度条本身随境界变色），还是别的？</li>
</ol>
</div>
</div>
</body>
</html>
"""


def main():
    html = (TEMPLATE
            .replace("{{IMG_SHOT}}", uri("nav_in_inventory_3x.png"))
            .replace("{{IMG_ATLAS}}", uri("rank_nav_atlas_4x.png")))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"设计稿已生成: {OUT}")
    print(f"  大小: {OUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
