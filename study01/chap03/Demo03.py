# 赋值运算符
a = 3 + 4
print(a)

# 链式赋值
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

# 参数赋值
a = 20
a += 30
print(a)
a -= 10
print(a)
a *= 2
print(a)
a /= 3
print(a)
a //= 2
print(a)
a %= 2
print(a)

# 解包赋值
a, b, c = 20, 30, 40
print(a, b, c)

print("---------交换两个变量的值---------")
print("交换之前：", a, b)
# 交换
a, b = b, a
print("交换之后：", a, b)
