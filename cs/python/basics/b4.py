'''
title: 使用模块
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

# 默认变量和方法的作用域都是public

# _${variable_name}_ 特殊变量,可以被直接引用，但是有特殊用途
__author__ = 'Leonard Zou'

import sys

def test():
    # sys.argv 用list存储了命令行的所有参数
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        _tomanytip()

# _${methodName} 私有方法
def _tomanytip():
    print('Too many arguments!')

def _nonMethod():
    # pass 语句什么也不做。它用于那些语法上必须要有什么语句，但程序什么也不做的场合
    pass


'''
当我们在命令行运行hello模块文件时,Python解释器把一个特殊变量__name__置为__main__
而如果在其他地方导入该hello模块时,if判断将失败,这种if测试可以让一个模块通过命令行运行时执行一些额外的代码
'''
if __name__=='__main__':
    test()

