###############################################################################################
# 暴力超时
###########
# 时间复杂度：O(4^50)，大出天际
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        res = 0
        def dfs(r, c, step):
            nonlocal res
            if r < 0 or r >= m or c < 0 or c >= n:
                res += 1
                return
            if step == maxMove:
                return
            dfs(r+1, c, step+1)
            dfs(r-1, c, step+1)
            dfs(r, c+1, step+1)
            dfs(r, c-1, step+1)
        
        dfs(startRow, startColumn, 0)
        return res

###############################################################################################
# dp，这种三个维度的还是第一次做，因为要限制步数，在任何一步都可能有能够出界的方案
# 而且转移的方式也不一样，不是从四方走到中间，而是从中间走到四方
###########
# 时间复杂度：O(maxMove*m*n)
# 空间复杂度：O(maxMove*m*n)
###############################################################################################
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[0]*n for _ in range(m)] for _ in range(maxMove+1)] # dp[i][j][k]: 第i步走到(j,k)的路径数
        dp[0][startRow][startColumn], MOD, res = 1, int(1e9+7), 0

        for i in range(maxMove):
            for j in range(m):
                for k in range(n):
                    for nex_j, nex_k in [(j+1, k), (j-1, k), (j, k+1), (j, k-1)]:
                        if 0 <= nex_j < m and 0 <= nex_k < n: # 只要在界内，就加上去
                            dp[i+1][nex_j][nex_k] += dp[i][j][k]
                        else: # 当出界了，就加到答案上去
                            res = (res + dp[i][j][k]) % MOD
        return res

# 使用两个二维数组，改进一下空间复杂度，减少到m*n
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[0]*n for _ in range(m)] # dp[j][k]: 第i步走到(j,k)的路径数
        dp[startRow][startColumn], MOD, res = 1, int(1e9+7), 0

        for i in range(maxMove):
            newdp = [[0]*n for _ in range(m)]
            for j in range(m):
                for k in range(n):
                    if dp[j][k]: # 此处剪枝，为0的时候直接跳过，因为没有路径可达
                        for nex_j, nex_k in [(j+1, k), (j-1, k), (j, k+1), (j, k-1)]:
                            if 0 <= nex_j < m and 0 <= nex_k < n:
                                newdp[nex_j][nex_k] += dp[j][k]
                            else:
                                res = (res + dp[j][k]) % MOD
            dp = newdp
        return res

###############################################################################################
# 记忆化dp，其实不是所有的循环式dp都能换成dfs来做，有时候需要变换定义，比如:
# 前面的dp[i][j][k]定义为：第i步走到(j,k)的路径数
# 这个记忆化dp[i][j][k]为：第i步在(j,k)的出界路径数
###########
# 时间复杂度：O(maxMove*m*n)
# 空间复杂度：O(maxMove*m*n)
###############################################################################################
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1]*(n+2) for _ in range(m+2)] for _ in range(maxMove+1)] # dp[i][j][k]: 第i步走到(j,k)时，有多少种走法可以出界
        MOD = int(1e9+7)
        def dfs(r, c, step):
            if r <= 0 or r > m or c <= 0 or c > n: # 如果出界了，就返回这种方法
                return 1
            if step == maxMove:
                return 0
            for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if dp[step+1][i][j] == -1: # dp记录，避免重复计算，只有这种dp定义才能避免，前面的循环dp方法没办法dfs递归，最多换成bfs
                    dp[step+1][i][j] = dfs(i, j, step+1)
            return dp[step+1][r+1][c] + dp[step+1][r-1][c] + dp[step+1][r][c+1] + dp[step+1][r][c-1]

        return dfs(startRow+1, startColumn+1, 0)%MOD # 必须把0，0转化为1，1，不然0,0往上到-1,0，python里这种赋值dp的方式会把最后一个覆盖了