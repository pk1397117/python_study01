def add(a, b):
    return a + b


def add_many(iter):
    x = 0
    for n in iter:
        x += n
    return x


nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(add_many(nums))

print(add_many((5, 8, 2, 1, 0, 9, 4)))
print(add_many({5, 9, 2, 1}))

print(add_many(range(2, 19)))


