###############################################################################################
# 此题，官方优化动规数组后，状态转移方程并没改变，但dp数组的定义却潜在地变化了，因此初始化和返回值也变化了
###############################################################################################

###############################################################################################
# 本题同样是背包问题，只不过有两个限制，因此可以考虑用三维数组
# 在本题学到了一个动规中很重要的定义：至少和恰好，最多和恰好（仅针对j的定义）
# - 对于返回的结果：如果是恰好，则需要求和，如果是至少至多，则不用
# - 对于初始化：如果是恰好，则只能初始化一个，如果是至少至多，则同维度都要初始化
# 因此对于题中j不同的定义（恰好和最），初始化和返回结果是不同的
# 但状态转移方程是否改变还未完全搞通，此题中只针对j，状态转移的方程不随j的定义变；但官方说max(0, k-earn)和k的定义是有关的
# 因为不是恰好，是至少，所以要加max
###########
# 时间复杂度：O(len*n*minProfit)，len 为数组 group 的长度，需要计算所有状态
# 空间复杂度：O(len*n*minProfit)，动规数组开销
###############################################################################################
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        len_ = len(group) # 工作的个数
        # 动规dp[i][j][k]表示：前i个任务，恰好使用j个人（不是最多j个人），在利润至少为k时（不是恰好）能产生的计划个数
        dp = [[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(len_+1)] 
        # 0个任务，0个人，最低利润为0，也有一种方案（初始化条件）；而dp[0][j][0] j>0的情况不可能出现
        dp[0][0][0] = 1 
        for i in range(1, len_+1):
            neededPeople, earn = group[i-1], profit[i-1]
            for j in range(n+1):
                for k in range(minProfit+1):
                    dp[i][j][k] = dp[i-1][j][k] # 工作无法开展(类比物品无法放入)
                    if j >= neededPeople:
                        dp[i][j][k] += dp[i-1][j-neededPeople][max(0, k-earn)] # 当k<earn说明利润至少为负数，那直接取利润为0的即可
                    dp[i][j][k] %= MOD
        # 对j的定义是恰好j个人，所以要全部求和
        return sum([dp[len_][j][minProfit] for j in range(n+1)])%MOD

###############################################################################################
# 优化动规数组，采用滚动数组；但注意定义改变了：dp[i][j]表示最多i个人，利润至少为j（前面是恰好使用j个人）
# 因此最后直接返回dp[n][minProfit]即可，且状态初始化也要初始化同维度所有的值
###########
# 时间复杂度：O(len*n*minProfit)，需要计算动规数组中每个状态
# 空间复杂度：O(n*minProfit)
###############################################################################################
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        len_ = len(group) # 工作的个数
        # 动规dp[j][k]表示：最多使用j个人（不是恰好），在利润至少为k时能产生的计划个数
        dp = [[0]*(minProfit+1) for _ in range(n+1)]
        # 最多i个人，最低利润为0
        for i in range(n+1):
            dp[i][0] = 1 # 任何人数都能找到1种方案
        for neededPeople, earn in zip(group, profit):
            for j in range(n, neededPeople-1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j-neededPeople][max(0, k-earn)])%MOD
        # 对j的定义是最多j个人，所以直接返回
        return dp[n][minProfit]

# 若要保持原dp[i][j][k]的j、k定义不变，仍然是恰好j个人，利润至少k；只需要改初始化和返回值，状态转移不变
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        len_ = len(group) # 工作的个数
        # 动规dp[i][j][k]表示：最多使用j个人（不是恰好），在利润至少为k时能产生的计划个数
        dp = [[0]*(minProfit+1) for _ in range(n+1)]
        # 恰好0个人，最低利润为0
        dp[0][0] = 1
        for neededPeople, earn in zip(group, profit):
            for j in range(n, neededPeople-1, -1):
                for k in range(minProfit, -1, -1):
                    dp[j][k] = (dp[j][k] + dp[j-neededPeople][max(0, k-earn)])%MOD

        return sum([dp[j][minProfit] for j in range(n+1)])%MOD

# 再次回到未优化前，改变定义为：前i个任务，最多j个人，利润至少为k;同样只需要改初始化和返回值，状态转移方程不变
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        len_ = len(group) # 工作的个数
        # 前i个任务，最多j个人，利润至少为k
        dp = [[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(len_+1)] 
        for j in range(n+1):
            dp[0][j][0] = 1
        for i in range(1, len_+1):
            neededPeople, earn = group[i-1], profit[i-1]
            for j in range(n+1):
                for k in range(minProfit+1):
                    dp[i][j][k] = dp[i-1][j][k] # 工作无法开展(类比物品无法放入)
                    if j >= neededPeople:
                        dp[i][j][k] += dp[i-1][j-neededPeople][max(0, k-earn)]
                    dp[i][j][k] %= MOD
        return dp[len_][n][minProfit]