# 集合是一个无序不重复的容器，可以使用 {} 或者 set 来表示
# {} 有两种意思: 字典、集合
# {} 里如果存放的是键值对，它就是一个字典；如果 {} 存放的是单个元素，它就是一个集合

person = {"name": "zhangssan", "age": 18}  # 字典
x = {"hello", 1, "good"}  # 集合

# 如果有重复的数据，会自动去重
names = {"zhangsan", "lisi", "jack", "tony", "jack", "lisi"}
print(names)  # {'jack', 'zhangsan', 'lisi', 'tony'}

# set 能不能进行增删改查

names.add("阿珂")  # 添加一个元素
print(names)

names.pop()  # 随机删除一个元素
print(names)

names.remove("jack")  # 删除一个指定的元素,如果元素不存在会报错
print(names)

print(names.union(["刘能", "赵四"]))  # union(iterable) 返回一个新的合并的集合
print(names)

names.update(["刘能", "赵四"])  # update(iterable) 将另一个可迭代对象的元素合并到当前集合中
print(names)


names.clear()  # 清空一个集合
print(names)  # 空集合的表示方式不是 {}, 而是 set(), {} 表示的是空字典


