# "百马百担"问题，有一百匹马，驮一百担货，大马驮3担，中马驮2担，两只小马驮1担，问有大，中，小马各几匹？
big = 0
middle = 0
little = 0
count = 0
for i in range(0, 34):
    for j in range(0, 51):
        if 3*i + 2*j + 0.5*(100-i-j) == 100:
            print(i, j, 100-i-j)
            count += 1

print(count)
