###############################################################################################
# 因为边权一样，可以用广搜；一下时间复杂度分析可见非常unreasonable
# 但由于n的范围不大于12，所以总的时间消耗小于10^6，可接收
###########
# 时间复杂度：O((n^2)*(2^n))，广搜常规本来是n+m，对每个点循环其所有边，但此题不一样；看循环次数，不止是循环n次
# 因为增加了状态的维度，到达每个点，状态可能有2^n种，所以一共可走的点有n*2^n种，而每次走一个点，边和点同一数量级
# 所以总的就是O((n^2)*(2^n))
# 空间复杂度：O(n*(2^n)),存储所有状态的seen哈希和queue
###############################################################################################
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N, n = 15, len(graph)
        final = sum([1<<i for i in range(n)])
        seen = set()
        queue = []
        res = float("inf")
        def bfs():
            nonlocal res
            hh, tt = -1, 0
            for i in range(n):
                queue.append((i, 1<<i, 0))
                seen.add((i, 1<<i))
                tt += 1
            while tt - hh > 1:
                hh += 1
                t, s, d = queue[hh]
                if s == final:
                    res = min(res, d)
                    continue
                for ne in graph[t]:
                    if (ne, s|(1<<ne)) not in seen: # 允许重复走一个点，但到达相同的点时状态不能一样，这样就能剔除重复点了
                        queue.append((ne, s|(1<<ne), d+1))
                        seen.add((ne, s|(1<<ne)))
                        tt += 1
        bfs()
        return res

###############################################################################################
# 硬核！状态压缩DP，和acwing上的题很像，又有点不一样
# 1、首先是图不是全连通的，需要使用floyd计算每两个点之间的最短路
# 2、我们的DP计算的不是0到某个点的Hamilton最短路，而是任一点到某个点的Hamilton最短路，所以初始化不一样
# 3、题目要求的不是0~n-1的Hamilton最短路，而是全局的hamilton最短路，所以还要取每个终点的hamilton最短路的最小值
###########
# 时间复杂度：O((n^2)*(2^n))，floyd的n^3看起来已经微不足道，直接三个大循环就很大
# 空间复杂度：O(n*(2^n)), DP状态消耗，每个点为终点的状态都有2^n个
###############################################################################################
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        g = [[float("inf")] * n for _ in range(n)] # 便于floyd计算最短路，因此变成邻接矩阵
        for i in range(n):
            for j in graph[i]:
                g[i][j] = 1 # 不带权图，因此默认为1
        
        # floyd 算法预处理出所有点对之间的最短路径长度
        # 因为此题和acwing上的那道【最短Hamilton路径】不一样，那个是全连接图，此题不是，所以要找最短的
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])

        dp = [[float("inf")] * (1 << n) for _ in range(n)] # dp[i][j]: 任一点到达i点，经过的点是j，所经过的最短路径长度；这里和acwing那题定义也不一样，acwing是说从0到i点
        # 因此初始化时，不能只初始化0点了，每个点都要
        for i in range(n):
            dp[i][1<<i] = 0 # 任一点到自己，经过的状态中只有自己一个点，那最短路径长度就是0

        # 同acwing，先遍历每个状态；这里也同区间dp先遍历区间，状态dp先遍历状态
        for j in range(1, 1 << n): # 0就不要了，什么点都没走，什么也到不了，距离无穷大
            for i in range(n): # 到达i点
                if j & (1 << i): # 必须要状态里包含i点，到达i点的路径计算才有意义
                    for k in range(n): # 枚举从哪个点过来的
                        if (j-(1<<i)>>k & 1): # 去掉i这个点后还要包含k这个点，才可能从k转移到i
                            dp[i][j] = min(dp[i][j], dp[k][j ^ (1 << i)] + g[k][i])

        # 因为我们求的从任一点到i点的Hamilton最短路，所以要遍历所有点作为终点的Hamilton最短路，并取最小
        res = min(dp[i][(1 << n) - 1] for i in range(n))
        return res