# 打印所有水仙花数， 水仙花数是一个三位数，其各位数字立方和等于该数本身
for num in range(100, 1000):
    single = num % 10
    ten = num % 100 // 10
    hundred = num // 100
    if single ** 3 + ten ** 3 + hundred ** 3 == num:
        print(num)

while True:
    num = input("请输入一个数：")
    if num == "exit":
        break

