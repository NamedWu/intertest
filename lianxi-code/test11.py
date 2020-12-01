# 开发：登录验证
import time

islogin = False  # 默认没有登录


def login():
    global islogin
    username = input("输入用户名")
    password = input("输入验证码")
    if username == "admin" and password == "123456":
        return True
    else:
        print("登陆失败，请重登录")
        return False


# 定义一个装饰器进行付款验证
def login_required(func):
    def wrapper(*args, **kwargs):
        global islogin
        print("付款开始")
        # 验证用户是否登录
        if islogin:
            func(*args, **kwargs)
        else:
            # 跳转页面
            print("用户没有登陆，不能付款")
            islogin = login()
            print("登录result", islogin)
            func(*args, **kwargs)
    return wrapper


@login_required
def pay(money):
    print("正在付款。。。付款金额是：{}元".format(money))
    print("付款中。。。")
    time.sleep(3)
    print("付款成功。。。。")


# 调用付款
pay(100)

pay(200)