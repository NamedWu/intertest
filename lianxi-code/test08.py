# 登录校验
import time


def decorate(func):
    def wrapper(*args, **kwargs):
        print("正在校验中。。。")
        time.sleep(3)
        print("校验结束。。。")
        # 调用func函数
        func(*args, **kwargs)

    return wrapper


@decorate
def f1(n):
    for i in range(12):
        n += 1
    print(n)


@decorate
def f2(s):
    for i in s:
        print(i)


@decorate
def f3(list01, clazz = '1901'):
    print('{}班级学生如下'.format(clazz))
    for i in list01:
        print(i)


f1(3)
f2("string")
students = ["xiaohong", "xiaohai"]
f3(students)
