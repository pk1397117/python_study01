import datetime as dt
import time

# 以一个下划线 _ 开始
# 以两个下划线 __ 开始
# 以两个下划线开始，以以两个下划线结束 __x__

# 涉及到四个类 date/time/datetime/timedelta
print(dt.date.today())  # 获取当天日期
print(dt.datetime.now())  # 获取当天日期时间
print(dt.date(2020, 1, 1))  # 创建一个日期
print(dt.time(18, 23, 45))  # 创建一个时间
print(dt.datetime(2020, 1, 1, 6, 30, 25))  # 创建一个日期时间
print(dt.datetime.now() + dt.timedelta(3, hours=5))  # 计算三天五小时以后的日期时间
print(dt.date.today() + dt.timedelta(3))  # 计算三天后的日期
print(dt.datetime.now().weekday())  # 获取今天星期几；[0,6] 分别表示星期一到星期天
print(dt.datetime.now().isoweekday())  # 获取今天星期几；[1,7] 分别表示星期一到星期天
print(dt.date(2020, 12, 7).weekday())  # 获取指定日期星期几

# 内置类
# list tuple int str
