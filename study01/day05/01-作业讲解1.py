import random

# 声明一个字典保存一个学生的信息，学生信息中包括: 姓名、年龄、成绩(单科)、电话、性别(男。女。不明)
# student = {"name": "张三", "age": 18, "score": 98, "tel": "1388888998", "gender": "female"}

# 声明一个列表，在列表中保存6个学生的信息(6个提1中的字典)

students = [
    {"name": "张三", "age": 18, "score": 98, "tel": "13888889998", "gender": "female"},
    {"name": "李四", "age": 18, "score": 95, "tel": "13886666666", "gender": "male"},
    {"name": "王五", "age": 21, "score": 97, "tel": "13655888889", "gender": "unknown"},
    {"name": "Jerry", "age": 20, "score": 90, "tel": "15666678999", "gender": "unknown"},
    {"name": "Chris", "age": 17, "score": 58, "tel": "13777775523", "gender": "male"},
    {"name": "Jack", "age": 23, "score": 52, "tel": "13999999288", "gender": "female"},
    {"name": "Tony", "age": 15, "score": 89, "tel": "13888888888", "gender": "unknown"}
]

# (1) 统计不及格学生的个数
count = 0
for student in students:
    if student["score"] < 60:
        count += 1
print("不及格的学生有%d个" % count)
# (2) 打印不及格学生的名字和对应的成绩
for student in students:
    if student["score"] < 60:
        print("%s不及格,分数是%d" % (student["name"], student["score"]))
# (2) 统计未成年学生的个数
count_kid = 0
for student in students:
    if student["age"] < 18:
        count_kid += 1
print("未成年学生有%d个:" % count_kid)
# (4) 打印手机尾号是8的学生的名字
for student in students:
    if student["tel"][-1] == "8":
        print("%s的手机尾号是8" % student["name"])
# (5) 打印最高分和对应的学生的名字
max_score = students[0]["score"]
for student in students:
    if max_score < student["score"]:
        max_score = student["score"]
for student in students:
    if student["score"] == max_score:
        print("%s的分数最高，是%d分" % (student["name"], student["score"]))
# (6) 删除性别不明的所有学生(这个地方有个坑，跳不出来的话大家可以在群里套路，或者等老师的解答)
# for student in students:
#     if student["gender"] == "unknown":
#         students.remove(student)

# 方法一: 拿出性别明确的学生放进新的字典里
# new_students = [student for student in students if student["gender"] != "unknown"]

# 方法二: 使用for循环倒着删除，避免"坑"
# for i in range(len(students) - 1, -1, -1):
#     if students[i]["gender"] == "unknown":
#         students.pop(i)

# 方法三: 删除元素，其后元素索引全部减一，重置索引以匹配索引变化
# i = 0
# while i < len(students):
#     if students[i]["gender"] == "unknown":
#         students.pop(i)
#         i -= 1
#     i += 1

# 方法四: 遍历列表切片，删除原列表
# for student in students[:]:
#     if student["gender"] == "unknown":
#         students.remove(student)

# 方法五: 使用内建函数filter()和匿名函数
new_students = filter(lambda x: x["gender"] != "unknown", students)
students = list(new_students)

# (7) 将列表按学生成绩从大到小排序(选做)
for i in range(len(students) - 1, 0, -1):
    for j in range(0, i):
        if students[j]["score"] < students[j+1]["score"]:
            students[j], students[j+1] = students[j+1], students[j]

print(*students, sep="\n")
