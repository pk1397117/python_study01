# 有一个列表names，保存了一组姓名 names = ["zhangsan","lisi","Chris","Jerry","Herry"]
# 再让用户输入一个姓名，如果这个姓名在列表里存在，提示用户姓名已存在;
# 如果这个姓名在列表里不存在，就将这个姓名添加到列表里

names = ["zhangsan", "lisi", "Chris", "Jerry", "Herry"]

username = input("请输入一个姓名:")

# if name in names:
#     print("用户姓名已存在")
# else:
#     names.append(username)
#     print("用户添加成功")

for name in names:
    if username == name:
        print("用户已存在")
        break
else:
    names.append(username)
    print("用户添加成功")

print(names)

# 冒泡完善
# 统计列表里出现次数最多的元素
# 求列表里的最大数
# 删除列表里的空字符串
