dict1 = {"a": 100, "b": 200, "c": 300}

# 交换key和value的位置
dict2 = {}
for k, v in dict1.items():
    dict2[v] = k
print(dict2)


dict3 = {v: k for k, v in dict1.items()}
print(dict3)