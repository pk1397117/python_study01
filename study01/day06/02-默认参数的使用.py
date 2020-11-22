def say_hello(name, age, city="襄阳"):  # 缺省参数必须放在最后面
    print("大家好,我是{}，我今年{}岁了，来自{}".format(name, age, city))


say_hello("Jack", 19)  # 如果没有传递参数则使用默认值
say_hello("Tony", 20, "北京")  # 如果传递了参数就使用传递的实参
say_hello(city="上海", age=17, name="Daisy")  # 直接对指定形参进行赋值，可以调换参数顺序
say_hello("jerry", city="南京", age=21)  # 如果同时有位置参数和关键字参数，关键字参数必须放在后面

# 缺省参数:
# 有些函数的参数是，如果你传递了参数，就使用传递的参数，如果没有传递参数，就使用默认的值

# print 函数里 sep 和 end 就是缺省参数
print("hello", "你好", sep="-", end="m")


