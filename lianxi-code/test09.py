# 装饰器两层
def func(f):
    def wrapper():
        f()
        print("刷漆")
    print("执行完了装饰函数1")
    return wrapper



def func2(f1):
    def wrapper1():
        f1()
        print("铺地板")
    print("执行完了装饰函数2")
    return wrapper1


@func2
@func
def house():
    print("我是毛坯房")


house()
# 执行步骤
# 调用装饰器后，先执行靠近装饰器的方法，在执行后面的装饰器方法
# 首先将被装饰函数作为参数传入装饰函数，再执行装饰函数中的代码
# 最后将装饰函数子函数返回给被装饰函数

# house 执行步骤
# 首先执行装饰函数 func, 将house作为参数传递给func，打印print 内容，将wrapper函数返回给house
# 其次执行装饰函数func2， 此时将wrapper作为参数传递给func2，打印print内容，将wrapper1 函数返回给 wrapper
# 再次执行 wrapper1 中的内容，
# 执行f1（wrapper），
# wrapper执行顺序，首先执行f()函数，此时f函数还是只house函数，在print
# 再执行wrapper1中的print
