'''
title: 函数

内置函数
函数定义

'''

print("---内置函数---")
print(max(2,5,6))
print(float('12.34'))
print(str(1.23))
print(int(12.34))
print(int('123'))
print(bool(2))
print(bool(''))


print("---自定义函数---")
# 传 *args 变为元组
# 传 **kw 变为dict
# country 提供defalut值
def info(name,age,country = 'CN',*args):
    print('姓名:',name)
    print('年龄:',age)
    print('国籍：',country)
    print(args[0])
    print(args[1])

info('bob',12,'CHINA','b','a')

def info2(name,age,country = 'CN',**kw):
    print('姓名:',name)
    print('年龄:',age)
    print('国籍：',country)
    print(kw)

info2('bob2',13,'CHINA', sex="Male", province="HeBei")


print("---递归函数---")
# 递归实现阶乘n! = (n-1)! × n
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))