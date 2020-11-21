person = {"name": "zhangsan", "age": 18, "addr": "襄阳"}
print(person["name"])

# 直接使用key可以修改对应的value
person["name"] = "list"

# 如果key存在，则修改key对影的value；
# 如果key在字典里不存在，会往字典里添加一个新的key-value
person["gender"] = "female"
print(person)

# 把name对应的键值对删除
person.pop("name")
print(person)

# popitem 删除一个元素，结果是被删除的这个元素组成的键值对
result = person.popitem()
print(person)
print(result)  # ('gender', 'female')

# 清空字典
person.clear()
print(person)
