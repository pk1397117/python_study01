# 列表推导式作用是使用简单的语法创建一个列表
teachers = ["张三", "李四", "王五", "赵六", "Jack", "Jerry", "Henry", "Daisy", "Tom", "Chris"]

# nums = []
# for i in range(10):
#     nums.append(i)

# 等同于上述方式
nums = [i for i in range(10)]
print(nums)

x = [i for i in range(10) if i % 2 == 0]
print(x)

y = [teacher for teacher in teachers if teachers.index(teacher) % 2 == 0]
print(y)

# points 是一个列表。这个列表里的元素都是元组
points = [(x, y) for x in range(5, 9) for y in range(10, 20)]
print(points)

# 请写出一段 Python 代码实现分组一个list里面的元素，比如[1,2,3,...100] 变成 [[1,2,3],[4,5,6]...]
m = [i for i in range(1, 101)]
print("m:", m)
n = [[x - 2, x - 1, x] for x in range(1, 101) if x % 3 == 0]
print("n:", n)
o = [m[j:j + 3] for j in range(0, 100, 3)]
print("o:", o)
