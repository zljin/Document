'''
面向对象 2

1. isinstance() 判断类型

2. 继承的优势: 多态
run_Animal(animal)

3. 对对象进行刨析的方法

type() 判断对象的类型
isinstance() 判断对象的类型
dir() 如果要获得一个对象的所有属性和方法
    getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态

    getattr(obj, 'z', 404) # 获取属性'z'如果不存在返回默认值404
    
    hasattr() # 如判断该fp对象是否存在read方法

4. 类属性和实例属性

直接在类定义一个变量即可,等效于java的static

但实例属性多是定义在构造方法里面的

'''

class Animal(object):
     def run(self):
        print('Animal is running...')


class Pig(Animal):
    # pass 什么都不做，用于创建一个最小结构的类
    pass

class Dog(Animal):
    """ 这里显示的是描述信息 """
    # 类属性
    version = 1

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

def run_Animal(animal):
    animal.run()

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型
d = Cat()


print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))

run_Animal(c)
run_Animal(d)

print(type(c))
print(dir(c))

# 显示类的描述信息
print(Dog.__doc__)