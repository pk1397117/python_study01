# Python里的数据类型
# 整型(int) 浮点型(float) 复数(complex)
# 字符串 布尔 列表 元组 字典 集合
# Python里数值默认是十进制
a = 98  # 十进制(decimal)
b = 0b100101101  # 二进制(binary)，0b开头
c = 0o30  # 八进制(octal)，0o开头
d = 0x30  # 十六进制(hexadecimal)，0x开头
# 打印结果为十进制,sep(separator) 分隔符
print(a, b, c, d, sep=', ')
e = int("100101101", 2)
print(e)
o = oct(int("100101101", 2))

print(int("0xF0384E", 16))
print(int("F0", 16), int("38", 16), int("4E", 16), sep='')
print(int("FF", 16), int("EE", 16), int("33", 16), sep='')

i = 0
j = 0
while i <= 10000:
    if (i % 3 == 0 or i % 7 == 0) and i % 21 != 0:
        print(i)
    i += 1



