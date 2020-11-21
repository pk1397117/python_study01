# 求素数
# for else 语句，当for循环正常结束就会执行else，如果中途break就不会执行else
for i in range(2, 201):
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)

# 假设法
for i in range(2, 201):
    flag = True  # 假设i是质数
    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            # 整除了，说明 i 是个合数
            flag = False
            break
    if flag:
        print(i)

# 计数法
for i in range(2, 201):
    count = 0
    lists = []
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            count += 1
            lists.append(j)
    if count == 0:
        print(i, "是质数")
    else:
        print(i, "是合数", "因数有", lists)

