# 函数返回值：return，将函数运算的结果，通过关键字返回来
# return 可以是一个参数，也可以是多个参数，如果是多个参数，底层会将多个参数放入一个元祖中将元祖作为一个整体返回
# 接收的时候也可以是多个：return ’hello‘, 'world' x,y = ('hello','world')
# 登录成功，加入购物车成功
islogin = False  # 用于判断用户是否登录变量，默认没有登录，


def add_shopppingcart(goodsName):
    global islogin
    if islogin:
        if goodsName:
            print("成功将{}加入购物车".format(goodsName))
        else:
            print("没有添加商品")
    else:
        print("用户没有登陆")
        answer = input("是否重新登录？y/n")
        if answer == 'y':
            username = input("请输入用户名")
            password = input("请输入密码")
            islogin = login(username, password)
        else:
            print("很遗憾添加失败")
            

def login(username, password):
    if username == "李佳奇" and password == "123456":
        print("登陆成功")
        return True
    else:
        print("用户名密码错误，请重新输入用户名密码")
        return False


username = input("请输入用户名")
password = input("请输入密码")
islogin = login(username, password)

# 调用函数，添加商品到购物车
add_shopppingcart("口红")
