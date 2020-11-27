import time


def cal_time(fn):
    start = time.time()
    fn()
    end = time.time()
    print("执行时间:", end - start)


def demo():
    x = 0
    for i in range(1, 100000000):
        x += i
    print(x)


def foo():
    print("hello")
    time.sleep(3)
    print("world")


cal_time(demo)
cal_time(foo)
