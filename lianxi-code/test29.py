# 多重继承
# 搜索方式：从左到右，广度优先

class P1:
    def foo(self):
        print("P1中的foo")

    def bar(self):
        print("P1中的bar")


class P2:
    def foo(self):
        print("P2中的foo")

    def bar(self):
        print("P2中的bar")


class C1(P1):
    def foo(self):
        print("C1中的foo")


class C2(P2):
    def bar(self):
        print("C2中的bar")


class D1(C1, C2, P1, P2):
    pass


d = D1()
print(D1.__mro__)  # 这个函数能看出运行时的查找顺序，首先查找的是 D1 ，其次是C1，再是C2，P1，P2，object
d.foo()  # 运行的结果是C1中的foo 的返回结果，
