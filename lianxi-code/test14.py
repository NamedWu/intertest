# 匿名函数
from functools import reduce

list1 = [3, 4, 5, 4, 6, 7, 0]
m = max(list1)
print(m)

list2 = [{'a': 12, 'b': 13}, {'a': 122, 'b': 13}, {'a': 17, 'b': 3}, {'a': 10, 'b': 13}]
# 取出列表中a 元素的最大值，函数中的数值不能直接用数学判断，需要取出其中不放呢元素进行比较
# max(参数，函数)
n = max(list2, key=lambda x: x["a"])  # 当比较的类型不能用>,<进行比较时，就会采用key
print(n)

# map（函数，参数）后的参数作为函数中的参数
result = map(lambda x: x + 2, list1)
print(list(result))

func = lambda y: y if y % 2 == 0 else y + 1

list3 = [1, 2, 3, 4, 5]
# 队列表中的奇数加1 操作
result1 = map(lambda x: x if x % 2 == 0 else x+1, list3)
print(list(result1))

# reduce() 队列表中的元素依次进行加减乘除运算
tuple1 = (12,)
result2 = reduce(lambda x, y: x / y, tuple1, 10)  # initial 作为函数的第一个参数传入
print(result2)

# filter (函数，参数)，判断迭代器中的值是否符合函数要求，如果符合，返回迭代器中的值，如果不符合不返回
result3 = filter(lambda x: x % 2 == 0, list1)
print(list(result3))


# min（参数，key = 函数）函数标明参数中的值按照哪个字段的值来进行比较
result4 = min(list2, key=lambda x: x["b"])
print(result4)

# sorted（参数，函数） 返回一个新列表，函数可以自定义排序规则如果不定义，表示按照升序排列,reverse=True 表示降序
result5 = sorted(list2, key=lambda x: x["a"], reverse=True)
print(list(result5))



