###############################################################################################
# 常规套路
###########
# 时间复杂度：O(n!*n), 暴搜，搜索树中每个节点都有计算量， 一般算最后一层，所以为n!，另外一个n是加入res的循环
# 空间复杂度：O(n^2)，地图消耗
###############################################################################################
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        N = 20
        res = []
        g = [['.']*N for _ in range(N)]
        col, dg, udg = [0]*N, [0]*N, [0]*N
        def dfs(u):
            if u == n:
                res.append([''.join(per[:n]) for per in g[:n]])
                return
            
            for i in range(n):
                if not col[i] and not dg[u+i] and not udg[n + u - i - 1]:
                    col[i] = dg[u+i] = udg[n+u-i-1] = 1
                    g[u][i] = 'Q'
                    dfs(u+1)
                    col[i] = dg[u+i] = udg[n+u-i-1] = 0
                    g[u][i] = '.'
        dfs(0)
        return res