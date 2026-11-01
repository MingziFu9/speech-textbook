"""按正文中第一次引用的先后，重新给某一章的参考文献编号，并在每一类文献内按新编号排序。

用法：python tools/renumber_refs.py 04
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
nn = sys.argv[1]
f = next((ROOT / "docs/chapters").glob(f"{nn}-*/index.md"))
text = f.read_text(encoding="utf-8")
ch = int(nn)
body, refs = text.split("## 参考文献", 1)
refs, tail = refs.split("</div>", 1)
order = []
for k in re.findall(rf"#ref{ch}-(\d+)\)", body):
    if k not in order:
        order.append(k)
listed = re.findall(rf'<span id="ref{ch}-(\d+)"></span>', refs)
missing = [k for k in listed if k not in order]
if missing:
    print("警告：正文没有引用这些文献：", missing)
order += missing
new = {old: str(i) for i, old in enumerate(order, 1)}


def sub_body(m):
    return f"[[{new[m.group(1)]}]](#ref{ch}-X{new[m.group(1)]})"


body = re.sub(rf"\[\[\d+\]\]\(#ref{ch}-(\d+)\)", sub_body, body)
body = body.replace(f"#ref{ch}-X", f"#ref{ch}-")
# 文献列表：每一项从“- <span id=...>”开始，到下一项或分类标题之前
parts = re.split(r"(\n\*\*[^*\n]+\*\*\n)", refs)
out = []
for part in parts:
    items = re.findall(rf"(- <span id=\"ref{ch}-(\d+)\"></span>\[\d+\].*?)(?=\n- <span|\n*$)", part, re.S)
    if not items:
        out.append(part)
        continue
    renum = []
    for item, old in items:
        k = new[old]
        item = re.sub(rf'<span id="ref{ch}-\d+"></span>\[\d+\]', f'<span id="ref{ch}-{k}"></span>[{k}]', item, count=1)
        renum.append((int(k), item.rstrip()))
    renum.sort()
    out.append("\n\n" + "\n".join(i for _, i in renum) + "\n\n")
refs = "".join(out)
refs = re.sub(r"\n{3,}", "\n\n", refs)
f.write_text(body + "## 参考文献" + refs + "</div>" + tail, encoding="utf-8")
print("新编号：", ", ".join(f"{o}→{n}" for o, n in new.items()))
