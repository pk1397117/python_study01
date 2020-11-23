def add(a, b):
    return a + b


print("0x%X" % id(add))

x = add(4, 5)  # 函数名(实参) 作用是调用函数，获取到函数的执行结果，并赋值给变量 x
print(x)

fn = add  # 相当于给函数 add 起了一个别名 af
print(fn)
print(type(fn))

print(fn(3, 7))

# 除了使用 def 关键字定义一个函数以外，我们还能使用 lambda 表达式定义一个函数
# 匿名函数，用来表达一个简单的函数，函数调用的次数很少，基本上就是调用一次
# 1.给它定义一个名字(很少这样使用)
# 2.把这个函数当做参数传给另一个函数使用(使用场景比较多)
mul = lambda a, b: a * b
print(mul(4, 5))

