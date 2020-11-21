def test1():
    print("test1开始了")
    print("test1结束了")


def test2():
    print("test2开始了")
    test1()
    print("test2结束了")


test2()


# 定义函数求n~m之间所有整数之和
def add(n: int, m: int):
    return sum([i for i in range(n, m + 1)])


print(add(1, 5))


# 求一个数的阶乘
def factorial(n: int):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product


print(factorial(5))


# 计算m以内正整数阶乘的和
def fac_sum(m: int):
    return sum([factorial(i) for i in range(1, m+1)])


print(fac_sum(5))
