# 进程-线程-协程
# 举例 迅雷下载电影，首先将电影区分很多小块，再去下载
# 这里迅雷APP下载电影就是一个进程
# 很多小块组成一个线程
# 每个线程包含很多小块，这样每个小块又可以称为一个协程
from collections.abc import Iterable


def task1(n):
    for i in range(n):
        print("正在搬{}块砖".format(i))
        yield i


def task2(n):
    for i in range(n):
        print("正在听{}首歌".format(i))
        yield None


g1 = task1(5)
print(g1)
g2 = task2(6)

while True:
    try:
        g1.__next__()
        print(g1.__next__())
        g2.__next__()
    except:
          break

# 可迭代对象 1、生成器 2、元祖、列表、集合、字典、字符串 3、整数不可迭代
# 如何判断一个对象是否是可迭代的
list1 = [1, 2, 4, 5, 6, 7]
f = isinstance(list1, Iterable)
print(f)  # 返回结果为True 为可迭代的对象


''''
迭代器是访问集合元素的一种方式，迭代器是一个可以记住遍历位置的对象
迭代器对象从估计和的第一个元素开始访问，知道所有的元素访问完为止
迭代器是不会后退的
可以被next（）函数调用，并不段返回下一个值的对象成为迭代器
可迭代的是不是肯定就是迭代器？ 错误
例如：列表是可以迭代的
但是列表不是迭代器，使用next函数调用时会报错
生成器是迭代器，可以使用next函数调用
'''

# print(next(list1)) # 运行时报错，说明列表不是迭代器
list2 = [2, 3, 4, 56, 2]  # list2 此时还不是迭代器
# 将列表2 转化成迭代器
list2 = iter(list2)  # iter 函数是可以将可迭代的对象转化为迭代器
# list2 已经转化为迭代器了，此时可以使用next 函数调用list2
print(next(list2))


'''
生成器 与 迭代器
生成器是迭代器的一部分，但是迭代器不仅仅是生成器
因为可迭代元素可以转化为迭代器 ，通过iter  函数转换
'''