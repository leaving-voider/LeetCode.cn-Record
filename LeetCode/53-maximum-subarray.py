###############################################################################################
# 线性dp
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N # dp[i]: 以i结尾的值最大串
        dp[0] = nums[0]

        for i in range(1, N):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp[i] for i in range(N))