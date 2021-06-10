###############################################################################################
# 经过前面好多道动规的训练，本次终于没看答案，也没看题解是否可以使用动规
# 独立对题目进行分析可以使用动规并成功实现通过！
###############################################################################################

###############################################################################################
# 本题同样是背包问题，经过之前的训练，现在对动规不同维度进行严格定义
# dp[i][j]，前i个种类的硬币(可使用可不使用)，amount恰好为j有多少种组法
###########
# 时间复杂度：O(len*amount*total)，len 为数组 coins 的长度，amount为金额，需要计算所有状态，total为金额/币值
# 空间复杂度：O(len*amount)，动规数组开销
###############################################################################################
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        len_ = len(coins)
        # 定义dp[i][j]，前i个种类的硬币(可使用可不使用)，amount恰好为j有多少种组法
        dp = [[0]*(amount+1) for _ in range(len_+1)]
        for i in range(len_+1):
            dp[i][0] = 1
        for i in range(1, len_+1):
            value = coins[i-1]
            for j in range(amount+1):
                dp[i][j] = dp[i-1][j] # 硬币无法使用
                if value <= j: # 硬币可以使用
                    for k in range(1, j//value+1): # 因为每个硬币可以使用多次，因此要加上每种不同的可能
                        dp[i][j] += dp[i-1][j-k*value]
        return dp[len_][amount]

# 利用python的语法，精简写法如下
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        len_ = len(coins)
        # 定义dp[i][j]，前i个种类的硬币(可使用可不使用)，amount恰好为j有多少种组法
        dp = [[0]*(amount+1) for _ in range(len_+1)]
        dp[0][0] = 1
        for i in range(1, len_+1):
            dp[i][0] = 1
            value = coins[i-1]
            for j in range(amount+1):
                dp[i][j] = dp[i-1][j] # 硬币无法使用
                dp[i][j] += sum([dp[i-1][j-k*value] for k in range(1, j//value+1)]) if value <= j else 0
        return dp[len_][amount]


###############################################################################################
# 优化动规数组，采用滚动数组（同样脱离官方解法独立完成）
###########
# 时间复杂度：O(len*amount*total)，同样两个循环计算所有状态，此外同样需要计算不同币值组合的总数
# 空间复杂度：O(amount)
###############################################################################################
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 定义dp[i][j]，前i个种类的硬币(可使用可不使用)，amount恰好为j有多少种组法
        dp = [0]*(amount+1)
        for coin in coins:
            dp[0], value = 1, coin
            for j in range(amount, value-1, -1):
                dp[j] += sum([dp[j-k*value] for k in range(1, j//value+1)])
        return dp[amount]


###############################################################################################
# 根据官方给的思路，可以再改写，从而降低到二重循环
# 即便没有按官方给的思路去想，也是同样可以优化该三重循环为二重循环，从第三重循环可以看出，对dp[j]的计算
# 其实是循环取了前面每个等差距离的值并求和，如此一来，可以直接将第二重循环从小到大进行叠加，同样满足计算
###########
# 时间复杂度：O(len*amount)，两个循环计算所有状态
# 空间复杂度：O(amount)
###############################################################################################
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 定义dp[i][j]，前i个种类的硬币(可使用可不使用)，amount恰好为j有多少种组法
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            value = coin
            for j in range(value, amount+1):
                dp[j] += dp[j-value]
        return dp[amount]