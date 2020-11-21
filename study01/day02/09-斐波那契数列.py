lists = [0, 1]
for i in range(2, 12):
    e = lists[i-1] + lists[i-2]
    lists.append(e)

print(lists)
print(lists[11])

num1 = 0
num2 = 1
num3 = num1 + num2
num4 = num2 + num3