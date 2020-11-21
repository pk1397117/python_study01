# in 和 not in 运算符
# 用来判断一个内容在可迭代对象里是否存在

word = "hello"
x = input("请输入一个字符:")

# for w in word:
#     if x == w:
#         print("存在")
#         break
# else:
#     print("不存在")

# if word.find(x) == -1:
#     print("不存在")
# else:
#     print("存在")


if x in word:
    print("存在")
else:
    print("不存在")

if x not in word:
    print("不存在")
else:
    print("存在")