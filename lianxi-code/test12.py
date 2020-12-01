# 函数
# local 局部变量
# enclosing 嵌套
# gloabl 全局
# bulit-in 内置

# 函数变量搜索，首先是local，enclosing,global ，bulit_in
def func():
    a = 10

    def inner_func():
        a = 1
        print(a)
        print(max)

    inner_func()
    return a


q = func()
print(q)
