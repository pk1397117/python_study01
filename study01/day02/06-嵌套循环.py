for i in range(1, 10):
    for j in range(1, i+1):
        print(j, "*", i, "=", j*i, sep='', end='\t')
    print("\n")

i = 1
while i < 10:
    j = 1
    while j < i+1:
        print(j, "*", i, "=", j*i, sep='', end='\t')
        j += 1
    print("\n")
    i += 1

# 打印0-100内所有奇数
for i in range(99, 0, -2):
    print(i, end=' ')

print()

# 打印所有偶数
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=' ')

print()

result = 0
for i in range(1, 101):
    result += i
print(result)

# 统计个位为2，能被3整除的100以内的数的个数
sum = 0
for i in range(0, 101):
    if i % 10 == 2 and i % 3 == 0:
        print(i)
        sum += 1

print(sum)

# 输入一个正整数，判断它是几位数
num = input("请输入一个正整数: ")
print("它是一个", len(num), "位数", sep='')

num = int(input("请输入一个正整数: "))
n = 1
while not(num // 10 ** n == 0):
    n += 1
print("它是一个", n, "位数", sep='')

