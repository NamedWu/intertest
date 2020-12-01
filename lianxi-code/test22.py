# 生成器\
# 很多时候我们创建的元素都存在一定的规律，但是此时如果元素很大，我们将元素都列出来，保存在一个列表中，可能会占用很大的内存，而且很多时候我们仅仅使用列表中的少部分元素，狠
# 很多元素存储了，但是不用，占用了很大的内存空间，这样会造成资源浪费，我们需要使用一个有规律的算法保存这些数据，这样在使用的时候调用这些算法就可以了，
# 这个就是生成器
'''
通过列表推导式得到生成器，



'''

# [x for x in range(100000)]
'''newlist1 = [X * 3 for X in range(30)]
print(newlist1)
print(type(newlist1))  # 此时还是列表

newlist2 = (X * 3 for X in range(4))
print(newlist2)  # 此时不能输出生成器里面的内容
print(type(newlist2))  # 此时生成的为列表推导式

# 调用生成器,打印里面的内容
print(newlist2.__next__())  # 0
print(newlist2.__next__())  # 3

# 方法2 next（）
print(next(newlist2))  # 6
# 每次调用生成一个元素
# 如果调用的次数达到生成器中元素上线，会抛出异常 StopIteration
print(next(newlist2))

newlist3 = (X * 3 for X in range(8))

while True:
    try:
        e = next(newlist3)
        print(e)
    except StopIteration:
        print("没有更改多元素了")
        break


# 定义函数生成器，方式二：借助函数完成
# 只要函数出现了yield 关键字，说明函数就不是函数，变成了函数生成器
# 步骤
# 定义一个函数，函数中使用yield 关键字
# 调用函数，接收函数的结果
# 得到的结果就是生成器
# 借助next（），--next--
def func():
    n = 0
    while True:
        n += 1
        yield n  # 相当于return + 暂停


num = func()
print(num)

print(next(num))'''


# 斐波那契数列
'''def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b
        a, b = b, a+b
        n += 1


g = fib(8)
print(next(g))
print(next(g))
print(next(g))
print(next(g))'''


'''
生成器方法：
--next--：获取下一个元素
send （value）向每次生成器传值：注意，第一次调用send函数时，需要先传递none
'''
def gen():
    i = 0
    while i < 5:
        yield i
        temp =
        print('temp:', temp)
        i += 1
    return '没有多余的数据'


g = gen()
print(next(g))
print(next(g))
print(next(g))

# print(g.send(None))  # 调用send之前需要先send（None）
'''n1 = g.send('呵呵')
print(n1)
n2 = g.send('哈哈')
print(n2)'''