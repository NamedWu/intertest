# 装饰器带参数，那就需要在原来的装饰器上再加上层函数，即总共需要添加3层函数
# 第一层函数添加装饰器参数，第二层相当于将被装饰函数作为参数传入装饰器，第三层执行装饰器函数内容


def outer(a):  # 第一层负责接装饰器参数
    def decorate(func):  # 第二层负责接收被装饰器函数
        def wrapper(*args, **kwargs):  # 负责接收被装饰函数的参数
            func(*args)
            print("铺砖{}块。。。。。。".format(a))
        return wrapper
    return decorate


@outer(a=10)
def house(time):
    '''
    :param time:
    :return:
    '''
    print("我{}日期拿到放钥匙，我是毛坯房".format(time))


house('2020-6-12')


@outer(a=100)
def street():
    print("新修的街道，名字是:宁围街道")

street()