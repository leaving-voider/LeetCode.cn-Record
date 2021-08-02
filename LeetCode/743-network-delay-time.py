###############################################################################################
# 朴素dijkstra
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)，地图消耗
###############################################################################################
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        N = 110
        g = [[float("inf")]*N for _ in range(N)]
        dist = [float("inf")]*N 
        st = [0]*N 

        def dijkstra(k):
            dist[k] = 0
            for _ in range(n-1):
                t = -1
                for j in range(1, n+1):
                    if not st[j] and (t == -1 or dist[j] < dist[t]):
                        t = j
                
                st[t] = 1

                for j in range(1, n+1):
                    if dist[t] + g[t][j] < dist[j]:
                        dist[j] = dist[t] + g[t][j]
        
        for u, v, w in times:
            g[u][v] = min(g[u][v], w)

        dijkstra(k)
        res = 0
        for i in range(1, n+1):
            if dist[i] == float("inf"):
                return -1
            res = max(res, dist[i])
        return res


###############################################################################################
# SPFA算法
###########
# 时间复杂度：O(m)，边的个数
# 空间复杂度：O(m)
###############################################################################################
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        N, M = 110, 6010
        h = [-1]*N 
        wth = [0]*M 
        val = [0]*M
        nex = [-1]*M
        idx = 0

        queue = [0]*M
        dist = [float("inf")]*N 
        st = [0]*N # 仅判断是否在队列中，弹出后可重复进入，所以这里的val和queue都是按边的数量增加的，一次性得开够

        def insert(a, b, w):
            nonlocal idx
            val[idx] = b
            wth[idx] = w 
            nex[idx] = h[a]
            h[a] = idx
            idx += 1
        
        def spfa(k):
            hh, tt = -1, 0
            dist[k] = 0
            queue[tt] = k
            tt += 1
            st[k] = 1

            while tt - hh > 1:
                hh += 1
                t = queue[hh]
                st[t] = 0

                i = h[t]
                while i!=-1:
                    j = val[i]
                    if dist[j] > dist[t] + wth[i]:
                        dist[j] = dist[t] + wth[i]
                        if not st[j]:
                            queue[tt] = j
                            tt += 1
                            st[j] = 1
                    i = nex[i]
        
        for u, v, w in times:
            insert(u, v, w)
        
        spfa(k)

        res = 0
        for i in range(1, n+1):
            if dist[i] == float("inf"):
                return - 1
            res = max(res, dist[i])
        return res
