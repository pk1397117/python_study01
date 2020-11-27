def calc(a, b, fn):
    return fn(a, b)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# 回调函数
x1 = calc(2, 3, add)
x2 = calc(2, 3, subtract)
x3 = calc(2, 3, multiply)
x4 = calc(2, 3, divide)
x5 = calc(2, 3, lambda x, y: x + y)
x6 = calc(2, 3, lambda x, y: x - y)
x7 = calc(2, 3, lambda x, y: x * y)
x8 = calc(2, 3, lambda x, y: x / y)
print(x1, x2, x3, x4)
print(x5, x6, x7, x8)
