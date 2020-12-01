'''import random





def generate_random(num):
    for i in range(num):
        ran = random.randint()
        print(ran)

generate_random(12)


''''定义一个登录函数，参数是，username，password，函数体：判断参数传过来的username，password是否正确，如果正确则'''


# fun01
def login(username, password):
    for i in range(3):
        if username == 'admin' and password == '123456':
            print("登录成功")
            break
        else:
            print("用户名密码错误，请重新输入")
            username == input("请输入用户名")
            password == input("请输入密码")
    else:
        print("输入次数过多，请稍后再试")


username = input("请输入用户名")
password = input("请输入密码")
login(username, password)


# 定义一个最大值函数
# fun02
# 随意添加几个数，放入列表中


def max01(list2):
    num = list2[0]
    for i in range(len(list2) - 1):
        if list2[i] >= num:
            num = list2[i]
        else:
            pass
    print(num)


list1 = [1, 2, 3]
max01(list1)


# 封装一个方法，取出元素下标
def enumerate(value):
    index = 0
    for i in value:
        t1 = (index, i)
        list1.append(t1)
        index += 1
    print(list1)


tuple1 = (1, 2, 34, 5)
enumerate(tuple1)


# 可变参数,name累加的和是sum，注意，如果有可变参数，先放固定参数，在放可变参数，几可变参数必须放在固定参数之后
def add(name, *args):
    sum01 = 0
    if len(args) > 0:
        for i in args:
            sum01 += i
        print("%s的分数总和为：%d" % (name, sum01))
    else:
        print("未输入分数，无法求和")


add("xiaoming", 12, 3)


# 可变参数，关键字参数,关键字参数可以传，如果传入，就会覆盖原来的默认值，可以有多个关键字
# 如果有多个关键字，想要给其中某个关键字复制，可以使用关键字来赋值。如果不适用关键字，默认给第一个关键字参数赋值
# 关键字参数，key = value
def sum01(a, b1=10):
    result = a + b1
    print(result)


sum01(1)
sum01(4, 7)

# 打印每位同学的年龄和姓名
student = {'001': ("蔡徐坤", 19), '002': ("王源", 19), '003': ('王俊凯', 18)}


def info_boy(name1, **kwarges):
    if isinstance(kwarges, dict):  # 判断元素类型
        values = kwarges.values()
        for name, age in values:
            print('%s喜欢的明星：%s年龄是：%d' % (name1, name, age))


info_boy("xiaohong", **student)


# 可变关键字参数，**kwargs，说明外界传值时只能是键值对的形式
def func(**kwargs):
    print(kwargs)


# 在调用的时候需要使用关键字赋值
func(a=1, b=2)
# 结果默认转换成字典保存，{a:1,b：2} 将关键字装包成一个字典
dict1 = {'001': 'xiaobai', '002': 'xiaohogn', '003': 'xiaodu'}
func(**dict1)  # 首先会将字典进行拆包，拆成键值对的形式，func里面的参数都是关键字参数，在调用函数时，会装包成一个字典


def fun1(a, *args, **kwargs):  # *args传入的是一个元祖做参数，**kwargs 传入的是一个字典做参数
    print(a, args, kwargs)


a = 1
b = [1, 2, 3]
c = {'name': 'xiaohong', 'sex': 'nv'}
fun1(a, b, **c)  # 输出结果是 1 ([1, 2, 3],) {'name': 'xiaohong', 'sex': 'nv'}
fun1(a, *b, **c)  # 输出结果是：1 (1, 2, 3) {'name': 'xiaohong', 'sex': 'nv'}


# 数据库基础命令
'''
persons

数据库基础知识：
1、插
insert into persons（name,age），values(name1,age1)
1）插入1列
alert table persons 
add sex int
2）插入多条
方法一
insert into persons(name,age)
select'wang',12 union all
select 'li',12
方法二
insert into persons（name，age）,
values(name1,age1)
(name2,age2)
3）复制demo至demo1
insert into demo1(name,age)
select name,age
from demo

删
1）删除一行
delete from person
where name = 'wang'
2）删除一列
alert table person
drop column age
3）删表
delete from table
4）清空
truncate table person

改
1）改一列数
update person 
set name = 'zhao'
where name = 'li'
2）改多列数
update person
set name = 'deng',
age = 13
where height = 90

查
1）查某一行
select *
from person
where name = 'wang'
2）查某行某列
select name
from person

列出不同（distinct）的值
select distinct name
from person

指定的列对结果集进行排序（DESC）
select name, height
from person 
order by age DESC,height

LIKE 操作符用于在 WHERE 子句中搜索列中的指定模式
1）查找N开头的城市名称
select name
from person
where name like N%

通配符：
% 指代一个或者多个字符
_ 指代一个字符
[charlist]	包含列表内的一个或者多个字符
[^charlist]/[!charlist] 不包含列表内的所有字符

IN
1）查找包含城市名为北京或者newyork 城市信息
select *
from person
where city in ( 北京 ,newyork)

BETWEEN ... AND 会选取介于两个值之间的数据范围
1）"Adams"（包括）和 "Carter"（不包括）之间的人信息
select * 
from person
where name between Admas and carter

使用关键词 JOIN 来从两个表中获取数据-----join连接两个表格时需要标明是哪个表格中的字段，
1）join 连接两个表格
select person.name ，person.age, orderinfo.number,orderinfo.id
from person
join orderinfo
on person.id = orderinfo.id
2）inner join 和join功能相同
3) left join 左连接，右边的表格作为主表格，如果右边表格中没有的数据，不会出现在表格中
4) right join 右链接，右边表格中没有的数据，不会出现在表格中
5) full join 全连接，左右两边表格中的数据全部都会出现在表格中


union 用于合并两个或多个 SELECT 语句的结果集
1)union 从表格1中选取数据+从表格2 中选择数据，结合起来放到一列，去除重复的名字
2)union all 从两个表格中去除数据，但是不会去除重复的内容
select name from person
union 
select name from demo

SELECT INTO 语句从一个表中选取数据，然后把数据插入另一个表中
1)select into from  从表格person中取出name，age数据存放到新表格personinfo中
select name ，age
into personinfo
from person
2)insert into select from
insert into demo1 
select name，age
from person
3）select into from 选择两个表格中的部分数据放入一个新的表格中
select person.name,person.age,orderinfo.id
into person_backen
from person
join orderinfo
on person.id = orderinfo.id

创建数据库
Create database
Create database students

创建数据库中的表
Create table
Create table students_info

NOT NULL 约束强制字段始终包含值。这意味着，如果不向字段添加值，就无法插入新记录或者更新记录
UNIQUE 约束唯一标识数据库表中的每条记录
PRIMARY KEY 约束唯一标识数据库表中的每条记录。主键必须包含唯一的值
一个表中的 FOREIGN KEY 指向另一个表中的 PRIMARY KEY
CHECK 约束用于限制列中的值的范围
DEFAULT 约束用于向列中插入默认值

创建索引
CREATE INDEX
'''

# linux 基础命令
''''
显示日期和时间的命令
显示日历命令
简单好用的计算器
热键命令不全或文件补齐
终端目前程序‘
输入结束限度昂与输入exit
在线求助
数据同步写入磁盘’
关机命令
重启命令
改变文件所属用户组
改变文件所有者
改变文件的属性‘改变权限
切换目录
显示目前所在的目录
新建新的目录
删除空的目录
查看文件与目录
复制文件或目录
移除文件或目录
移动文件或目录
直接查看文件内容
反向列式
取出前面几行
取出后面几行



'''