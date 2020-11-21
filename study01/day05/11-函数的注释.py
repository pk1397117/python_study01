def add(a: int, b: int):  # add(形参1: type1, 形参2: type2) 定义期望的参数类型，实参与形参期望的数据类型不一致时提示
    """
    这个函数用来求两个数字的和
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 两个数字的和
    """
    return a + b


help(add)  # help(object) 返回对象的帮助信息

x = add(1, 2)
print(x)

y = add("hello", "world")  # add(形参1: type1, 形参2: type2) 定义期望的参数类型，实参与形参期望的数据类型不一致时提示
print(y)



