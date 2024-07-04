'''
title: 数据类型

字符串
列表 ---> list
元组 ---> Immutable list,more safe
字典 ---> map
集合 ---> set
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("-----------------布尔值-------------------------")
print(True and False)
print(5 > 3 or 1 > 3)
print(not 1 > 2)

print("-----------------常量-------------------------")

# 通常用全部大写的变量名表示常量
PI = 3.14159265359

print("--------------- 字符串 -------------------------")

name = 'mike'
age = 9+9

print('244'.isdigit())
print('+'.join(['1','2','3']))
print('\n123'.strip())
print("1+2+3+4".split("+")) # gen list

# UTF-8编码中，1个中文字符占3字节，1个英文字符占1字节
s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))

# 字符串格式化

print('Age:%s Gender:%s' % (25,True)) # %s 万能转换为字符串
print('%2d-%02d' % (3, 1)) # 是否补0，2为占2位 %d 整数
print('%.2f' % 3.1415926) # 保留两位浮点数
print('growth rate: %d %%' % 7) # 转义：用%%来表示一个% 

# format用法
print("He is {0}, and she is also {0}. And they are {1} years old.".format(name, age))
print("He is {name}, and she is also {name}. And they are {age} years old.".format(name=name, age=age))
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format(name, 17.125))

# f-string用法
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

print("--------------- 列表 -------------------------")
foods = ['Rice','Noodles','Dumplings','Hamburger','bread']
foods2 = ['Hamburger','bread']
foods.extend(foods2)

print("切片",foods[1:3]) 
foods.pop()

for index,item in enumerate(foods):
    print(index,item)

print("----------------元组----------------------")
drink = ('Milk','Tea','Coffee','Coca Cola')
print(drink.index('Tea'))

b = (1) # 注意这不是元组，会造成歧义，如何解决？
d = (3,) # 解决方案：加个逗号，


print("--------------- 字典 ----------------------")
# dict key值是Immutable
job_type = {1:'teacher',2:"student",3:"engineer",4:"doctor"}

print(job_type.get(3,"defalut"))


# job_type.keys() job_type.values()
for k,v in job_type.items():
    print(k,v)

print("-------------- 集合 ------------------")
sports1 = set(['basketball','soccer','tennis'])

sports2 = set(['lol','pingpong','volleyball',"soccer"])

for index,item in enumerate(sports1):
    print(index,item)

for index,item in enumerate(sports2):
    print(index,item)

print("并集",sports1 | sports2)

print("差集",sports1.difference(sports2))

print("交集",sports1 & sports2)

