###############################################################################################
# 记数组的元素和为 sum，添加 - 号的元素之和为 neg，其余添加 + 的元素之和为 sum−neg；所以
# sum - neg - neg = target，变式得到 neg = (sum - target)/2，所以只需找到有多少种和为neg的子集
# 然后就可以当作类似背包问题的题来做，使用动态规划，只不过不是最大容量，而是刚好得满足容量为neg
###########
# 时间复杂度：O(n*neg)，需要计算动规数组中每个值
# 空间复杂度：O(n*neg)
###############################################################################################
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        neg = (sum(nums) - target)
        if neg < 0 or neg % 2 != 0: # 后者要求(sum(nums) - target)/2得是整数，不然也不可能有这样的子集
            return 0
        neg //= 2
        len_ = len(nums)
        dp = [[0]*(neg+1) for _ in range(len_+1)]
        dp[0][0] = 1 # 前0个元素和为0的解法，有1个
        for i in range(1,len_+1):
            num = nums[i-1]
            for j in range(neg+1):
                dp[i][j] = dp[i-1][j]
                if num <= j:
                    dp[i][j] += dp[i-1][j-num]
        return dp[len_][neg]


###############################################################################################
# 优化动规数组，采用滚动数组
###########
# 时间复杂度：O(n*neg)，需要计算动规数组中每个状态
# 空间复杂度：O(neg)
###############################################################################################
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        neg = (sum(nums) - target)
        if neg < 0 or neg % 2 != 0: # 后者要求(sum(nums) - target)/2得是整数，不然也不可能有这样的子集
            return 0
        neg //= 2

        dp = [0]*(neg+1)
        dp[0] = 1 # 前0个元素和为0的解法，有1个
        for i in range(1,len(nums)+1):
            num = nums[i-1]
            for j in range(neg, num-1, -1):
                dp[j] += dp[j-num]
        return dp[neg]


###############################################################################################
# 回溯遍历所有情况，直接超时
###########
# 时间复杂度：O(2^n)，n 是数组 nums 的长度，所有不同的表达式共2^n种
# 空间复杂度：O(n)，递归的栈空间消耗
###############################################################################################
class Solution:
    def trackback(self, nums, target, index, sum_):
        if index == len(nums):
            self.count += 1 if sum_ == target else 0
        else:
            self.trackback(nums, target, index+1, sum_+nums[index])
            self.trackback(nums, target, index+1, sum_-nums[index])
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        self.trackback(nums, target, 0, 0)
        return self.count