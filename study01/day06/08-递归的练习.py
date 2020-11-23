# 使用递归求 n!
def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1) * n


print(factorial(4))


# 使用递归求斐波那契数列的第 n 个数字
def sequence(n):
    if n == 1 or n == 2:
        return 1
    return sequence(n-2) + sequence(n-1)


print(sequence(60))
