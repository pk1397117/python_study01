person = {"name": "zhangsan", "age": 18, "height": "180cm"}

# 列表和元组的每个元素时一个单一的数据，而字典的每个元素是键值对的形式，包含两个数据

# 第一种遍历方式: 直接for...in循环字典
for x in person:  # for...in循环获取的是key
    print(x, "=", person[x])

# 第二种遍历方式: 获取所有的key，然后再遍历key。根据key获取value
print(person.keys())  # dict_keys(['name', 'age', 'height'])

for k in person.keys():
    print(k, "=", person[k])

# 第三种遍历方式: 获取到所有的value
# 只能拿到票value，不能拿到key
for v in person.values():
    print(v)

# 第四种遍历方式:
print(person.items())  # dict_items([('name', 'zhangsan'), ('age', 18), ('height', '180cm')])

for item in person.items():
    print(item)  # 键值对元组

# 第五种遍历方式: 拆包
for k, v in person.items():
    print(k, "=", v)


