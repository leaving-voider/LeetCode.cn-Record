###############################################################################################
# 枚举法，在python里直接超时
###########
# 时间复杂度：O(n²)，求和时间复杂度为O(1)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        len_ = len(nums)
        res = 0
        for i in range(len_):
            sum_ = 0
            for j in range(i, len_):
                sum_ += nums[j]
                if sum_ == k:
                    res += 1
        return res

###############################################################################################
# 一次遍历，利用前缀和+哈希表
###########
# 时间复杂度：O(n)，n 为数组的长度，遍历一次，哈希表查询删除的复杂度均为 O(1)
# 空间复杂度：O(n)，哈希表在最坏情况下可能有 n 个不同的键值
###############################################################################################
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum_ = 0
        counter = Counter() # 哈希表作用
        for i in range(len(nums)):
            sum_ += nums[i]
            # 可以换一种写法，给counter一个初值：counter[0] = 1，这样当sum_ = k时，就不用单独判断res+=1了，直接就有counter[0] = 1可以加
            if sum_ == k:
                res += 1
            res += counter[sum_ - k]
            counter[sum_] += 1
        return res

### 替代写法
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        sum_ = 0
        counter = Counter() # 哈希表作用
        counter[0] = 1 # 为了当sum-k = 0即sum_ 等于k时，有最初的一个1可以加上
        for i in range(len(nums)):
            sum_ += nums[i]
            res += counter[sum_ - k]
            counter[sum_] += 1
        return res