###############################################################################################
# 一次遍历，min_记录之前最小的股票作为买入
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - min_)
            min_ = min(prices[i], min_)
        return res