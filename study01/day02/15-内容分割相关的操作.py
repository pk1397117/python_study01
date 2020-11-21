# split splitlines partition rpartition
x = "zhangsan-lisi-wangwu-jerry-henry-merry-jack-tony"
# ['zhangsan','lisi','wangwu','jerry','henry','merry','jack','tony']
y = x.split("-")  # split方法，将字符串切割成一个列表
print(x)
print(y)  # 切割后的结果就是一个列表

z = x.rsplit("-")
print(z)

print(x.split("-", 2))  # 从左往右分割
print(x.rsplit("-", 2))  # 从右往左分割

# partition 指定一个字符串作为分隔符，分为三部分
# 前面 分隔符 后面
print("abcdefXmpXqrst".partition("X"))  # ('abcdef', 'X', 'mpqrst') 从左往右匹配第一个分隔符然后分割成三部分
print("abcdefXmpXqrst".rpartition("X"))  # ('abcdef', 'X', 'mpqrst') 从右往左匹配第一个分隔符然后分割成三部分

# 获取文件名和后缀名
file = "2020.4.abc.mp4".rpartition(".")
file_name = file[0]
file_suffix = file[2]
print(file_name, file_suffix)

