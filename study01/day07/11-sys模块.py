# 系统相关的功能
import sys


print("hello world")
print("你好世界")
print("you'd better not do the thing like that")
# ['F:\\python_study01\\study01\\day07', 'F:\\python_study01',
#  'F:\\Program Files\\JetBrains\\PyCharm 2020.2.3\\plugins\\python\\helpers\\pycharm_display',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\DLLs',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\lib',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39',
#  'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages',
#  'F:\\Program Files\\JetBrains\\PyCharm 2020.2.3\\plugins\\python\\helpers\\pycharm_matplotlib_backend']
print(sys.path)  # 结果是一个列表，表示查找模块的路径；以上任意路径的里的模块的py文件都能在 import 时找到
# sys.exit(100)  # 程序退出，和内置函数 exit 功能一致
# sys.stdin  # 可以像 input 一样 接受用户的输入，和 input 相关
# sys.stdout  # 标准输出；修改 sys.stdout 可以改变默认输出位置
# sys.stderr  #  修改 sys.stderr 可以改变错误输出的默认位置
# sys.stdout 和 sys.stderr 默认都是在控制台输出
