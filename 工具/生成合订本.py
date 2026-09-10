#!/usr/bin/env python3
"""把讲义合并成一份 PDF/EPUB 用的长 markdown。

用法：
    python3 工具/生成合订本.py 1 53 [输出.md]

按编号顺序拼接 `讲义/NN-*.md`，板块切换处插一页分隔页。
每篇的「知识点范围」头部行是内部索引，对读者是噪音，删掉；
「真题依据｜有无计算、是否阶段B」那行保留。正文一字不动。

⚠️ 文件名有三种形状，都要认：
    08-数据结构与算法-基础概念与线性表（√）.md   三段
    46-标准化与知识产权（√）.md                  两段（无课题段）
    49-下午题1-数据流图DFD实战（√）.md           板块段带序号，要归并成「下午题」
早先只认三段形状，46 和 47 被静默跳过，整本书少两课还不报错。
"""
import io, re, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEC = os.path.join(ROOT, '讲义')

_数 = '零一二三四五六七八九十'


def 中文序数(n):
    """1→一，10→十，11→十一，20→二十，21→二十一。够用到几十。"""
    if n <= 10:
        return _数[n]
    if n < 20:
        return '十' + _数[n - 10]
    return _数[n // 10] + '十' + (_数[n % 10] if n % 10 else '')


def 收集(起, 止):
    出 = []
    for f in sorted(os.listdir(LEC)):
        if not re.match(r'^\d{2}-', f) or f.startswith('00-'):
            continue
        base = re.sub(r'（√）\.md$|\.md$', '', f)
        段 = base.split('-', 2)
        n = int(段[0])
        if not (起 <= n <= 止):
            continue
        板块 = re.sub(r'^下午题\d$', '下午题', 段[1]) if len(段) > 1 else '其他'
        课题 = 段[2] if len(段) > 2 else 段[1]      # 两段形状：板块即课题
        出.append((n, 板块, 课题, os.path.join(LEC, f)))
    return 出


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

    # 硬断言：编号必须连续无缺口，防止文件名形状变化导致静默丢课
    实到 = sorted(p[0] for p in 篇)
    应到 = [n for n in range(起, 止 + 1)
            if any(f.startswith(f'{n:02d}-') for f in os.listdir(LEC))]
    缺 = sorted(set(应到) - set(实到))
    if 缺:
        sys.exit(f'解析失败，这些编号的文件存在却没被收进来：{缺}\n'
                 f'多半是文件名形状变了，检查 收集() 的解析逻辑')

    块, 上个, 板块号 = [], None, 0
    for n, 板块, 课题, 路径 in 篇:
        if 板块 != 上个:
            板块号 += 1
            同 = [x for x in 篇 if x[1] == 板块]
            块.append(f'# 第{中文序数(板块号)}部分 · {板块}\n\n'
                      f'本部分收讲义 {同[0][0]:02d}–{同[-1][0]:02d}，共 {len(同)} 课。\n')
            上个 = 板块
        块.append(正文(路径))
    md = '\n\n'.join(块) + '\n'
    io.open(目标, 'w', encoding='utf-8').write(md)
    return 篇, 板块号, len(md)


if __name__ == '__main__':
    起 = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    止 = int(sys.argv[2]) if len(sys.argv) > 2 else 53
    目标 = sys.argv[3] if len(sys.argv) > 3 else f'/tmp/讲义{起:02d}-{止:02d}.md'
    篇, 板块数, 字符 = 构建(起, 止, 目标)
    print(f'{len(篇)} 篇 / {板块数} 个板块 / {字符:,} 字符 → {目标}')
