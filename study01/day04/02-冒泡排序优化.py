nums = [6, 5, 3, 1, 8, 7, 2, 4]
# nums = [1, 2, 3, 4, 5, 6, 7, 9, 8]
# 比较次数
count = 0
j = 0
while j < len(nums) - 1:
    # 在每一趟里都定义一个flag
    flag = True  # 假设该趟没有发生交换
    i = 0
    while i < len(nums) - 1 - j:
        count += 1
        if nums[i] > nums[i + 1]:
            # 只要交换了，假设就不成立
            flag = False
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        i += 1
    if flag:
        # 这一趟走完以后，flag依然是True，说明这一趟没有进行过交换数据
        break
    j += 1
print(nums)
print(count)
