ages = [12, 23, 30, 17, 16, 22, 19]
m = map(lambda e: e + 2, ages)  # 对每个元素进行操作,将结果打包成一个可迭代的 map 对象
print(m)
print(list(m))

# map 也是用一次就没了 类似于 Java 里的 Stream
print(list(m))
