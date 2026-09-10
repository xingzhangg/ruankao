#!/usr/bin/env python3
"""把讲义里过长的正文段落在句末断开。

用法：
    python3 工具/拆长段.py --check 讲义/*.md     只报告，不改文件
    python3 工具/拆长段.py 讲义/*.md            就地改写

为什么在源文件做而不是在电子书生成时做：讲义是单一事实来源，电子书只是
派生物。在派生环节修，源头仍然是坏的——以后导 docx、导网页、课上直接读
原文都要各自再打一遍补丁。而且拆段是「在哪断」的编辑判断，不是机械转换，
藏在构建脚本里就没有 diff 可审。

**只加空行，不动一个字。** 三条保险：
  1. 只在句号、问号、叹号之后断，不在逗号分号处断
  2. 断点取最接近段落中点的那个，不是见句号就断，避免切得太碎
  3. 跳过代码块、表格、列表、引用、标题，也跳过落在加粗或行内代码内部的句号

拆不动的段落（整段没有安全断点）会被列出来。那不是「断在哪」的问题，
是一段里塞了太多东西，要改写不要硬断——见 `_讲义写作规范.md` 的段落条款。
"""
import io, re, sys

上限 = 180      # 超过这个字数就找地方断
最短 = 45       # 断出来的碎片不得短于此，避免孤儿句
警戒 = 200      # 处理后仍超过这个字数的，列出来提示人工改写


def _安全断点(p):
    点 = []
    for m in re.finditer(r'[。！？](?![」』）\)”"])', p):
        i = m.end()
        前 = p[:i]
        if 前.count('`') % 2:   continue    # 断点落在行内代码里
        if 前.count('**') % 2:  continue    # 断点落在加粗里
        点.append(i)
    return 点


def 拆段(p):
    if len(p) <= 上限:
        return [p]
    候选 = [i for i in _安全断点(p) if 最短 <= i <= len(p) - 最短]
    if not 候选:
        return [p]
    中 = len(p) // 2
    切 = min(候选, key=lambda i: abs(i - 中))
    return 拆段(p[:切].strip()) + 拆段(p[切:].strip())


def _是正文段(t):
    return (t and '\n' not in t and t[0] not in '#|>-*+'
            and not re.match(r'^\d+[\.、]', t) and not t.startswith('```'))


def 处理(md):
    出, 在码块 = [], False
    for 块 in md.split('\n\n'):
        t = 块.strip()
        if t.count('```') % 2:
            在码块 = not 在码块
        if 在码块 or not _是正文段(t):
            出.append(块)
            continue
        出.append('\n\n'.join(拆段(t)))
    return '\n\n'.join(出)


def 顽固段(md):
    return [t for t in (b.strip() for b in md.split('\n\n'))
            if _是正文段(t) and len(t) > 警戒]


if __name__ == '__main__':
    args = sys.argv[1:]
    只查 = '--check' in args
    文件 = [a for a in args if a != '--check']
    if not 文件:
        sys.exit(__doc__)
    改动, 新增, 顽固 = 0, 0, []
    for f in 文件:
        s = io.open(f, encoding='utf-8').read()
        n = 处理(s)
        assert re.sub(r'\s+', '', s) == re.sub(r'\s+', '', n), f'{f} 内容被改动了，中止'
        for t in 顽固段(n):
            顽固.append((f, len(t), t[:40]))
        if s != n:
            改动 += 1
            新增 += n.count('\n\n') - s.count('\n\n')
            if not 只查:
                io.open(f, 'w', encoding='utf-8').write(n)
    动词 = '需要分段' if 只查 else '已分段'
    print(f'{len(文件)} 个文件，{改动} 个{动词}，共 {新增} 处')
    print(f'仍超 {警戒} 字、自动拆不动、建议人工改写的段落：{len(顽固)} 个')
    for f, L, t in sorted(顽固, key=lambda x: -x[1])[:10]:
        print(f'  {L:>4} 字  {f.split("/")[-1][:24]:<26} {t}…')
