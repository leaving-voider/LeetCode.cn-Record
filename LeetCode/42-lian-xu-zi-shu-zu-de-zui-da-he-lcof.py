###############################################################################################
# 动规，遍历一次
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = pre = nums[0] # max_记录曾经遇到的最大值，pre记录不包含nums[j-1]时的最大值
        for j in range(2, len(nums)+1):
            pre = max(pre + nums[j-1], nums[j-1]) # 要么加上nums[j-1]， 要么只加nums[j-1]，保持连续
            max_ = max(pre, max_)
        return max_