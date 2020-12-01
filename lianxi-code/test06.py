# 闭包
# 保存，返回闭包时的变量的范围和状态（外层函数变量的状态）
# 闭包需要有内层函数
# 闭包内层函数需要调用外层函数变量
# 返回出内层函数

def func(a, b):
    c = 10

    def inner_func():
        s = a + b + c
        print("相加之和的结果是：", s)

    return inner_func


ifunc = func(2, 3)
ifun1 = func(2, 8)
ifunc()


def funv():
    c = 1

    def funb():
        print("时间")

    def funN():
        funb()
        print("funN")

    return funN


ifun2 = funv()
ifun2()


# 计数器
def generate_count():
    counter = [0]

    def add_one():
        # nonlocal counter 不需要加局部变量注释，因为是列表，列表是可变的
        counter[0] += 1
        print("当前是第{}次调用".format(counter))

    return add_one


counter = generate_count()
counter()
counter()
