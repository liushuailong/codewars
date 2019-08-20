# -*- coding: utf-8 -*-

# print 打印带有颜色的信息
# 以 f开头表示在字符串内支持大括号内的python 表达式


def esc(code=0):
    return f'[{code}m'


print(esc('31;1;0') + 'Error:' + esc() + 'important')

# 在python中使用定时器



