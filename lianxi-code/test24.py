''''
面向对象
程序    现实中
对象    具体的事务


现实中的实物---转化为程序 ====面向对象

好处：
面向对象:
类
对象
属性
方法

对象：
    小明的手机
    小红的手机
    小妹的手机
    。。。
    对象的集合 ---共同的特征：品牌， 颜色，大小，价格     动作：打电话， 发短信，上网
    类别：手机类
    对象里面包含属性（特征）和方法（动作）
    多个对象----提取共同的属性和方法---封装成一个类



'''
# 所有的类名首字母大写，多个单词使用驼峰命名法
# 所有的类都默认继承object
# 类相当于一个模子
# 在模子中定义属性和方法，
'''

class 类名（父类）
     属性
     方法
'''


class phone(object):
    brand = 'vivo'


tom = phone()
print(tom.brand)
tom.brand = 'iphone'  # 修改类中的属性
print(tom.brand)


# 定义一个类和属性
class Student:
    # 类属性
    name = 'huawei'
    age = 2


# 使用类来创建对象
xiaowei = Student()
xiaowei.age = 13  # 对象属性
print(xiaowei.age)  # 先找对象属性，如果没有找到，再到类中 去找属性

# 类中的方法
# 普通方法、类方法 静态方法， 魔术方法
'''
普通方法
def 方法名（self{}）：


'''


class Car:
    price = 23000000
    type = 5
    __age = 3  # 私有变量，类外面不可以修改，可以借助类方法修改
    nickname = "xiaobao"

    # 魔术方法之一：称作魔术方法 ：————名字————（）
    def __init__(self):  # 只要创建了对象，系统自动调用初始化方法
        print("初始化")
        self.brand = 'benzi'  # 动态的给self空间中添加了两个属性
        self.seat = 7

    def run(self):  # self 是不断发生变化的，随着调用对象的改变而改变 只有对象去调用
        print('跑的很快')
        print('有:', self.seat)

    def drink(self):
        self.run()
        print("调用了run方法")

    # 类方法
    @classmethod
    def eat(cls):
        print(cls.nickname)  # 只能访问类属性
        # self.run()  # 会报错，类方法中不可以调用普通方法，因为缺少self

    @classmethod
    def update_age(cls):
        cls.__age = 20
        print("类方法")

    @classmethod
    def show_age(cls):
        print(cls.__age)


# Car.run()  这种写会报错，普通方法需要实例化后才能调用，类方法可以直接调用
Car.update_age()
Car.show_age()
ben = Car()
ben.seat = '7座'
ben.run()

bao = Car()
bao.seat = "5座"
bao.run()

ben.drink()


# 在系统中找是佛有一块空间是Car
# 利用Car类，向内存中申请一块和Car一样的空间
# 去Car中找是否有一种方法叫——__init__,如果没有则执行将开辟空间给个对象
# 如果有，会进入__init__则会执行里面的动作
# 最后将内存地址复制给bao/ben
# 函数和类里面定义的方法

# 类方法
'''
特点：
类方法中的参数不是对象中的，而是雷钟德
定义方法classmethod
类方法中只可以使用类属性
只要加上self，说明要依赖于对象
类中方法的调用需要加self.方法名()
所以普通方法不能在方法中调用，因为没有self
类方法的作用：
在对象还没出现之前的动作，可以放在类方法中
因为只能访问类属性和类方法，所以在创建对象之前创建，如果需要完成一些动作（功能）


'''
