ages = [12, 23, 30, 17, 16, 22, 19]
m = map(lambda e: e + 2, ages)
print(m)
print(list(m))

# map 也是用一次就没了 类似于 Java 里的 Stream
print(list(m))
