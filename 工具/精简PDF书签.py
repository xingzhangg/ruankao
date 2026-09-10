#!/usr/bin/env python3
"""把 PDF 的书签只留一级（板块页 + 讲义标题）。

用法：python3 工具/精简PDF书签.py <file.pdf>

make-pdf 的 --outline 从全部标题层级生成书签，53 篇会得到 713 条，
把每课的「定位/开讲/一、二、三…/速记」全收了进去，手机 PDF 阅读器
的侧栏里根本没法翻。EPUB 那边已定为只到讲义标题（65 条），PDF 对齐。

make-pdf 没有控制书签深度的参数，所以只能生成后再裁。
正文里的小标题不受影响，只是不进导航。
"""
import sys, fitz

def 精简(路径):
    d = fitz.open(路径)
    旧 = d.get_toc()
    新 = [x for x in 旧 if x[0] == 1]
    d.set_toc(新)
    d.saveIncr()          # 增量保存，不重排页面、不改动正文
    d.close()
    return len(旧), len(新)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('用法：python3 工具/精简PDF书签.py <file.pdf>')
    旧, 新 = 精简(sys.argv[1])
    print(f'书签 {旧} → {新} 条')
