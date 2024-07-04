'''
title: 高级特性

1. 迭代器

2. 生成器

3. 装饰器

4. 切片

5. 列表生成器: 语法糖

'''

from collections.abc import Iterable

city = ['beijing','shanghai','tinajin','chongqin']

# 是否是可迭代对象，可迭代都可用迭代器
print(isinstance(city, Iterable))

for x in iter(city):
    print(x)

for index,item in enumerate(city):
    print(index,item)


# 字典迭代器
d = {'a': 1, 'b': 2, 'c': 3}

print(isinstance(d, Iterable))

for k in d:
    print(k,str(d[k]))

for v in d.values():
    print(v)



'''
生成器
有yield的关键字的函数为生成器函数
每次执行一次到yield的时候,函数会暂停执行,并将当前的值返回给调用者
当下一次迭代时,函数会从暂停的地方继续执行

目的：实现了按需生成数据的效果，避免了一次性生成所有数据并存储在内存中，提高了效率和节省了内存空间
'''
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()

# 继承上一次的指针
print(next(o))
print(next(o))
print(next(o))

# 指针永远返回1
print(next(odd()))
print(next(odd()))
print(next(odd()))



def generator(low,high):
    while low <= high:
        yield low
        low += 1


for i in generator(1,10):
    print(i,end='')



# 装饰器
import time
def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("run time %s"%(stop_time-start_time))
    return wrapper

@timer      #语法糖  test=timer(test)
def test():
    time.sleep(3)
    print("in the test")


# test()


# 切片
foods = ['Rice','Noodles','Dumplings','Hamburger','bread']
print("切片",foods[1:3]) 



# 列表生成器

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])


d = {'x': 'A', 'y': 'B', 'z': 'C' }

print([[k + '=' + v for k, v in d.items()]])


L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])