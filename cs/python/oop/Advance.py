'''
面向对象 高级编程

1. __slots__
用tuple定义允许绑定的属性名称

2. @property ---> 对类的get和set属性方法的优化升级写法

把一个getter方法变成属性,只需要加上@property就可以了,

此时,@property本身又创建了另一个装饰器@score.setter,
负责把一个setter方法变成属性赋值,
于是,我们就拥有一个可控的属性操作

!!! 要特别注意：属性的方法名不要和实例变量重名
# 方法名称和实例变量均为birth:
    @property
    def birth(self):
        return self.birth # !!!是错误的

3. 支持多种继承

class Dog(Mammal, Runnable):
    pass
    
MixIn 的命名规范,代表多继承出来的是实现某一个功能,可以更好的看出继承关系

class Dog(Mammal, RunnableMixIn):
    pass


4. 类的特殊方法

__str__ ---> java toString()

__init__() --> java 构造方法

__del__() --> 对象的销毁方法

__doc__() ---> print(Func.__doc__) 表示类的描述信息

5. python的反射-->metaclass 使用元类
todo
'''

class Student(object):
    __slots__ = ('name', 'score')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

