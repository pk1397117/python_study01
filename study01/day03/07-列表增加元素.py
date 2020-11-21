# 列表是用来保存多个数据的，是有序可变的
# 操作列表，增删改查

heros = ["阿珂", "嬴政", "韩信", "露娜", "后裔", "亚瑟", "李元芳"]

# 添加元素的方法 append insert extend
# append 在列表的末尾追加数据
heros.append("黄忠")
print(heros)

# insert(index, obj) 在指定位置增加数据
heros.insert(3, "李白")
print(heros)

# extend(iterable) 合并可迭代对象的数据
# A.extend(B) ==> 将可迭代对象 B 的元素添加到 A 里
x = ["马可波罗", "米莱迪", "狄仁杰"]
heros.extend(x)
print(heros)
