# 去重排序
nums = [5, 8, 7, 6, 4, 1, 3, 5, 1, 8, 4]

new_nums = list(set(nums))
new_nums.sort(reverse=True)
print(new_nums)