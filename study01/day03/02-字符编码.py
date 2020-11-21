# ASCII --> Latin1 --> Unicode编码
# 字符 --> 数字编码存在一个对应的关系

# 使用内置函数 chr 和 ord 能够查看数字和字符的对应关系
# ord 获取单个字符对应的编码；chr 根据 编码获取对应的字符
print(ord('a'))  # 字符对应的编码是97
print(chr(65))  # 编码对应的字符是A

print(ord("你"))
print(hex(20320))

print(hex(65))
print(int(0xFFFF))
print(ord("ℤ"))

# GBK BIG5 UFT-8

# 使用字符串的encode方法，可以将字符串转换成为指定编码集的结果
print("你".encode("utf8"))
# 如果有一个编码集的结果，想把它转换成为对应的字符，则使用decode
x = b'\xe4\xbd\xa0'
print(x.decode("utf8"))
print(type(x))