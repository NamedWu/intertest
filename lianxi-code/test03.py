import random


# 定义一个函数，产生一个验证码
def generate_checkcode(n):
    s = '0987654321qwertyuiopasdfghjklzxxcvbnmQWERTYUIOPADSFGHJKLZCXVBNM'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(s)-1)
        code += s[ran]
    return code


def login():
    username = input("请输入用户名")
    password = input("请输入密码")
    # 得到一个验证码
    code = generate_checkcode(4)
    print(code)
    code1 = input("请输入一个验证码")
    if code.lower() == code1.lower():
        if username == '李佳琪' and password =="123456":
            print("用户登录成功")
        else:
            print("用户名或密码错误")
    else:
        print("验证码错误")


login()