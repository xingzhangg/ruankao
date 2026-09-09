#!/usr/bin/env python3
"""把讲义合并成一份 PDF 用的长 markdown。

用法：
    python3 工具/生成合订本.py 1 22 [输出.md]

按编号顺序拼接 `讲义/NN-*.md`，板块切换处插一页分隔页。
每篇的「知识点范围」头部行是内部索引，对读者是噪音，删掉；
「真题依据｜有无计算、是否阶段B」那行保留。正文一字不动。
"""
import io, re, sys, glob, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEC = os.path.join(ROOT, '讲义')

# 板块序号 → 中文序数，用于分隔页标题
ORD = '一二三四五六七八九十'


def 收集(起, 止):
    out = []
    for f in sorted(os.listdir(LEC)):
        m = re.match(r'^(\d{2})-([^-]+)-(.+)\.md$', f)
        if not m:
            continue
        n = int(m.group(1))
        if 起 <= n <= 止:
            out.append((n, m.group(2), os.path.join(LEC, f)))
    return out


def 正文(路径):
    s = io.open(路径, encoding='utf-8').read()
    # 删掉指向内部转录本的「知识点范围」头部行
    s = re.sub(r'^> 知识点范围：.*(?:\n(?!\n)[^>\n].*)*\n', '', s, flags=re.M)
    # 合并后的 md 不在 讲义/ 下，图片的相对路径会失效，改成绝对路径
    s = re.sub(r'\]\(\.\./', '](' + ROOT + '/', s)
    return s.rstrip() + '\n'


def 构建(起, 止, 目标):
    篇 = 收集(起, 止)
    if not 篇:
        sys.exit(f'讲义/ 下没有编号 {起}-{止} 的文件')
    块, 上个板块, 板块号 = [], None, 0
    for n, 板块, 路径 in 篇:
        if 板块 != 上个板块:
            板块号 += 1
            同板块 = [x for x in 篇 if x[1] == 板块]
            范围 = f'{同板块[0][0]:02d}–{同板块[-1][0]:02d}'
            块.append(f'# 第{ORD[板块号-1]}部分 · {板块}\n\n'
                      f'本部分收讲义 {范围}，共 {len(同板块)} 课。\n')
            上个板块 = 板块
        块.append(正文(路径))
    md = '\n\n'.join(块) + '\n'
    io.open(目标, 'w', encoding='utf-8').write(md)
    return 篇, 板块号, len(md)


if __name__ == '__main__':
    起 = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    止 = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    目标 = sys.argv[3] if len(sys.argv) > 3 else f'/tmp/讲义{起:02d}-{止:02d}.md'
    篇, 板块数, 字符 = 构建(起, 止, 目标)
    print(f'{len(篇)} 篇 / {板块数} 个板块 / {字符:,} 字符 → {目标}')
