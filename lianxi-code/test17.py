# 文件操作
'''
文件上传

系统函数：
open（file,mode,buffering,encoding）
读:
open(path/filename,'rt') 如果文件和pycharm在同一级目录用文件名可以读取，否则需要加上路径，返回值是一个流
stream。read（） ----读取管道中的内容
stream.readable()
readline
readlines
如果文件名或者路径有误 会报错，文件找不到
'''
# 读文件
# 读取默认是读取文本文件
stream = open(r'C:\Users\Win10\Downloads\qq.txt')
result = stream.readable()  # 判断文件是否可读

if result:
    container = stream.read()
    print(stream.read())
else:
    print("内容不可以读取")

line = stream.readline()  # 表示只读取一行内容，如果内容已被读取就会报错
while True:
    line = stream.readline()
    print(line)
    if not line:
        break

lines = stream.readlines()  # 表示将文件内容全部读取，每次读取一行后面都会加上个换行符，存到一个列表中


# 读取图片，需要转换成二进制
stream = open(r'C:\Users\Win10\Downloads\qq.jpg', 'rb')
container = stream.read()
print(container)



# 写文件
# 每次都会将原来的内容清空，在写入新东西

stream = open(r'C:\Users\Win10\Downloads\qq.txt', 'w')
s = '''
你好！
欢迎你
'''
result = stream.write(s)
print(result)
stream.write("wag")
stream.close() # 资源释放，不可以再继续往文件中写入东西

stream.write("ss") # 这个会报错，因为管道已经关闭了，不可以再继续写入东西了

