# 求列表中出现次数最多的元素出现的次数
chars = ["a", "c", "x", "d", "p", "a", "p", "a", "c"]
print(chars.count("a"))

# 第一种
max_count = chars.count(chars[0])
for e in chars:
    if max_count < chars.count(e):
        max_count = chars.count(e)

print(max_count)

# 第二种
_dict = {}
for char in chars:
    if char in _dict:
        _dict[char] += 1  # 第二次及之后累加
    else:
        # _dict.update({k: chars.count(k)})
        _dict[char] = 1  # 第一次
print(_dict)
print(max(_dict.values()))

# 第三种
counts = []
for char in set(chars):
    counts.append(chars.count(char))

print(max(counts))