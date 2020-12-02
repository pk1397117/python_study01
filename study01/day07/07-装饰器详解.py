import time


def cal_time(fn):
    print("我是外部函数，我被调用了")
    print("fn = {}".format(fn))

    def inner(n, *args, **kwargs):
        start = time.time()
        s = fn(n)
        end = time.time()
        # print("代码耗时:", end - start)
        return s, end - start

    return inner


@cal_time
def demo(n):
    x = 0
    for i in range(1, n):
        x += i
    # print(x)
    return x


m = demo(100000000, "good", y="hello")
print("m的值是", m)



