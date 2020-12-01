# 继承 is a has a
import random
'''
知识点
1、has a 
   一个类中使用了另外一个自定义的类型
   student 使用computer Book
2、类型
 系统类型
 str int float 
 list dirt tuple set
 自定义类型：
   算是自定义的类，都可以将其当成一种类型
   s =student
   s 是student 类型的对象
   



'''


# 声明一个road
class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def run(self, hour, Road):
        militer = hour*60

        print("{}在{}路上跑了{}米".format(self.name, Road.name, militer))

    def __str__(self):
        return self.name, self.job


# 定义一个car
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = "{}车在{}路上{}时以{}速度行驶了{}千米".format(self.brand, ran_time, road.name, self.speed, road.len)
        print(msg)

    def __str__(self):
        return self.brand, self.speed




# 创建实例化对象
r = Road("青藏高速", 1200)
C = Car("audi", 12)
r.name = "京沪高速"  # 非私有属性可以直接在外面访问
C.get_time(r) # 将对象作为类调用，对象里面的属性都可以访问


