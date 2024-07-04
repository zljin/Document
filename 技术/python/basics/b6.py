'''
title: io

1. 文件读写流

mode:
https://docs.python.org/3/library/functions.html#open

2. 内存读写流 

StringIO # 字符
BytesIO # 字节

'''

try:
    f = open('../assets/1.txt', 'r',encoding='utf-8',errors='ignore')
    # read()会一次性读取文件的全部内容
    # print(f.read())
    for line in f.readlines():
         print(line.strip()) # 把末尾的'\n'删掉
finally:
    if f:
        f.close()

# try close的另外一种写法
with open('../assets/1.txt', 'a') as f:
    f.write('Hello, world!')


from io import StringIO,BytesIO
f = StringIO()
f.write('hello')
print(f.getvalue())
b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())