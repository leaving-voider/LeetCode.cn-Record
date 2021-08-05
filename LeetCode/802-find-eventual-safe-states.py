###############################################################################################
# 深搜居然超time限制了，各种剪枝都不行，包括循环内的边都不再试了，还是超时
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        st = [0]*N
        set_ = set() # 剔除重复边
        def dfs(u):
            flag = 1
            for i in graph[u]:
                if not st[i]:
                    st[i] = 1
                    set_.add(i)
                    flag &= dfs(i)
                    if not flag: # 剪枝1：有一个失败，就直接退出
                        return 0
                    st[i] = 0
                    set_.remove(i)
                else:
                    set_.add(i)
                    return 0
            return flag
        res = []
        for i in range(N):
            if i in set_: # 剪枝2
                continue
            st[i] = 1
            set_.add(i)
            ret = dfs(i)
            if ret:
                res.append(i)
                set_ = set()
            st[i] = 0
        return res

# 实际上深搜是可以的，只不过之前的剪枝不够干净，不止是走过不行的就跳过，实际上走过发现可行的，以其为起点也一定可行
# 这样的time complexity 是 O(n)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        color = [0]*N # 颜色记录状态, 0 未走过，1表示能到达环，2表示安全
        def dfs(u):
            if color[u] > 0: # 说明已经尝试过了
                return color[u] == 2
            color[u] = 1 # 先默认不行
            for i in graph[u]:
                if not dfs(i): # 返回0说明不可行
                    return 0
            color[u] = 2 # 说明这条路可行
            return 1

        return [i for i in range(N) if dfs(i)]

###############################################################################################
# 拓扑排序，把有向图反过来，每次从入度为0（即原来的出度为0）的点开始走，这样每次遇到的这样的点都是答案
# 不过会导致乱序，最后排序就好了
###########
# 时间复杂度：O(n*m + nlogn), n试是点数，m是平均边数；即 制造反向图(拓扑耗时不超过此) + 排序
# 空间复杂度：O(n*m)，反向图，队列和出度消耗O(n)不超过此，排序消耗logn也不超过此
###############################################################################################
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        queue = [0]*N
        d = [0]*N # 记录出度
        antiGraph = [[] for _ in range(N)]
        for i in range(N):
            for j in graph[i]:
                d[i] += 1 # 出度 += 1
                antiGraph[j].append(i)

        def topo():
            hh, tt = -1, 0

            for i in range(N):
                if not d[i]: # 出度为0的就是终点，从这些地方开始走
                    queue[tt] = i 
                    tt += 1
            
            while tt - hh > 1:
                hh += 1
                t = queue[hh]

                for i in antiGraph[t]:
                    d[i] -= 1
                    if not d[i]:
                        queue[tt] = i 
                        tt += 1

            return queue[:tt] # 栈顶所在位置就代表了所有最终入度能为0的点的个数
        return sorted(topo())