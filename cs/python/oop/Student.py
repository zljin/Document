'''
面向对象 1
创建一个Student类,继承父类Object类

1. __init__ 构造方法,
第一个参数永远是实例变量self,并且,调用时不用传递该参数,自动获取

一般将类属性绑定进去

2. 类方法：
一般参数中第一个参数为self的方法,为类方法,调用时不用传递该方法自动获取

3. 封装：
类方法的好处就是可以封装,如get_grade方法,你不知道他的细节,对象的属性也不会共享给别人


4. 实例的变量名如果以__开头,就变成了一个私有变量
如分数是个人隐私，我设置为私有，就不能直接用. 来访问

如果要访问请用get_Score() 和 set_Score()

'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.__score))

    def get_Score(self):
        return self.__score

    def set_Score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
# print('bart.score =', bart.__score) # 私有变量不能直接访问
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())