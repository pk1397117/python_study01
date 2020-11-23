# 函数的三要素: 函数名、参数、函数体
# 在有一些编程语言里，允许函数重名。在Python里不允许函数重名
# 如果函数重名了，后一个函数会覆盖前一个函数，如java里的重载

# def test(a, b):
#     print("hello,a={},b={}".format(a, b))

# test = 对应的是一个函数
def test(x):
    print("good,x={}".format(x))


# test = 5  # 对函数名进行赋值也会覆盖函数

test(3)

# input = 2
# input("请输入:")

# int = 50
# print(int("45"))


# Python 里 函数名也可以理解为一个变量名
