# 私有化， 将属性name更改为了_Student__name，所以无法修改属性值
# 封装：1、私有化属性  2、定义公有的set get 方法
# __属性：将属性私有化，访问范围：仅仅限制在类中进行修改和访问
# 私有化好处
# 隐藏属性，不被外界随意修改
# 要修改的话可以通过函数修改 setxxx(self, XXX)
# 如果想要获取具体的某一个属性
# 使用getxxx (self)
# self 是指对象属性
# attribute : 方法名，属性

class Student:
    __age = 18  # 类属性

    def __init__(self, name, age, score):
        self.__age = age
        self.__name = name
        self.__score = score

    # 定义公有的set和get方法
    # set是为了赋值
    def setAge(self, age):
        if age > 0 and age < 100:
            self.__age = age
        else:
            print("年龄输入有误")

    # get是为了取值
    def getAge(self):
        return self.__age

    def __str__(self):
        return "姓名{}，年龄{}，分数{}".format(self.__name, self.__age, self.__score)

    # 相当于get 方法，先有getXXX ，将方法变成属性调用，可以将get方法转换为对象的属性直接调用
    @property
    def age(self):
        return self.__age

    # 再有set，因为set依赖于get  相当于装饰后的set方法  这两个方法是捆绑式的，每次都会一起执行
    @age.setter
    def age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("输入年龄有误")


tom = Student("tom", 25, 96)
print(tom)
# 借助setAge方法修改私有属性值
tom.setAge(220)
print("修改后的age：{}".format(tom.getAge()))
# 打印私有属性会报错
# print(tom.__score)
# 更改私有属性后值不会变化
tom.__score = 23  # 重新赋值后打印的值还是原来值
print(tom)
print(dir(Student))  # 打印类中包含的属性
print(dir(tom))

print(tom.age)
tom.age = 200  # 会自动执行set 的装饰方法

''''
class Student:
    def __init__(self, name, age)
        self.__name = name # 此时为私有属性，类外不可以访问

    @property   在类外可以调用此方法查看私有属性
    def name(self):
       return self.__name

    @name.setter   在类外调用该方法可以修改私有属性的值
    def name(self, name)
       self.__name = name

'''


class Person:
    def __init__(self):
        self.__money = 300

    def show(self):
        print("现在有{}元钱".format(self.__money))


class Student(Person):
    def __init__(self):
        super().__init__()
        self.__money = 700

    def show1(self):
        print("现在有{}元钱".format(self.__money))


s = Student()
s.show()   # ————money 首先从自己的类中查找 所以此时访问的是类Person 中的私有变量
s.show1()   # 先从自己的类中寻找变量，再从父类中寻找变量
