#!/usr/bin/env python3
"""精简不变量复核：讲义瘦身前后，三份清单不许少。

用法：
    python3 工具/精简不变量.py 旧讲义.md 新讲义.md [新题库.md]
    旧版一般用 git 取：git show HEAD:"讲义/NN-….md" > /tmp/old.md

比对的是「新讲义 + 新题库」合起来是否包含旧讲义的全部：
    题目清单   每条【真题…】/【模拟…】标注 + 紧随的题干首 30 字
    数值集合   正文里出现过的每一个数字串（头部引用行不算）
    术语集合   旧版加粗过的术语，新版正文里必须还找得到（不要求仍加粗）
另报：字符数降幅（>35% 要说明）、旧版 ### 小节标题在新版里消失的。
有任何一条硬违反退出码 1；退出码只是提醒导师去看清单，最终由导师裁定。
"""
import io, re, sys


def 读(p):
    return io.open(p, encoding='utf-8').read() if p else ''


def 题目(s):
    """只认「编号 + 标注」开头的题目行，正文里顺带提到的【真题】【模拟】字样不算。"""
    出 = []
    for m in re.finditer(r'^\W*\d+[.、．]\s*【(真题[^】]*|模拟[^】]*)】(.{0,60})', s, flags=re.M):
        题干 = re.sub(r'[\s*]+', '', m.group(2))[:30]
        出.append((m.group(1), 题干))
    return 出


def 去头(s):
    # 头部引用行不算；v1 定位里「前后关系」「分值与去向」两行是规范要求删掉的，也不算
    s = re.sub(r'^> .*$', '', s, flags=re.M)
    return re.sub(r'^\*\*(前后关系|分值与去向)\*\*.*$', '', s, flags=re.M)


def 数值(s):
    return set(re.findall(r'\d+(?:[.,]\d+)*', 去头(s)))


def 术语(s):
    出 = set()
    for t in re.findall(r'\*\*([^*\n]{1,24})\*\*', 去头(s)):
        t = t.strip('：:，,。 ')
        if t and not re.fullmatch(r'[\d.\s第节题A-D]+', t):
            出.add(t)
    return 出


def 小节(s):
    return [t.strip() for t in re.findall(r'^###\s+(.+)$', s, flags=re.M)]


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    旧 = 读(sys.argv[1])
    新 = 读(sys.argv[2])
    题库 = 读(sys.argv[3]) if len(sys.argv) > 3 else ''
    合 = 新 + '\n' + 题库
    违反 = 0

    # 1. 题目清单：多重集包含
    旧题, 新题 = 题目(旧), 题目(合)
    剩 = list(新题)
    缺题 = []
    for t in 旧题:
        if t in 剩:
            剩.remove(t)
        else:
            缺题.append(t)
    print(f'题目：旧 {len(旧题)} 道，新 {len(新题)} 道' + ('' if not 缺题 else f'，缺 {len(缺题)} 道 ✗'))
    for 标, 干 in 缺题:
        print(f'  ✗ 【{标}】{干}')
    违反 += bool(缺题)

    # 2. 数值集合
    缺数 = sorted(数值(旧) - 数值(合), key=lambda x: (len(x), x))
    print(f'数值：旧 {len(数值(旧))} 个不同数字' + ('' if not 缺数 else f'，缺 {len(缺数)} 个 ✗'))
    if 缺数:
        print('  ✗ ' + ' '.join(缺数))
    违反 += bool(缺数)

    # 3. 术语集合（新版正文里还能找到即可）
    正文合 = 去头(合)
    缺词 = sorted(t for t in 术语(旧) if t not in 正文合)
    print(f'术语：旧 {len(术语(旧))} 个加粗术语' + ('' if not 缺词 else f'，缺 {len(缺词)} 个 ✗'))
    for t in 缺词:
        print(f'  ✗ {t}')
    违反 += bool(缺词)

    # 4. 字符数降幅
    降 = 1 - len(合) / max(len(旧), 1)
    标记 = ' ⚠ 超过 35%，报告须逐条说明去向' if 降 > 0.35 else ''
    print(f'字符：旧 {len(旧):,} → 新讲义 {len(新):,} + 题库 {len(题库):,}，降幅 {降:.0%}{标记}')

    # 5. 消失的小节
    消失 = [t for t in 小节(旧) if t not in 小节(合)]
    print('小节：' + ('旧版 ### 标题全部保留' if not 消失 else f'{len(消失)} 个旧标题在新版找不到（改名或整节没了，报告须说明）'))
    for t in 消失:
        print(f'  ? {t}')

    print('\n结论：' + ('三清单齐全 ✓' if not 违反 else f'{违反} 项清单有缺 ✗，退回 agent 说明去向'))
    sys.exit(1 if 违反 else 0)


if __name__ == '__main__':
    main()
