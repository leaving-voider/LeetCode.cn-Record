###############################################################################################
# 官方方法，将提醒转化为打家劫舍可解决的问题，采用动态规划+滚动数组
###########
# 时间复杂度：O(n+m)，n为数组nums长度，m为nums中最大值
# 空间复杂度：O(m)，在转化题型时需要设置allnums数组，消耗了空间
###############################################################################################
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # 创建数组用于存放第几个数共能加多少点数，因此要使数组能放下最大的数
        allnums = [0]*(max(nums)+1)
        for per in nums:
            allnums[per] += per
        
        # 使用allnums数组便将题目转化为打家劫舍可解问题
        first = allnums[0]
        second = allnums[1]
        for i in range(2, len(allnums)):
            first, second = second, max((first+allnums[i]), second)
        return second