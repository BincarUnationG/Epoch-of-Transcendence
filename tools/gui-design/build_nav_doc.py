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

<div class="done"><strong>已更新：</strong>①按钮改成<strong>扁平标签</strong>（平面底色 + 1px 白边框，去掉斜面凸起）；②点击标签后<strong>替换整个背包面板</strong>，新增子面板框架 <code>rank_tab_panel.png</code>；③「位阶」栏直接显示当前 level；④底部是晋升进度条。</div>

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
<text x="12" y="11" font-size="7" fill="#212121" font-family="Consolas,monospace">位阶</text>
<text x="85" y="11" font-size="7" fill="#000000" font-family="Consolas,monospace" text-anchor="end" font-weight="bold">3 阶</text>
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

<h2>三 · 三态样式（扁平标签）</h2>
<div class="card pad0"><img src="{{IMG_ATLAS}}" alt="按钮图集"></div>
<div class="cap">rank_nav_buttons.png · 4 倍放大 · 第 1 排宽按钮 84×12，第 2 排窄按钮 40×12（每排三态：常态/悬停/激活），第 3 排进度条凹槽 84×6</div>
<table>
<tr><th>状态</th><th>底色</th><th>边框</th><th>文字</th></tr>
<tr><td>常态 idle</td><td><code>#C6C6C6</code>（= 面板色）</td><td>1px <code>#FFFFFF</code></td><td><code>#3C3C3C</code></td></tr>
<tr><td>悬停 hover</td><td><code>#D6D6D6</code></td><td>1px <code>#FFFFFF</code></td><td><code>#1A1A1A</code></td></tr>
<tr><td><strong>激活 active</strong></td><td><strong><code>#FFFFFF</code></strong></td><td>1px <code>#FFFFFF</code></td><td><code>#000000</code></td></tr>
</table>
<p>三态都是<strong>平面色块 + 1px 全边框</strong>，没有高光/阴影斜面 —— 这就是扁平标签感。激活态靠「整块变白」拉开差距，一眼能看出当前停在哪一页。</p>

<h2>四 · 进度条</h2>
<p>凹槽内区是 <code>(8, 63) .. (89, 66)</code>，即 <strong>82 × 4</strong>。填充由代码按比例画：</p>
<pre><code><span class="cm">// 凹槽</span>
g.blit(TEX, ox + <span class="kw">7</span>, oy + <span class="kw">62</span>, <span class="kw">0</span>, <span class="kw">24</span>, <span class="kw">84</span>, <span class="kw">6</span>);
<span class="cm">// 填充：内区 x 从 8 宽 82，y 从 63 高 4</span>
<span class="kw">int</span> w = (<span class="kw">int</span>)(progress * <span class="kw">82</span>);           <span class="cm">// progress = 0f..1f</span>
<span class="kw">if</span> (w &gt; <span class="kw">0</span>) g.fill(ox + <span class="kw">8</span>, oy + <span class="kw">63</span>, ox + <span class="kw">8</span> + w, oy + <span class="kw">67</span>, <span class="kw">0xFF4AA24A</span>);</code></pre>
<p>建议填充色 <code>#4AA24A</code>（柔和绿）。想更接近原版经验条那种亮绿，可换 <code>#80FF20</code>，但在灰色面板上会比较扎眼 —— 也可以按境界染色（凡尘铜 / 传说紫 / 神话金）。</p>

<h2>五 · 「位阶」栏直接显示 Rank level</h2>
<p>不用点进去 —— 这一栏左边是栏名、右边就是当前等级，画两段文字即可，<strong>纹理不用改</strong>：</p>
<table>
<tr><th>内容</th><th>位置</th><th>对齐</th><th>建议色</th></tr>
<tr><td>位阶</td><td>x = ox + 12</td><td>左对齐</td><td><code>#212121</code></td></tr>
<tr><td>3 阶</td><td>x = ox + 85 减去文字宽度</td><td>右对齐</td><td><code>#000000</code></td></tr>
</table>
<pre><code><span class="cm">// 左：栏名</span>
g.drawString(font, <span class="kw">"位阶"</span>, ox + <span class="kw">12</span>, oy + <span class="kw">4</span>, <span class="kw">0x212121</span>, <span class="kw">false</span>);
<span class="cm">// 右：当前 Rank level（右对齐 = 右边线 ox+85 减去文字宽度）</span>
String lv = rank.level() + <span class="kw">" 阶"</span>;
g.drawString(font, lv, ox + <span class="kw">85</span> - font.width(lv), oy + <span class="kw">4</span>, <span class="kw">0x000000</span>, <span class="kw">false</span>);</code></pre>
<p>想让等级更跳，可把数值换成境界色（凡尘铜 <code>#8A6E4B</code> / 传说紫 <code>#7B5EA7</code> / 神话金 <code>#A8853A</code>）—— 但这些色在 <code>#8B8B8B</code> 底面上对比度偏低，稳妥起见用黑色。</p>

