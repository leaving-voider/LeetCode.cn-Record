###############################################################################################
# 经典动规，不过这个竟然超时了
###########
# 时间复杂度：O(n*coins), n为雪糕数量，coins为钱的数量，计算dp每个状态
# 空间复杂度：O(n*coins)
###############################################################################################
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        num = len(costs)
        # dp[i][j]定义：在前i个雪糕中，用最多j的现金能买到的雪糕最大数量
        dp = [[0]*(coins+1) for _ in range(num+1)]
        for i in range(1, num+1):
            cost = costs[i-1]
            for j in range(coins+1):
                if j < cost: # 买不起第i-1个（从0开始计数）
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j-cost]+1, dp[i-1][j])
        return dp[num][coins]

# 压缩后仍然超时
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        num = len(costs)
        # dp[i][j]定义：在前i个雪糕中，用最多j的现金能买到的雪糕最大数量
        dp = [0]*(coins+1)
        for i in range(1, num+1):
            cost = costs[i-1]
            for j in range(coins, cost-1, -1):
                dp[j] = max(dp[j-cost]+1, dp[j])
        return dp[coins]


###############################################################################################
# 官方方法：仔细分析，直接无脑贪心即可
###########
# 时间复杂度：O(nlogn), 对数组排序的时间复杂度是 O(nlogn)，遍历数组的时间复杂度是 O(n)
# 空间复杂度：O(logn), 空间复杂度主要取决于排序使用的额外空间
###############################################################################################
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for cost in costs:
            if coins >= cost:
                res += 1
                coins -= cost
            else:
                break
        return res

###############################################################################################
# 官方的另一个方法，也是贪心，只不过利用了哈希来计数，免去了排序
###########
# 时间复杂度：O(n + C), 其中 n 是数组 costs 的长度，C 是数组 costs 中的元素的最大可能值, 此题中为10^5
# 空间复杂度：O(C), 记录每个雪糕价格的个数，最坏情况下每个雪糕价格不一样，价格范围在1 - 10^5之间，因此空间最坏为 C
###############################################################################################
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        dict_ = defaultdict(int)
        for cost in costs:
            dict_[cost] += 1
        res = 0
        for i in range(1, 100001):
            if coins >= i:
                thisBuy = min(dict_[i], coins//i)
                res += thisBuy
                coins -= thisBuy*i
            else:
                break
        return res