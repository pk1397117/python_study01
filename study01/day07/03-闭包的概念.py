# 闭包是由函数及其相关的引用环境组合而成的实体(即：闭包=函数块+引用环境)
# 如果在一个内部函数里，对外部作用域(但不是全局作用域)的变量进行引用，那么这个内部函数就被认为是闭包
def outer(n):
    num = n  # 在外部函数里定义了一个变量x，是一个局部变量
    pass

    def inner():  # outer 的内嵌函数
        # nonlocal 在内部函数修改外部函数的局部变量
        nonlocal num
        num = 3
        return num + 1
    return inner


print(outer(3)())
print(outer(4)())
