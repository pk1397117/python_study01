import time  # time 模块可以获取当前的时间

# time 模块的 time() 方法会获取当前时间的时间戳
# 时间戳是 1970-01-01 00:00:00 UTC 到现在的秒数
# 代码执行前时间
start = time.time()
x = 0
for i in range(1, 100000000):
    x += i

print(x)
# 代码执行后世间
end = time.time()
print("代码运行时间:", end - start)
