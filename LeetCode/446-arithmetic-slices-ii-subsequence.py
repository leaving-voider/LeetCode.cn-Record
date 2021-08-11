###############################################################################################
# 确实有点难想，本来仿照【等差数列划分】也是这个思路，遍历以nums[i]结尾，并且前一个数为nums[j]，但我没有用【计数】来表示
# 而是用的每个子序列的长度，而且还得分情况讨论，极其复杂
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)
###############################################################################################
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))] # dp[i][j]: 以i结尾等差为j的子序列个数
        res = 0
        for i in range(1, len(nums)):
            for j in range(i):
                res += dp[j][nums[i] - nums[j]]
                dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]] + 1 # +1表示加上(nums[j], nums[j])这个序列
        return res