<h2>六 · 点击后替换整个背包面板</h2>
<p>点任一标签 → 用 <code>rank_tab_panel.png</code>（176 × 166）整块替换原版背包面板；右上角导航区照旧贴按钮，所以随时能切到别的页。</p>
<div class="card pad0"><img src="{{IMG_TAB}}" alt="子面板预览"></div>
<div class="cap">点击「位阶」后（3 倍放大）· 左上深色区放标题与大字等级，下方凹槽放内容列表；导航与进度条位置不变</div>
<table>
<tr><th>区域</th><th>位置</th><th>尺寸</th><th>底色</th><th>用途</th></tr>
<tr><td>A 标题区</td><td>(7, 7)</td><td>69 × 72</td><td><code>#212121</code> 深色</td><td>当前标签名 + 大号数值</td></tr>
<tr><td>B 主内容区</td><td>(7, 83)</td><td>162 × 76</td><td><code>#8B8B8B</code> 凹槽</td><td>内容列表 / 属性</td></tr>
<tr><td>导航区</td><td>(76, 7)</td><td>97 × 72</td><td>面板色</td><td>贴按钮 + 进度条（不变）</td></tr>
</table>
<pre><code><span class="cm">// 切换页：背景整块换掉，坐标不变</span>
g.blit(RANK_TAB_PANEL, guiLeft, guiTop, <span class="kw">0</span>, <span class="kw">0</span>, <span class="kw">176</span>, <span class="kw">166</span>);
drawNav(g, guiLeft, guiTop, activeTab);   <span class="cm">// 导航照旧，只是 active 换一项</span>
drawPage(g, guiLeft, guiTop, activeTab);  <span class="cm">// 再在 A / B 区里画该页内容</span></code></pre>

<h2>七 · 完整代码用法</h2>
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

<span class="cm">// 文字：垂直 y = 按钮y + 2（按钮高 12，字高 8）</span>
<span class="cm">// 「位阶」栏 —— 左栏名 + 右数值，见第五节</span>
g.drawString(font, <span class="kw">"位阶"</span>, ox + <span class="kw">12</span>, oy + <span class="kw">4</span>, <span class="kw">0x212121</span>, <span class="kw">false</span>);
String lv = rank.level() + <span class="kw">" 阶"</span>;
g.drawString(font, lv, ox + <span class="kw">85</span> - font.width(lv), oy + <span class="kw">4</span>, <span class="kw">0x000000</span>, <span class="kw">false</span>);
<span class="cm">// 其余五栏：水平居中</span>
g.drawCenteredString(font, <span class="kw">"境界"</span>, ox + <span class="kw">7</span> + <span class="kw">20</span>, oy + <span class="kw">19</span>, TEXT_COLOR[state]);</code></pre>

<h2>八 · 待你确认</h2>
<div class="ask">
<ol>
<li><strong>六个标签点开后各显示什么？</strong> 现在只有「位阶」页填了示意（大字等级 + 境界/修为/攻击/防御/生命/灵力 六行）。其余五页（境界 / 职业 / 加成面板 / 已学法术 / 知识原理）需要你给内容清单，我才好排布。</li>
<li><strong>「加成面板」4 个字塞在 40px 按钮里</strong>，左右各只剩 4px（扁平标签去掉内斜面后略微宽松些）。要不要两列都加宽到 42px？</li>
<li><strong>进度条代表的进度</strong>是什么？当前阶位的晋升进度（那它该随境界变色吗），还是别的？</li>
<li><strong>子面板的 A 区</strong>（左上深色块）我放了大号等级数字。如果每页都用它显示各自的"主数值"（境界名 / 职业 / 法术数…），说一声我就统一这么排。</li>
</ol>
</div>
</div>
</body>
</html>
"""


def main():
    html = (TEMPLATE
            .replace("{{IMG_SHOT}}", uri("nav_in_inventory_3x.png"))
            .replace("{{IMG_ATLAS}}", uri("rank_nav_atlas_4x.png"))
            .replace("{{IMG_TAB}}", uri("tab_panel_rank_3x.png")))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"设计稿已生成: {OUT}")
    print(f"  大小: {OUT.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
