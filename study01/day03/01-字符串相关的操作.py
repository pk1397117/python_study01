# 修改大小写

# 让第一个单词首字符大写
print("hello world.good morning\nyes-no".capitalize())

# upper 全大写
print("hello".upper())

# lower 全小写
print("WORLD".lower())  # 面向对象里，我们称之为方法

# title 每个单词的首字母大写(其余字母都强制小写)
print("good morNing".title())

# while True:
#     content = input("请输入内容，输入exit退出")
#     print("您输入的内容:", content)
#     if content.lower() == "exit":
#         break


# ljust(width,fillchar)
# width 长度  fillchar 填充字符，默认是空格
# 让字符串以指定长度显示，如果长队不够默认在右边使用空格补齐
print("Monday".ljust(10, "+"))  # 右侧补齐
print("Tuesday".rjust(10, "-"))  # 左侧补齐
print("Wednesday".center(11, "+"))  # 居中

# strip 默认删除空格，也可以自定义字符strip(str),str里的任意字符都会被删除
print("     apple          ".lstrip())  # 删除前导空格
print("     pear          ".rstrip())  # 删除结尾空格
print("     banana          ".strip())  # 删除前导和结尾空格

# 以某种固定格式显示的字符串，我们可以将它切割成为一个列表
x = "zhangsan+lisi+wangwu+jack+tony+henry+chris"
names = x.split("+")
print(names)
# 将列表转换为成为字符串
fruits = ["apple", "pear", "peach", "banana", "orange", "grape"]

# 以给定字符串连接任意数量的字符串生成一个新的字符串
# join(Iterable[str])
print("-".join(fruits))
print("*".join("hello"))

# 字符串的运算符
# 字符串和字符串之间可以使用加法运算，作用是拼接两个字符串
# 字符串和数字之间可以使用乘法运算，目的是将指定的字符串重复多次
# 字符串和数字之间做 == 运算，结果为False ，做 != 运算，结果是True
# 字符串之间做比较运算，会逐个比较字符串的编码值
# 不支持其它运算符


