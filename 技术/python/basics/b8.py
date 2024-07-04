'''
title: 函数式编程

本质就是将函数参数化

高阶函数：
Map and Reduce

filter

sorted

匿名函数：
在java中lambda就是匿名函数的简化写法

返回函数：

闭包...todo
'''

def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(r))

print(list(r))


from functools import reduce

def fn(x, y):
    return x * 10 + y

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上,这个函数必须接收两个参数,reduce把结果继续和序列的下一个元素做累积计算
print(reduce(fn, [1, 3, 5, 7, 9]))



def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

