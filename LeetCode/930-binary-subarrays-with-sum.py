###############################################################################################
# 二重循环直接超时
###########
# 时间复杂度：O(n^2), 其中 n 是数组 nums 的长度
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        accSum = [0]
        for num in nums:
            accSum.append(accSum[-1] + num)
        len_, res = len(nums), 0
        for i in range(len_): # 左开
            for j in range(i+1, len_+1): # 右闭
                if accSum[j] - accSum[i] == goal:
                    res += 1
        return res

###############################################################################################
# 哈希表优化
###########
# 时间复杂度：O(n), 其中 n 是数组 nums 的长度
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        accSum = defaultdict(int)
        acc = res = 0
        for num in nums:
            accSum[acc] += 1
            acc += num
            res += accSum[acc - goal]
        return res

###############################################################################################
# 滑动窗口优化
###########
# 时间复杂度：O(n), 其中 n 是数组 nums 的长度
# 空间复杂度：O(1), 只需要常数的空间
###############################################################################################
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left1 = left2 = right = 0 # 滑动窗口，三个指针
        sum1 = sum2 = 0 # sum1为left1与right之间的数的和，左开右闭，sum2同
        res, len_ = 0, len(nums)
        while right < len_:
            sum1 += nums[right]
            while left1 <= right and sum1 > goal: # 当left和right相同时也可以继续右移，因为可能最右这个数就很大，也同样排除掉
                sum1 -= nums[left1]
                left1 += 1
            sum2 += nums[right]
            while left2 <= right and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            res += left2 - left1 # left1 闭， left2 开 之间的个数为答案
            right += 1
        return res