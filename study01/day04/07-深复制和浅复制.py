import copy

# 浅复制(拷贝)
nums = [1, 2, 3, 4, 5]
nums1 = nums  # 深拷贝/浅拷贝？都不是，这是一个指向，是赋值

nums2 = nums.copy()  # 浅拷贝，两个内容一模一样，但是不是同一个对象

nums3 = copy.copy(nums)  # 和nums.copy()功能一致，都是浅拷贝

# 深拷贝。只能使用copy模块实现
words = ["hello", "good", [100, 200, 300], "yes", "hi", "ok"]

# words1是words的浅拷贝

# 浅拷贝认为只拷贝了一层
words1 = words.copy()
print(id(words[2]), id(words1[2]))

# words2是words的深拷贝
words2 = copy.deepcopy(words)
print(id(words2[0]), id(words[0]))
print(words2[2] is words[2])
print(words2[0] is words[0])
