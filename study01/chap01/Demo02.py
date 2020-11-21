# 转义字符
# 换行符
print('hello\nworld')

# 制表符(占四个字符)
print('hello\tworld')
print('helloooo\tworld')

# 回车
print("hello\rworld")

# 退格
print("hello\bworld")

print("http:\\\\www.baidu.com")
print("老师说:\"大家好\"")

# 原字符，不希望字符串中的转义字符起作用就使用元字符，就是在字符串之前加上r或R
print(r"hello\nworld")
# 最后一个字符不能是反斜杠但是可以是两个反斜杠
print(r"hello\nworld\\")


