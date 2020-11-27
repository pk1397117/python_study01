# 1.一个函数作为另一个函数的返回值
# 2.一个函数作为另一个函数的参数
# 3.函数内部再定义一个函数

def foo():
    print("我是foo,我被调用了")
    return "字符串foo"


def bar():
    print("我是bar,我被调用了")
    return foo


# x 是函数 bar 的返回值，而函数 bar 返回的是函数 foo
x = bar()
print("x的值是:", x)

# bar() 返回的是 函数 foo;bar()() 相当于 foo(),也就是调用了函数 foo
y = bar()()
print("y的值是:", y)


# 装饰器
def outer():
    m = 100
    def inner():
        print("我是inner函数")

    print("我是outer函数")
    return inner


outer()()