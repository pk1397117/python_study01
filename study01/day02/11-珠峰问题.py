# 一张纸的厚度大约是0.08mm,对折多少次之后能达到珠穆朗玛峰的高度(8848.13米)
count = 1
while True:
    height = 0.08 * 2 ** count
    if height >= 8848130:
        print(count)
        break
    count += 1
