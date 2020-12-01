# 嵌套函数
# 特点
# 可以访问外部函数变量
# 内部函数可以修改外部函数的可变类型变量比如：list01
# 内部函数修改全局的不可变变量时 ，需要在内部函数声明global 变量名
# 内部函数修改外部函数的不可变变量时，需要在内部函数中声明：nonlocal 变量名
# locals 查看本地变量有哪些，globals 查看全局变量有哪些，里面会有系统变量

c = 100


def func():
    # 声明变量
    n = 100  # 局部变量
    list01 = [1, 3, 5, 6]

    # 声明内部函数
    def inner_func():
        global c
        nonlocal n  # 相当于全局变量的使用，只是这个是函数内部调用变量
        # 将列表所有元素+5
        for index, i in enumerate(list01):
            list01[index] = i + n
        list01.sort()

        # 修改n 变量
        n += 101
        c += 101  # 内部函数修改外部全局变量时需要在内部函数声明变量 global 变量名

    # 需要调用内部函数
    inner_func()
    # 使用locals内置函数进行查看。查看本函数声明的内容有哪些,local 是用一个字典存储，
    print(locals())
    print(list01)
    print(n)


func()
print(locals(), globals())