# 装饰器
# 特点
# 函数A是作为参数，函数B就接收了函数A作为参数
# 要有闭包的特点出现
"""
加入购物车
判断用户登录状态

"""


def func(number):
    count = 100

    def innner_func():
        nonlocal count
        for i in range(number):
            count +=1
            print("修改后count的值", count)

    return innner_func


ifunc = func(5)
ifunc()


# 函数作为参数
def test():
    print("test")


test = 2


def func3(f):
    print(f)
    f()


func3(test)


# 定义一个装饰器
def decorate(func):
    a = 100
    print("wraper外层打印")
    def wrapper():

        func()
        print('1111111')
        print('222222')
        print(a)

    print("wrapernei层打印")
    return wrapper


# 使用装饰器（函数需要扩展，但是函数不能修改，就需要使用装饰器）
@decorate
def house():
    print("房子没装修。。。")

# 1.house 被装饰函数，
# 2.被装饰函数作为参数传入给装饰器decorate，在程序底层完成
# 3.执行装饰器函数，执行完后内部返回的函数wrapper直接给了被装饰函数house


house()




