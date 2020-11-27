# 1.把一个函数当做另一个函数的返回值
def test():
    print("我是test函数")
    return "hello"


def demo():
    print("我是demo函数")
    return test


def bar():
    print("我是bar函数")
    return test()


x = test()
print(x)  # "hello"

y = demo()  # y = test
z = y()  # z = test()
print(z)  # "hello"

a = bar()  # a = test()
print(a)  # "hello"
# 2.把一个函数当做另一个函数的参数,lambda 表达式的使用
# sort filter map reduce

# 3.在函数内部再定义一个函数
