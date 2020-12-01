# global 变量的范围
# 局部变量 全局变量

name = "月月"  # 全局变量，可以在函数内容或者全局访问


def func():
    # 函数内部申明的变量，局部变量，只能在函数内部使用
    global name # 不修改全局变量，只是获取打印，但是如果要发生修改，需要定义全局变量
    s = "小明"
    print(name)  # 打印的是全局变量
    name += '会谈吉他' # 这种写法会报错，不能随便在函数体重修改全局变量
    print(name)

def funw():
    name = "小月月"  # 局部变量和全局变量重名，优先使用局部变量，在函数内部修改，默认修改的是局部变量
    print(name)  # 打印的是局部变量


list01 = [1,2,3,4,56]  # 可变元素的全局变量，在函数内部可以直接访问,不用加global
def funb():
    name = "ruirui"
    print(name)
    print(list01)
    list01.append(8)
    print(list01)


def funv():
    global name
    print(name)
    name += "真帅"
    print(list01)


func()
print(name)

funb()
print(name)
funv()
print(name)