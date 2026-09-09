#!/bin/bash
# 把讲义合成 PDF 和 EPUB。用法：bash 工具/生成电子书.sh [起] [止]
# 例：bash 工具/生成电子书.sh 1 22
set -e
起=${1:-1}; 止=${2:-40}
根=$(cd "$(dirname "$0")/.." && pwd)
工作=$(mktemp -d)
名="软考讲义合订本（$(printf %02d $起)-$(printf %02d $止)）"
PDF工具="$HOME/.claude/skills/gstack/make-pdf/dist/pdf"

python3 "$根/工具/生成合订本.py" "$起" "$止" "$工作/book.md"

# PDF：A4，页边距 0.45in 是为了容下最宽的 ASCII 时空图（约 100 显示列）
"$PDF工具" generate "$工作/book.md" "$工作/$名.pdf" \
  --cover --toc --page-size a4 --margins 0.45in --no-confidential \
  --title "$名" --author "软考·软件设计师（中级）备考" --date "$(date +%F)"

# EPUB：微信读书等阅读器用。封面取 PDF 首页；内部文件名必须全 ASCII，
# 带中文的内部路径会让部分阅读器解包失败
mkdir -p "$工作/cv" && qlmanage -t -s 1400 -o "$工作/cv" "$工作/$名.pdf" >/dev/null 2>&1
cp "$工作/cv/"*.png "$工作/cover.png"

cat > "$工作/epub.css" <<'CSS'
body { line-height: 1.7; }
h1 { page-break-before: always; font-size: 1.35em; margin: 1.2em 0 0.8em; }
h2 { font-size: 1.15em; margin: 1.4em 0 0.6em; }
h3 { font-size: 1.03em; margin: 1.2em 0 0.5em; }
blockquote { margin: 0.8em 0; padding: 0.4em 0.9em; border-left: 3px solid #bbb; color: #444; }
pre { white-space: pre; overflow-x: auto; font-size: 0.62em; line-height: 1.35;
      font-family: "Menlo","Consolas","DejaVu Sans Mono","Courier New",monospace;
      padding: 0.6em 0.7em; background: #f6f6f6; border-radius: 4px;
      -webkit-hyphens: none; hyphens: none; word-break: keep-all; }
pre code { white-space: pre; font-family: inherit; font-size: inherit; }
code { font-family: "Menlo","Consolas",monospace; font-size: 0.88em; }
table { border-collapse: collapse; width: 100%; font-size: 0.9em; }
th, td { border: 1px solid #ccc; padding: 0.3em 0.5em; }
img { max-width: 100%; }
CSS

cat > "$工作/meta.yaml" <<YAML
---
title: $名
creator:
  - role: author
    text: 软考·软件设计师（中级）备考
language: zh-CN
date: $(date +%F)
---
YAML

pandoc "$工作/meta.yaml" "$工作/book.md" \
  -f markdown+pipe_tables+backtick_code_blocks -t epub3 \
  --toc --toc-depth=3 --split-level=1 \
  --css "$工作/epub.css" --epub-cover-image "$工作/cover.png" \
  --resource-path="$工作:$根" \
  -o "$工作/$名.epub"

cp "$工作/$名.pdf" "$工作/$名.epub" "$HOME/Desktop/"
echo "已生成到桌面："; ls -lh "$HOME/Desktop/$名.pdf" "$HOME/Desktop/$名.epub"
