###############################################################################################
# 直接参考官方方法，经典题型——打家劫舍，采用动态规划
###########
# 时间复杂度：O(n)，n为数组长度
# 空间复杂度：O(1)，采用滚动数组，复杂度减少到最低
###############################################################################################
class Solution:
    def rob(self, nums: List[int]) -> int:
        len_ = len(nums)

        if len_ == 0:
            return 0
        elif len_ == 1:
            return nums[0]

        first = nums[0] # 代表前n-2个最大收益
        second = max(nums[0], nums[1]) # 代表n-1即上一个之前最大收益（包括上一个）

        for i in range(2, len_):
            # first + nums[i]代表抢，second代表不抢
            first, second = second, max((first + nums[i]), second)
        return second