import random
while True:
    player = input("请输入 1剪刀  2石头  3布\n")
    if player == "1":
        print("你:", "剪刀")
    elif player == "2":
        print("你:", "石头")
    elif player == "3":
        print("你:", "布")
    else:
        print("输入有误")

    computer = str(random.randint(1, 3))
    if computer == "1":
        print("电脑:", "剪刀")
    elif computer == "2":
        print("电脑:", "石头")
    elif computer == "3":
        print("电脑:", "布")

    if player == computer:
        print("平局")
    elif player == "1" and computer == "3" or player == "2" and computer == "1" or player == "3" and computer == "2":
        print("你赢了")
    else:
        print("电脑赢了")

    print("")
