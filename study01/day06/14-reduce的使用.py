from functools import reduce  # 导入模块的语法

# reduce 以前是一个内置函数
# 内置函数和内置类都在 builtins.py 文件里
# reduce 现在 是 functools 模块里的一个函数
scores = [100, 89, 76, 87]
# reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
print(reduce(lambda x, y: x + y, scores))
print(reduce(lambda x, y: x - y, scores))
print(reduce(lambda x, y: x * y, scores))
print(reduce(lambda x, y: x / y, scores))

students = [
    {"name": "zhangsan", "age": 18, "score": 98, "height": 180},
    {"name": "lisi", "age": 21, "score": 97, "height": 185},
    {"name": "Jack", "age": 22, "score": 100, "height": 175},
    {"name": "Tony", "age": 23, "score": 90, "height": 176},
    {"name": "Henry", "age": 20, "score": 95, "height": 172}
]

# 求所有学生的总年龄
print(sum(map(lambda e: e["age"], students)))
print(sum([stu["age"] for stu in students]))
print(reduce(lambda x, y: x + y["age"], students, 0))  # reduce(function, sequence, initial=_initial_missing)
