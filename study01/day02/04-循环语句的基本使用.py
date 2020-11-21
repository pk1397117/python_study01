i = 0
while i < 10:
    print(i)
    i += 1


for j in range(0, 10):  # 左闭右开 ;in的后面必须是一个可迭代对象(字符串、字典、元组、集合、range....)
    print(j)

result = 0
for i in range(1, 101):
    result += i
print(result)

for i in range(0, 10):
    if i == 5:
        continue
    print(i)
    