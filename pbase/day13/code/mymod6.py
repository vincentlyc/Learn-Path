# mymod6.py

''' 此模塊示意__all__列表作用和用法
'''

# 限制 用 from mymod6 import *時導入 f1, var1
__all__ = ['f1', 'var1']


def f1():
    pass


def f2():
    pass


def f3():
    pass


var1 = 'hello'
var2 = 'myworld'
