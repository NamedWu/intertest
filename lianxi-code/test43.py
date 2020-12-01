# 进程》线程〉协程
# 创建进程
'''
首先：导入创建进程的函数
from multiprocessing import Process
process = Process（target = 函数， name=进程的名字， agres(给函数传递的参数
process 对象
对象调用的方法
process.start() 启动进程并执行任务
process.run()  只执行了任务，没有启动进程
terminate（）终止



'''
from multiprocessing import Process
from time import sleep
import os

m = 1


def task1(s):
    global m
    while True:
        sleep(s)
        m += 1
        print("执行的是任务1。。。。。。。。。", m)


def task2(s):
    global m
    while True:
        sleep(s)
        m += 2
        print("执行的是任务2。。。。。。。。。。。", m)


number = 1
if __name__ == '__main__':
    # 子进程
    p1 = Process(target=task1, name='任务1', args=(1,))  # 这个是子进程
    p1.start()  # 这个是子进程
    print(p1.name)  # 这个是主进程，运行时先运行主进程
    p2 = Process(target=task2, name='任务2', args=(2,))  # 这个是子进程
    p2.start()  # 这个是子进程
    print(p2.name)  # 主进程
    print('************')  # 主进程

    while True:
        number += 1
        sleep(0.2)
        if number == 200:
            p1.terminate()
            p2.terminate()
            break
        else:
            print(number)
