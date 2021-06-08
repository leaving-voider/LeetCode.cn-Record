###############################################################################################
# 本题通过变换，再次转化成背包问题：通过把石头分成两堆，假设这两堆碰撞后有最小的差值，则一堆和为neg，
# 另一堆和为sum - neg，因此，我们要找的就是 sum - neg - neg 最小，即 neg在不超过sum/2的情况下的最大值
# 此时题目已经转化为背包问题，容量为sum/2，物体的重量为stone[i]，价值也为stone[i]，用动规求解
###########
# 时间复杂度：O(n*maxNeg)，需要计算动规数组中每个值
# 空间复杂度：O(n*maxNeg)，动规数组开销
###############################################################################################
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        len_, sum_ = len(stones), sum(stones)
        maxNeg = sum_//2
        dp = [[False]*(maxNeg+1) for _ in range(len_+1)]
        dp[0][0] = True # 前0个石头是能凑出重量为0的

        for i in range(1, len_+1):
            weight = stones[i-1]
            for j in range(maxNeg+1):
                dp[i][j] = dp[i-1][j]
                if j >= weight:
                    dp[i][j] |= dp[i-1][j-weight]
        
        return sum_ - 2*max([index for index in range(maxNeg+1) if dp[len_][index]])


###############################################################################################
# 优化动规数组，采用滚动数组
###########
# 时间复杂度：O(n*maxNeg)，需要计算动规数组中每个状态
# 空间复杂度：O(maxNeg)
###############################################################################################
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_ = sum(stones)
        maxNeg = sum_//2
        dp = [False]*(maxNeg+1)
        dp[0] = True # 前0个石头是能凑出重量为0的

        for i in range(1, len(stones)+1):
            weight = stones[i-1]
            for j in range(maxNeg, weight-1, -1):
                dp[j] |= dp[j-weight]
        
        return sum_ - 2*max([index for index in range(maxNeg+1) if dp[index]])