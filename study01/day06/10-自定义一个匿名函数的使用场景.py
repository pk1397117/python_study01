def calc(func, *args):
    if args == ():
        return func
    return args[-1](func, args[0])


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# 回调函数
x1 = calc(add(1, 2))
print(x1)

x2 = calc(subtract(1, 2))
print(x2)

x3 = calc(multiply(1, 2))
print(x3)

x4 = calc(divide(1, 2))
print(x4)

x5 = calc(2, 3, lambda x, y: x + y)
x6 = calc(2, 3, lambda x, y: x - y)
x7 = calc(2, 3, lambda x, y: x * y)
x8 = calc(2, 3, lambda x, y: x / y)
print(x5, x6, x7, x8)
