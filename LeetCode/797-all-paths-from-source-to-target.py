###############################################################################################
# 有向无环，直接深搜，复杂度不会太高
###########
# 时间复杂度：O(n*(2^n))，最坏情况就是每一个点都指向所有编号比其大的点，这样的情况下两点之间的连通数为(n*(n-1))/2
# 不过可以自己尝试计算，第0个点到第n-1个点的路径走法X0 = X1 + X2 + ... + Xn-2 + 1 (其中Xi表示从第i个点开始到n-1的走法)
# 所以0到n-1的走法为2^n, 每种走法走完后，还要复制一遍路径到res，所以最坏为O(n*(2^n))
# 空间复杂度：O(n), 存放路径消耗
###############################################################################################
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        res, path = [], [0]
        def dfs(n):
            if n == N - 1:
                res.append([per for per in path])
                return
            for nex in graph[n]:
                path.append(nex)
                dfs(nex)
                path.pop()
        dfs(0)
        return res