# 文件操作
# 文件
'''
open()
读：rb , r
写：wb, w
mode
path（非同级目录需要写绝对路径） ,filename(同级目录直接写文件名)
stream = open（file，name）
stream。read（）
stream。write（）
stream.close（）
with open(file,mode)as stream:
    操作代码




   os模块
   os.path：
   os。getcwd
   os.path。isfile
   os.path.isdir
   os.path.split(path)
   os.path.splitext(path)
   os.path.join
   os.path.getsize()




'''

# 怎么持久化保存：文件
# list 元祖，字典----内容
# 用户注册
def register():
    username = input('输入用户名')
    password = input('输入密码')
    repassword = input('请确认密码')

    if password == repassword:
        # 保存信息
        with open(r'C:\Users\Win10\Desktop\pycharm\用户.txt','a') as wstream:
            wstream.write('{} {}\n'.format(username, password))
        print("用户注册成功！")
    else:
        print("两次输入密码不一致")


def login():
    username = input("请输入用户名")
    password = input("请输入密码")

    if username and password:
        with open(r'C:\Users\Win10\Desktop\pycharm\用户.txt', 'r') as rstream:
            while True:
                user = rstream.readline() # 读取每行用户信息
                if not user:
                    print('用户名或信息有误')
                    break

                input_user = '{} {}\n'.format(username, password)
                if user == input_user:
                    print("登录成功")
                    break

def show_books():
    print('-------图书馆里面的图书：---------')
    with open(r'C:\Users\Win10\Desktop\pycharm\文本图书.txt') as rstream:
        books = rstream.readlines()
        for book in books:
            print(book, end='')

show_books()


# 问题：编写借书还书函数