# 语法错误 在编写代码时候会有红线提示
# 异常 语法没有错误，但是运行时候会报错
# 异常处理
"""
try :
 可能出现异常的代码
except：
    如果有异常执行的代码
finally：
    不论是否存在异常，都会执行的代码

情况1
    try ：
     有可能会产生多个异常
     except 异常类型1：
         print（）
     except 异常类型2：
        print()
     except 异常类型3：
        pass
    except Exception:
       pass


情况2：
    try ：
     有可能会产生多个异常
     except 异常类型1：
         print（）
     except 异常类型2：
        print()
     except 异常类型3：
        pass
    except Exception as err:
       print（err）其中二人是错误原因

情况3：
   try:
       可能出现异常的代码执行
   except:
       有异常代码执行
   else:
       没有异常发生时，代码执行
注意：如果使用else，则在try中不能使用return




情况4
try：
    pass
except：
    pass
finally：#不论程序是否报错，都会执行的代码，例如读取文件错左后如果报错还是要江南文件关闭，所以需要这个finally
    pass

异常总的是继承老父类’
baseexception
exception
其中异常类都是从exception中延伸的。如果直接写exception，包含了所有的报错类型

如果是多个except，异常类新顺序需要注意，最大的Exception要放在最下面
"""


def func():
    try:  # try 不能单独使用，需要结合except
        num1 = int(input("请输入一个数字"))
        num2 = int(input("请输入第二个数字"))
        # 加法操作
        per = input("请输入加减乘除")
        if per == "-":
            result = num1 - num2
        elif per == "/":
            result = num1 / num2
        elif per == "*":
            result = num1 * num2
        else:
            sum = num1 + num2
        print("两个数的和是", sum)
        return 10
    except ZeroDivisionError:
        print("除数不能为0")
    except ValueError:
        print("请输入数字")
    except Exception as err:  # 输入exception中包含了所有的出错类型
        print("出错了", err)
    else:
        print("没有异常时执行的代码")


func()
print("异常代码之外代码执行结果")

'''
抛出异常
raise

系统往外扔
手动往外扔（比如贵规定用户名必须>6位，如果输入的用户名<6位，系统不会报错，此时需要手动输入报错内容）

'''


def register():
    username = input("请输入用户名")
    if len(username) < 6:
        raise Exception("用户名长度必须大于6位")
    else:
        print("用户名为{}".format(username))


try:
    register()
except Exception as err:
    print(err)
    print("注册失败")
else:
    print("注册成功")
