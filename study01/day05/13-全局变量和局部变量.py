a = 100  # 这个变量是一个全局变量，在整个py文件里都可以访问到
word = "hello"


def test():
    x = "hello"  # 这个变量是在函数内部定义的变量，它是局部变量，只能在函数内部使用
    print("x = {}".format(x))

    a = 10  # 在函数内部定义了一个新的局部变量，仅在函数内部覆盖了变量a
    print("函数内部a = {}".format(a))

    # 函数内部如果想要修改全局变量？
    # 使用global对变量进行声名，可以通过函数修改全局变量的值
    global word
    word = "hi"

    print("locals = {}\nglobals = {}".format(locals(), globals()))


test()
# print(x)  # x只能在函数内部使用
print("函数外部a = {}".format(a))
print("函数外部word = {}".format(word))

# 内置函数 globals() 全局变量  locals() 局部变量
print("locals = {}\nglobals = {}".format(locals(), globals()))

# 在Python里，只有函数能够分割作用域
if 3 > 2:
    m = "hi"

print(m)
