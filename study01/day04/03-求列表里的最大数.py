nums = [3, 1, 9, 8, 4, 2, 0, 7, 5]
# 升序
# nums.sort()
# print(nums[-1])

# 降序
# nums.sort(reverse=True)
# print(nums[0])

max_num = nums[0]
index = 0
for num in nums:
    if num > max_num:
        max_num = num
        index = nums.index(num)
print(max_num)
print(index)
print(num)
