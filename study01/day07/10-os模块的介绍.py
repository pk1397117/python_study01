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

# 拆分文件名和后缀
file_name = "2020.2.21.demo.py"
print(file_name.rpartition("."))
print(os.path.splitext(file_name))

# 获取当前工作目录
print(os.getcwd())

# os里其它方法介绍
# os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录
# os.chdir("PATH")  # 改变当前脚本的工作目录，相当于shell下的cd命令
# os.rename("old","new")  # 文件重命名
# os.remove("file")  # 删除文件
# os.rmdir("dir")  # 删除空文件夹
# os.removedirs("dir")  # 删除所有空的叶子目录
# os.mkdir()  # 创建文件夹
# os.chdir()  # 切换工作目录
# os.listdir()  # 列出指定目录里所有文件和文件夹
# os.name  # nt -> windows;posix -> Linux/Unix 或者MacOS
# os.environ  # 获取到环境配制
# os.environ.get("PATH")  # 获取指定的环境配置

