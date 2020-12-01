# 列表推导式列表 字典推导式 集合推导式
# 旧的列表---新的列表
# 1、列表推导式
# 格式：[表达式 for 变量 in 旧的列表] 或者[表达式 for 变量 in 旧的列表 if 条件]

# 过滤掉长度小于或者等于3的人名
names = ['xiaomei', 'xiax', 'bob']
result = [name for name in names if len(name) > 3]  # 第一个name 是符合条件的name 存放值，第二个name是从names中遍历的值，
print(result)

# 将获取的名字首字母大写
names = ['xiaomei', 'xiax', 'bob']
result = [name.capitalize() for name in names if len(name) > 3]  # 第一个name 是符合条件的name 存放值，第二个name是从names中遍历的值，
print(result)

# 将1-100之间能被3整除的数组成一个新的列表
num = [num2 for num2 in range(1, 101) if num2 % 3 == 0 and num2 % 5 == 0]
print(num)


# 求出0-10 之间的偶数和0-10之间的奇数组成的元祖
def func():
    newlist = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i % 2 == 0:
                if j % 2 != 0:
                    newlist.append((i, j))
    return newlist


X = func()
print(X)


# 使用列表推导式怎么写
newlist1 = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newlist1)


# 练习 list1 = [(1,2,3),(4,5,6),(7,8,9)]  ---输出list2 = [(3,6,9),(2,5,8),(1,3,7)]
list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 3, 5)]
newlist2 = [i[-1] for i in list1]
print(newlist2)

dict1 = {'name': 'tom', 'salary': 3000}
dict2 = {'name': 'ptom', 'salary': 4000}
dict3 = {'name': 'itom', 'salary': 5000}
dict4 = {'name': 'utom', 'salary': 6000}
list2 = [dict1, dict2, dict3, dict4]
# if 薪资大于5000，加200，if薪资小于=5000 加500
newlist3 = [i['salary'] + 200 if i['salary'] >= 5000 else i['salary'] + 500 for i in list2]
print(newlist3)

# 集合推导式 {}类似与列表推导式，在列表推导式的基础上添加了一个去重复项

list = [1, 2, 4, 5, 6, 6, 7, 9]

set1 = {x-1 for x in list if x>1}
print(set1)    # 输出的结果去除了重复项


# 字典推导式
dict1 = {'name': 'xiaohong', 'sex': 'woman', 'age': 12, 'height': 12}
print(dict1.items())  # 输出每一个key:value
newlist1 = {value: key for key, value in dict1.items()}
print(newlist1)  # 输出的结果能够去重 {'xiaohong': 'name', 'woman': 'sex', 12: 'height'}
