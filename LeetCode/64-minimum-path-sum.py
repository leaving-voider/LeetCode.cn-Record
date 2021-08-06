###############################################################################################
# 暴搜超时
###########
# 时间复杂度：O(2^(m+n)), 一共需要m+n步，每步都是两种选择，此题m+n最大200，2^200 ≈ 10^60 太吓人了...
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = float("inf")
        def dfs(i,j,d):
            nonlocal res
            if i == m-1 and j == n-1:
                res = min(res, d)
                return
            
            if i+1 < m:
                dfs(i+1, j, d+grid[i+1][j])
            
            if j+1 < n:
                dfs(i, j+1, d+grid[i][j+1])
        
        dfs(0,0,grid[0][0])
        return res

###############################################################################################
# 简单动规
# 此题背包没法做，因为没法确定当m+n-2中某一步选择右or下时下一步的具体位置，就没法加上grid中的值
###########
# 时间复杂度：O(m*n)
# 空间复杂度：O(m*n)
###############################################################################################
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)] # dp[i][j]: 从0,0走到i,j的最短路
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]

# 滚动
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0]*n # dp[j]: 从0,0走到m-1,j的最短路（最后一层时）
        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i-1] + grid[0][i]
        
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][0] # 初始化
                else:
                    dp[j] = min(dp[j], dp[j-1]) + grid[i][j]

        return dp[n-1]
