import random
print(random.randrange(1,7))
print(random.choice('hello world'))
print(random.sample([1,2,3,4,5],3))



def v_code():
    code = ""
    for i in range(4):
        num = random.randint(0,9)             #随机选择0~9
        A1Z1 = chr(random.randint(65,90))     #随机选择A~Z
        a1z1 = chr(random.randint(97,122))    #随机选择a~z
        add = random.choice([num,A1Z1,a1z1])  #随机选择其中一个
        code = "".join([code,str(add)])       #拼接一次选到的元素
    return code                               #返回验证码#
print(v_code())