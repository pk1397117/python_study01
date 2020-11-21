# 元组和列表很像，都是用来保存多个数据的
# 使用一对小括号 () 来表示一个元组
# 元组和列表的区别在于，列表是可变数据类型，而元组是不可变数据类型
words = ["hello", "yes", "good", "hi"]  # 列表，使用 [] 表示
nums = (9, 4, 3, 1, 7, 6)  # 元组，使用 () 表示

# 元组和列表一样，也是一个有序的存储数据的容器
# 可以通过下标来获取元素

print(nums[3])
print(nums.count(9))
print(nums.index(9))

# 特殊情况:如何表示只有一个元素的元组？
age = (18,)  # 如果元组里只有一个元素，要元素后面加一个逗号
print(type(age))  # <class 'tuple'>

# tuple 内置类
# tuple(iterable)
print(tuple("hello"))

# 怎样把列表转换成为元组? 元组转换成为列表？
print(tuple(list("world")))
print(list(tuple("python")))

heights = ("189", "174", "170")
print("-".join(heights))
print("".join(("h", "e", "l", "l", "o")))

# 元祖也可以遍历
for i in nums:
    print(i)

j = 0
while j < len(nums):
    print(j)
    j += 1

