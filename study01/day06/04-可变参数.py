def add(a, b, *args, mul=1):  # *args 表示可变参数
    # print("a = {},b = {}".format(a, b))
    # print("args = {}".format(args))  # 多出来的可变参数会以元祖的形式保存在args里
    c = a + b
    for arg in args:
        c += arg
    return c * mul


print(add(1, 3))
print(add(9, 5, 4, 2, 0))
print(add(8, 9, 7, 5, 7, 9, 8, 7, 5, 3))
print(add(1, 2, 3, 4, mul=2))


# arg1,arg2 位置参数。一一对应
# *args 可变参数。将多个参数打包成一个 tuple
# **kwargs 可变关键字参数。将多个关键字参数打包成一个 dict
def func(arg1, arg2, *args, **kwargs):
    print(type(args))
    print(type(kwargs))
    if args != ():
        print("非空元组")
        print("args = {}".format(args))
    if kwargs != {}:
        print("非空字典")
        print("kwargs = {}".format(kwargs))


func(1, 2)
func(1, 2, 3)
func(1, 2, 3, a=2)

