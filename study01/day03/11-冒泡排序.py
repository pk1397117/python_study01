nums = [6, 5, 3, 1, 8, 7, 2, 4]
# nums = [1, 2, 3, 4, 5, 6, 7, 9, 8]

# 冒泡排序思想:
# 让一个数字和它相邻的下一个数字进行比较运算
# 如果前一个数字大于后一个数字则交换连个数据的位置


def exchange(a, b, _list):
    _list[a], _list[b] = _list[b], _list[a]


# 比较次数
count = 0

# for i in range(len(nums) - 1, 0, -1):
#     flag = True  # 假设该趟没有发生交换
#     for j in range(0, i):
#         count += 1
#         if nums[j] > nums[j + 1]:
#             flag = False  # 发生交换，假设不成立
#             exchange(j, j + 1, nums)
#     if flag:  # 确定没有发生交换(说明假设成立，排序完成，终止循环)
#         break

i = len(nums) - 1
while i >= 0:
    flag = True  # 假设该趟没有发生交换
    j = 0
    while j < i:
        count += 1
        if nums[j] > nums[j+1]:
            flag = False  # 发生交换，假设不成立
            exchange(j, j+1, nums)
        j += 1
    i -= 1
    if flag:  # 确定没有发生交换(说明假设成立，排序完成，终止循环)
        break

print(nums)
print(count)
