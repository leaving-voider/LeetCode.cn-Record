###############################################################################################
# 记忆化搜索dp
###########
# 时间复杂度：O(nm)，n为横排，m为竖排
# 空间复杂度：O(nm)
###############################################################################################
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r, c = len(matrix), len(matrix[0])
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        
        dp = [[-1]*c for _ in range(r)]
        
        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 1

            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if x >= 0 and x < r and y >= 0 and y < c and matrix[x][y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(x, y) + 1)
            return dp[i][j]
        max_ = 0
        for i in range(r):
            for j in range(c):
                max_ = max(max_, dfs(i, j))

        return max_