# 多态
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("昵称：{},年龄：{}".format(self.name, self.age))


class Cat(Pet):
    def catch_mouse(self):
        print("{}猫能捉老鼠".format(self.name))


class Dog(Pet):
    def watch_house(self):
        print("{}狗能看门".format(self.name))


class Tiger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat_meat(self):
        print("{}不是宠物，很危险，会吃人".format(self.name))


class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):
        if isinstance(pet, Pet):  # 可以传入属于Pet的类，也可以传入不属于Pet的类
            print("{}可以饲养{}".format(self.name, pet.name))
        else:
            print("{}不可以饲养，不是宠物".format(pet.name))


P = Person("xiaohogn")
c = Cat("kitty", 12)
P.feed_pet(c)
t = Tiger("xinba", 13)
P.feed_pet(t)