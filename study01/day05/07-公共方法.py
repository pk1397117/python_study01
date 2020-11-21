# 可迭代对象.png
# + : 可以用来拼接，用于 字符串、元组、列表
print("hello" + "world")
print(("good", "yes") + ("hi", "ok"))
print([1, 2, 3] + [4, 5, 6])

# - : 求集合差集，只能用于集合
print({1, 2, 3, 4, 5, 6} - {2, 4})

# * : 与整数n相乘，复制n个可迭代对象合并为一个，用于字符串、列表、元组。不能用于字典与集合
print("hello" * 3)
print([1, 2, 3] * 3)
print((1, 2, 3) * 3)

# in/not in ,用于 字符串、列表、元组、字典、集合
print("a" in "abc")
print(1 in [1, 2, 3])
print(1 in (1, 2, 3))
print("name" in {"name": "zhangsan", "age": 18, "height": "180cm"})
print("a" in {"a", "b", "c"})

# 带下标的遍历 enumerate 类的使用，一般用于列表、元组等带索引的可迭代对象
nums = [19, 82, 39, 12, 34, 58]
for i, e in enumerate(nums):
    print("第%d个数据是%d" % (i, e))

person = {"name": "zhangsan", "age": 18, "height": "180cm"}

for i, k in enumerate(person):
    print(i, k)
