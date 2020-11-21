a = 13
b = 20

# 方法一: 使用第三个变量
# c = a
# a = b
# b = c

# 方法二: 使用加减法.只适用于数字
# a = a+b
# b = a-b
# a = a-b

# 方法三: 使用异或运算.适用于整数
# a = a ^ b
# b = a ^ b
# a = a ^ b

# 方法四: 使用Python特有(解包赋值)
a, b = b, a

print(a)  # 20
print(b)  # 13



