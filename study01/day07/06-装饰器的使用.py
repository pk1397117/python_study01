import time


def cal_time(fn):
    print("我是外部函数，我被调用了")
    print("fn = {}".format(fn))

    def inner():
        start = time.time()
        fn()
        end = time.time()
        print("代码耗时:", end - start)
    return inner


# 第一件事:调用cal_time
# 第二件事:把被装饰的函数传递给fn
# 第三件事:将装饰器函数的返回值赋值给被装饰函数的标识符,没有返回值就赋值为None
@cal_time
def demo():
    x = 0
    for i in range(1, 100000000):
        x += i
    print(x)


# @cal_time
# def foo():
#     print("hello")
#     time.sleep(3)
#     print("world")

# 此时的demo函数已经不是原来的demo函数了
print("装饰后的demo = {}".format(demo))
# 此时 demo 指向 inner函数
demo()





