###############################################################################################
# 编辑距离题
###########
# 时间复杂度：O(n1*n2)
# 空间复杂度：O(n1*n2)
###############################################################################################
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)] # dp[i][j]: 把word1前i个改成word2前j个，所需最小操作数(0<=i,j<=各自的长度)
        for i in range(1, n2+1):
            dp[0][i] = i # 全部都是插入
        for i in range(1, n1+1):
            dp[i][0] = i # 全部都是删除
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        return dp[n1][n2]