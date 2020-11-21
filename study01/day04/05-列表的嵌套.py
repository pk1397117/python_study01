import random

# 一个学校，有3个办公室，现在有10位老师等待工位的分配，请编写程序，完成随机分配
teachers = ["张三", "李四", "王五", "赵六", "Jack", "Jerry", "Henry", "Daisy", "Tom", "Chris"]
# room1 = []
# room2 = []
# room3 = []
# rooms = [room1, room2, room3]

rooms = [[], [], []]

for teacher in teachers:
    # rooms[random.randint(0, 2)].append(teacher)
    random.choice(rooms).append(teacher)  # 从列表里随机选择一个数据

# 随机平均
# random.shuffle(teachers)
# for i in range(0, len(teachers)):
#     if i <= 2:
#         rooms[0].append(teachers[i])
#     elif i <= 5:
#         rooms[1].append(teachers[i])
#     else:
#         rooms[2].append(teachers[i])
#
# print(rooms)

# 第0个房间有3个人，分别是
print(len(rooms[0]))
print(*rooms[0])

# for room in rooms:
#     print("第%d个房间有%d个人" % (rooms.index(room)+1, len(room)), "分别是:", *room)

# 带下标的for循环
for i, room in enumerate(rooms):
    print("第%d个房间有%d老师" % (i+1, len(room)), "分别是:", *room)

