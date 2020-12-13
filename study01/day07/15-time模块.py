import time
import datetime as dt

# 时间戳
print(time.time())  # 获取 1970-01-01 00:00:00 UTC 到现在时间的秒数
print(time.strftime("%Y-%m-%d %H:%M:%S", (2020, 1, 1, 1, 1, 1, 1, 1, 1)))  # 按照指定格式输出时间
print(time.asctime(time.struct_time((2020, 1, 1, 1, 1, 1, 1, 1, 1))))
print(time.ctime(time.time() + 3.5))

print("hello")
# time.sleep(5)  # 线程暂停指定秒数
print("world")
print(dt.datetime(1998, 4, 8, 12, 12, 12).strftime("%Y-%m-%d %H:%M:%S"))
