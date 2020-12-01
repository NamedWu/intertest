# 匿名函数: 简化函数定义
# 格式：lambda 参数1，参数2 ：运算

"""
def func():
    print("aaa")


def add(a,b):
    s = a+b
    return s
"""


s = lambda a, b: a + b
print(s)   # s就是一个函数

result = s(1, 2)
print(result)


# 匿名函数作为参数
def func(x, y, func1):
    print(x, y)
    print(func1)
    a = func1(x, y)
    print(a)


func(1, 2, lambda a, b: a*b)
