# 有几个内置函数和内置类，用到了匿名函数
nums = [4, 8, 2, 1, 7, 6]
# 列表的 sort 方法，会直接对列表进行排序
nums.sort()
print(nums)

ints = (5, 9, 2, 1, 3, 8, 7, 4)
# sorted 内置函数: 获取可迭代对象里的元素进行排序，生成一个新的有序列表，不会改变原有列表
x = sorted(ints)
print(x)

students = [
    {"name": "zhangsan", "age": 18, "score": 98, "height": 180},
    {"name": "lisi", "age": 21, "score": 97, "height": 185},
    {"name": "Jack", "age": 22, "score": 100, "height": 175},
    {"name": "Tony", "age": 23, "score": 90, "height": 176},
    {"name": "Henry", "age": 18, "score": 95, "height": 172}
]


# 字典和字典之间不能使用比较运算
# students.sort()


def foo(element):
    # print("element = {}".format(element))
    return element["age"]  # 通过返回值告诉 sort 方法，按照元素的哪个属性进行排序


# 需要传递参数 key 来指定比较规则
# key 参数类型是函数
# 在 sort 方法内部实现中，调用了传递给 key 的函数，并且传递了一个参数，参数就是调用 sort 方法的列表里的元素
# students.sort(key=foo)

# 使用 lambda 表达式代替函数
students.sort(key=lambda stu: stu["age"])
print(*students, sep="\n")
