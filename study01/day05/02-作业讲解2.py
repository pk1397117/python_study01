# 用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)
sing = ("李白", "白居易", "李清照", "杜甫", "王昌龄", "王维", "孟浩然", "王安石")
dance = ("李商隐", "杜甫", "李白", "白居易", "岑参", "王昌龄")
rap = ("李清照", "刘禹锡", "岑参", "王昌龄", "苏轼", "王维", "李白")

# (1)求选课学生总共有多少人
print("选课学生总共有%d人" % len(set(sing + dance + rap)))

# (2)求只选了第一个学科的人的数量和对应的名字
count = 0
course_one = []
for s in sing:
    if s not in dance and s not in rap:
        course_one.append(s)
        count += 1
print("只选了第一个学科的人有%d人,分别是:" % count, *course_one)

# (3)求只选了一门学科的学生的数量和对应的名字
# (4)求只选了两门学科的学生的数量和对应的名字
# (5)求选了三门学生的学生的数量和对应的名字
choose_one = []
choose_two = []
choose_three = []
num1 = 0
num2 = 0
num3 = 0
for student in set(sing + dance + rap):
    count = 0
    if student in sing:
        count += 1
    if student in dance:
        count += 1
    if student in rap:
        count += 1
    if count == 1:
        choose_one.append(student)
        num1 += 1
    if count == 2:
        choose_two.append(student)
        num2 += 1
    if count == 3:
        choose_three.append(student)
        num3 += 1
print("只选了一门学科的学生有%d个,分别是:" % num1, *choose_one)
print("只选了两门学科的学生有%d个,分别是:" % num2, *choose_two)
print("选了三门学科的学生有%d个,分别是:" % num3, *choose_three)


