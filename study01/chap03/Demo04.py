# 比较运算符,结果为bool类型
a, b = 10, 20
print(a > b)  # False
print(a < b)  # True
print(a <= b)  # True
print(a >= b)  # False
print(a == b)  # False,比较的是值
print(a != b)  # True
print("------------")

a = 10
b = 10
print(a == b)  # True 说明，a与b的value值相等
print(a is b)  # True 说明，a与b的id标识相等
print(a is not b)  # False id相等所以为False
print("------------")

list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list1 == list2)  # True value相同
print(list1 is list2)  # False id不同
print(list1 is not list2)  # True id不同所以为True


