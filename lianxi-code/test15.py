# 递归函数
'''
普通函数：def func():pass
匿名函数：lambda 参数：返回结果
递归函数: 普通函数的一种表现形式，自己调用自己
特点：
1.需要设定终点
2.通常会有一个入口
'''


def sum1(n):
    if n == 0:
        return 0
    else:
        return n+sum1(n-1)


result = sum1(2)
print(result)


def f1(n):
    if n > 0:
        print(n)
        f1(n-1)
    else:
        pass


f1(5)


def sum2(n):
    if n == 100:
        return 100
    else:
        return n + sum2(n+1)


sum2(99)
print(sum2(99))

