x = "abcdefghijklmn"

# 获取字符串的长度
print(len(x))

# 查找内容相关的方法 find/index/rfind/rindex
# 如果子串存在则返回子串第一个字符在原字符串的索引
print(x.find("e"))  # 4
print(x.find("efg"))  # 4
print(x.index("e"))  # 4
print(x.index("efg"))  # 4
print(x.find("w"))  # 不存在，返回-1
# print(x.index("w"))  # 不存在，报错

print(x.find("l", 4, 9))  # find(sub, start, end)
# x.rfind()、x.rindex().匹配子串最高索引
print(x.startswith("ab"))  # 以...开头
print(x.endswith("mn"))  # 以...结尾
print(x.isalpha())  # 只含字母并且长度大于等于一
print(x.isdigit())  # 只含数字并且长度大于等于一(浮点数不行)
# alnum 判断是否由数字或字母组成
print("abc".isalnum())  # True
print("123".isalnum())  # True
print("abc123".isalnum())  # True
print("abc123/*-".isalnum())  # False

# isspace 判断是否只由空格符组成
print("      ".isspace())  # True
print("          s".isspace())  # False

# count,计算子串在原串里出现的次数
print("12314156789".count("1"))

# replace方法，用来替换字符串
word = "hello"
m = word.replace("l", "x")  # 将字符串里的l替换为x
print(word)  # hello 字符串是不可变数据类型！！！
print(m)  # 原字符串不会改变，replace方法则是生成了一个新的字符串

