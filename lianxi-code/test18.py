# 文件
import os

path = os.getcwd()  # 获取当前文件所在路径 类似于 os.path.dirname(__file__)
print(path)

r = os.path.isfile(os.getcwd())
print(r)

r = os.path.isdir(path)
print(r)

# os.path
path = r'C:\Users\Win10\PycharmProjects\day1\lianxi\test18.py'
result = os.path.split(path)  # 得到一个元祖中存储了路径,文件名
print(result[1])  # 获取文件名
result = os.path.splitext(path) # 将文件名和扩展名分开
print(result[1])  # 获取扩展名

# 得到文件名
filename = path[path.rfind('\\') + 1:]
print(filename)
print(path.rfind('\\'))  # 输出的是查找到对应文件的第一个索引值

size = os.path.getsize(path)  # 获取文件的大小，返回字节
print(size)

res = os.path.join(os.getcwd(), 'file', 'a', 'test.py')  # 将文件=路径拼接
print(res)

# os.path 里面的函数‘
# os中的函数

dir = os.getcwd()
print(dir)
all = os.listdir(dir)  # 返回指定路径下的文件和文件夹，保存在列表中了
print(all)

# 创建文件夹
# 在当前目录下创建文件夹，无返回值'''

if not os.path.exists(r'C:\Users\Win10\PycharmProjects\day1\lianxi\test23.py'):
    os.mkdir(r'C:\Users\Win10\PycharmProjects\day1\lianxi\test23.py')
    os.rmdir(r'C:\Users\Win10\PycharmProjects\day1\lianxi\test23.py')


if not os.path.exists(r'C:\Users\Win10\PycharmProjects\day1\lianxi\test\aa.txt'):
    os.mkdir(r'C:\Users\Win10\PycharmProjects\day1\lianxi\test\aa.txt')


list1 = os.listdir(r'C:\Users\Win10\PycharmProjects\day1\lianxi\test')
print(list1)

#  文件复制
src_path = r'C:\Users\Win10\PycharmProjects\day1\lianxi'
target_path = r'C:\Users\Win10\PycharmProjects\day1‘

# 封装成函数
def copy(src_path, target_path):
    if os.path.isdir(src_path) and os.path.isdir(target_path):
        filelist1 = os.listdir(src_path) # 将源文件中的文件名分别读取出来

         # 读取文件中的内容
         for file in filelist1:  # 遍历每一个文件名
             path = os.path.join(src_path, file) # 连接每一个文件的绝对路径
             with open(path,'r') as rstream:  # 需要建立一个读取的管道流
                 container = rstream.read() # 从管道流中读取内容
             # 将源文件中的内容写入目标文件
             # 首先找到写入的路径
             path1 = os.path.join(target_path, file)  # 确定文件写入的路径
             with open(path1, 'w') as wstream: # 建立一个写入的管道流
                 wstream.write(container)  # 将container中的内容写入
         else:
             print("复制完毕")




