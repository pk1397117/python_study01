print(abs(-1))

print(all(["hello", "good", "yes"]))
print(all(["hello", 1]))
print(all(["hello", 0]))

print(any([0, 0, 0]))
print(any([0, 0, "hello"]))

print(bin(5))
print(chr(97))
print(ord("a"))

# 列出对象所有的属性和方法
print(dir([1]))

# divmod(num1,num2) 返回 num1 // num2 和 num1 % num2 的两个结果打包的元组
quotient, remainder = divmod(15, 2)
print(quotient, remainder)


# exit(0)

print(help(int))