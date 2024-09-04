'''
题目
'''

# -*- coding: utf-8 -*-

print("题目:小明的成绩从去年的72分提升到了今年的85分,请计算小明成绩提升的百分点,并用字符串格式化显示出'xx.x%',只保留小数点后1位")
s1 = 72
s2 = 85

r = (s2-s1)/s1 * 100
print('%.1f %%' % r)
print('{0:.1f} %'.format(r))

print("----------------------------------------------------------------------------------------------------------------")

print("打印Apple")

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])


print("----------------------------------------------------------------------------------------------------------------")

print("小明身高1.75,体重80.5kg。请根据BMI公式(体重除以身高的平方)帮小明计算他的BMI指数,并根据BMI指数:低于18.5:过轻 18.5-25:正常 25-28:过重 28-32:肥胖 高于32:严重肥胖")

# if-else的写法

height=1.75
weight=80.5
bmi = weight/(height*height)

if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")

print("----------------------------------------------------------------------------------------------------------------")
print("你的年龄范围")

# match类似于java的switch
age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')



print("----------------------------------------------------------------------------------------------------------------")
print("匹配列表")
# match还能匹配列表
args = ['gcc', 'hello.c', 'world.c']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')

print("----------------------------------------------------------------------------------------------------------------")
print("求总和")

sum = 0
# range(10) 生成了一个包含 10 个值的链表
for x in range(101):
    sum = sum + x
print(sum)


n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

print("----------------------------------------------------------------------------------------------------------------")
print("导入模块")

import b4

b4.test()

print("----------------------------------------------------------------------------------------------------------------")
print("把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字")

def normalize(name):
    return str(name).lower().capitalize()
     
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)