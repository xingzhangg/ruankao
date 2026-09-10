#!/bin/bash
# 把讲义合成 PDF 和 EPUB。用法：bash 工具/生成电子书.sh [起] [止]
# 例：bash 工具/生成电子书.sh 1 53
#
# ⚠️ 变量名一律用 ASCII —— bash 不支持中文变量名，用了会报 "command not found"。
set -e
FROM=${1:-1}
TO=${2:-53}
ROOT=$(cd "$(dirname "$0")/.." && pwd)
# ⚠️ 工作目录必须在 /private/tmp 下 —— make-pdf 拒绝写其他位置
#    （mktemp -d 默认给 /var/folders/...，会报 "Path must be within: /private/tmp, <repo>"）
WORK=$(mktemp -d /private/tmp/ruankao-book.XXXXXX)
NAME="软考讲义合订本（$(printf %02d "$FROM")-$(printf %02d "$TO")）"
PDFBIN="$HOME/.claude/skills/gstack/make-pdf/dist/pdf"

echo "[1/5] 合并 markdown"
python3 "$ROOT/工具/生成合订本.py" "$FROM" "$TO" "$WORK/book.md"

# PDF：A4，页边距 0.45in 是为了容下最宽的 ASCII 时空图（约 100 显示列）
echo "[2/5] 生成 PDF"
"$PDFBIN" generate "$WORK/book.md" "$WORK/$NAME.pdf" \
  --cover --toc --page-size a4 --margins 0.45in --no-confidential \
  --title "$NAME" --author "软考·软件设计师（中级）备考" --date "$(date +%F)"

# make-pdf 没有控制书签深度的参数，生成后再裁：713 条砍到 66 条，与 EPUB 目录对齐
echo "[3/5] 精简 PDF 书签"
python3 "$ROOT/工具/精简PDF书签.py" "$WORK/$NAME.pdf"

# EPUB 封面取 PDF 首页；内部文件名必须全 ASCII，带中文的内部路径会让部分阅读器解包失败
echo "[4/5] 生成封面"
mkdir -p "$WORK/cv"
qlmanage -t -s 1400 -o "$WORK/cv" "$WORK/$NAME.pdf" >/dev/null 2>&1
cp "$WORK/cv/"*.png "$WORK/cover.png"

cat > "$WORK/epub.css" <<'CSS'
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

cat > "$WORK/meta.yaml" <<YAML
---
title: $NAME
creator:
  - role: author
    text: 软考·软件设计师（中级）备考
language: zh-CN
date: $(date +%F)
---
YAML

# 目录只到一级（讲义标题）：开到 3 级时 22 篇就有 292 条，微信读书里堆成一面墙
echo "[5/5] 生成 EPUB"
pandoc "$WORK/meta.yaml" "$WORK/book.md" \
  -f markdown+pipe_tables+backtick_code_blocks -t epub3 \
  --toc --toc-depth=1 --split-level=1 \
  --css "$WORK/epub.css" --epub-cover-image "$WORK/cover.png" \
  --resource-path="$WORK:$ROOT" \
  -o "$WORK/$NAME.epub"

cp "$WORK/$NAME.pdf" "$WORK/$NAME.epub" "$HOME/Desktop/"
echo "已生成到桌面："
ls -lh "$HOME/Desktop/$NAME.pdf" "$HOME/Desktop/$NAME.epub"
