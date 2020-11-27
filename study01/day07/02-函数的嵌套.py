def outer(x):
    m = 100  # 局部变量
    print("我是outer函数")

    def inner():  # inner函数是定义在outer函数内部的一个函数,不能在outer函数外部直接访问
        print("我还是inner函数")

    if x > 18:
        inner()

    return "hello"



