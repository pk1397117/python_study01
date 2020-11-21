person = {"name": "zhangsan", "age": 18, "x": "y"}

# 查找数据(字典的数据在保存时，时无序的，不能通过下标来获取)
print(person["name"])  # 使用key获取对应的value
# print(person["height"])  # 如果查找的key不存在，会直接报错

# 获取一个不存在的key时，不报错，如果这个key不存在吗，使用默认值
# 使用字典的get方法，如果key不存在，会默认返回None，而不报错
print(person.get("height"))
# 找不到key，自定义默认值
print(person.get("gender", "female"))
print(person.get("name", "lise"))  # zhangsan



# x = "age"
# print(person[x])
# print(person["x"])

