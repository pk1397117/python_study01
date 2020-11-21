masters = ["王昭君", "甄姬", "貂蝉", "妲己", "小乔", "大乔"]

# 删除数据有三个相关的方法 pop remove clear
# pop() 删除列表末尾元素并返回末尾元素
x = masters.pop()
print(x)  # 大乔
print(masters)

# pop(index) 删除列表索引对应元素并返回该元素
x = masters.pop(3)
print(x)
print(masters)

# remove(value) 删除指定元素
masters.remove("小乔")
# masters.remove("妲己") #元素不存在，报错
print(masters)

# del 使用del也可以删除数据
del masters[2]
print(masters)

# clear 清空列表
masters.clear()
print(masters)  # []

tanks = ["亚瑟", "程咬金", "盾山", "张飞", "廉颇", "程咬金"]
# 查询相关的方法
print(tanks.index("盾山"))  # 2
# print(tanks.index("庄周"))  # 如果元素不存在则报错
print(tanks.count("程咬金"))  # 2
# in 运算符
print("张飞" in tanks)  # True
print("苏烈" in tanks)  # False

# 修改元素
# 使用下标可以直接修改列表里的元素
tanks[5] = "铠"
print(tanks)

