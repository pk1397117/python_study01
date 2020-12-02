# os(operating system) 操作系统
# os 模块里提供的方法就是用来调用操作系统里的方法
import os

# os.name ==> 获取操作系统的名字 windows系列 ==> nt / 非windows ==> posix
print(os.name)  # nt
print(os.sep)  # 路径的分隔符 windows \ ;非windows /

# abspath ==> 获取文件的绝对路径
print(os.path.abspath("01-高阶函数.py"))

# isdir 判断是否为文件夹
print(os.path.isdir("02-函数的嵌套.py"))  # False

# isfile 判断是否为文件
print(os.path.isfile("02-函数的嵌套.py"))  # True

# 判断文件/文件夹是否存在
print(os.path.exists("../day07"))  # True

#
file_name = "2020.2.21.demo.py"
print(file_name.rpartition(".")[-1])
os.path.splitext("2020.2.21.demo.py")

