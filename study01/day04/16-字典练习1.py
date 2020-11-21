persons = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 20},
    {"name": "wangwu", "age": 19},
    {"name": "jerry", "age": 21},
]

# 让用户输入姓名，如果姓名已经存在提示用户；如果姓名不存在，继续输入年龄，并存入列表里
while True:
    name = input("请输入姓名:\n")
    for person in persons:
        if person["name"] == name:
            print("已存在")
            break
    else:
        break


age = int(input("请输入年龄:\n"))
persons.append({"name": name, "age": age})
print(*persons, sep="\n")
