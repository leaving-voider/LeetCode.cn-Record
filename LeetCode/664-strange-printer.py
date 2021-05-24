###############################################################################################
# 官方给的动态规划解，该题难点在于，不容易看得出来该题是多阶段决策过程，能通过动态规划求解
###########
# 时间复杂度：O(n^3)，三重循环
# 空间复杂度：O(n²)，存dp数组
###############################################################################################
class Solution:
    def strangePrinter(self, s: str) -> int:
        len_ = len(s)
        dp = [[0]*len_ for _ in range(len_)]
        for i in range(len_-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, len_):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    min_ = float("inf")
                    for k in range(i, j):
                        min_ = min(min_, dp[i][k] + dp[k+1][j])
                    dp[i][j] = min_
        return dp[0][len_-1]