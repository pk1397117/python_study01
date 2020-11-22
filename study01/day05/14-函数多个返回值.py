def test(a, b):
    x = a // b
    y = a % b

    # 一般情况下，一个函数最多只会执行一个return语句
    # 特殊情况下(finally语句)下，一个函数可能会执行多个return语句
    # return x  # return语句表示一个函数的结束
    # return y  # Unreachable 不可达的
    return x, y  # 返回多个值就返回它们组成的元组


result = test(13, 5)
print("商是{},余数是{}".format(result[0], result[1]))

shang, yushu = test(16, 3)
print("商是{},余数是{}".format(shang, yushu))
