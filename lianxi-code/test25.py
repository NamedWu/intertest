# 魔术方法
# __init__
# __new__  在实例化时触发,new 方法的作用个，开辟内存空间
'''
1、new
首先将new方法执行完之后会返回一个内存地址，之后将内存地址传递到init 方法中的self中，’
之后执行init方法，执行完之后将init执行完之后返回的地址赋值给对象
new 方法一定要return
2、call  对象调用
将对象当成函数用时，会默认调用call
3、del delete 的缩写，虚构魔术方法
#出发时机，当对象没有用（没有任何变量引用）的时候被触发
__del__:
1）。对象赋值
p = person()
p1= p
说明：p 和 p1 共同指向同一个地址
2）、删除地址的引用
del p 删除p1对地址的引用
查看对地址的引用次数
import sys
引用sys.getrecount(原始对象名)
当一块空间没有任何引用时，会默认执行del ，当没有引用时，python解释器会回收所有在本次执行过程中使用到的空间
垃圾回收是python底层自带的东西，垃圾回收：内存释放
3、str
# 触发时机，打印对象名的时候会自动调用__str__里面内容
# 注意：一定要在__str__ 方法中加入return


'''
import sys

class Person:
    def __init__(self, name, age):
        print(self)
        self.name = name
        self.age = age


    def __new__(cls, *args, **kwargs):
        print('new')
        position = super(Person, cls).__new__(cls)
        print(position)
        return position

    def __call__(self, name, age):
        print("call")
        print(name)

    def __del__(self):
        print("del")

    def __str__(self):
        return self.name, self.age


P = Person("xiaohong", 12)
print(P.name)

# 对象当成函数调用时会执行call
P('hello', 12)
# 对象赋值
n = 5
p1 = P
p2 = p1

del p2
print("删除p2之后打印", p.name)
print(sys.getrefcount(P))

# 单纯打印对象名称，出来的一个地址。地址对应对于开发者来说没有太大意义
# 如果想在打印对象名的时候给开发者更多的信息量
print(p1)


'''
总结:魔术方法  到达出现时机后自动调用函数
重点：1 ， 5
1、__init__作用：构造方法，创建完空间后第一个被调用的方法

2、__new__ 作用， 开辟空间

3、__call__作用， 想不想将对象当成函数用， 调用时机：到对象当成函数调用的时候，会调用这个方法，例如对象名（），执行时会自动调用call

4、__del__ 作用，没有指针引用的时候调用，99%都不需要重写

5、__str__ 作用：想要打印对象名的时候给开发者更多的信息（在调试的时候可以看到返回结果） 时机：打印对象名的时候会调用

'''


# 方法
'''
1、普通方法
def 方法名（参数）：
    pass
类名.方法名（）
对象.方法名（）

方法之间的调用
class A:
def a(self):
     pass
def b(self):
    self.a()
2、静态方法
@staticmethod
def 方法名（参数）：
pass
类名.方法名（）
对姓名.方法名（）

3、魔术方法
自动调用

4、类方法
@classmethod
def 方法名（cls，[参数]）
pass

类名。方法名（）
对象名.方法名（）





'''