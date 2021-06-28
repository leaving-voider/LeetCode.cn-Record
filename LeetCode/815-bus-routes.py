###############################################################################################
# 参考官方：广度搜索，但此题需要先建图：每条线路为一个点，线路间有公共站则有边
###########
# 时间复杂度：O(nm + n^2), n 是公交路线的数量，m 是车站的总数量，建图时最坏的情况耗时O(n)×O(m/n)×O(n) = O(nm), 因为当所有线路都经过同样的车站，第三个循环复杂度就为n
### 广度搜索会遍历所有线路与其他线路一次，即O(n^2)
# 空间复杂度：O(n^2 + m)，队列queue O(n)省略 、 图O(n^2) 、 存每个站点所属的公交站列表 rec O(m)，其实我认为rec最坏可能是 O(m*n)，每个站点的所属路线都一样为全部路线
###############################################################################################
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        n = len(routes) # 一条公交线路为一个点
        edge = [[0]*n for _ in range(n)] # 若俩公交线路有公共站点，则为1
        rec = defaultdict(list) # 存每个站点所属的公交站list
        for i in range(n): # 遍历每个路线
            for site in routes[i]: # 路线中的站点
                for j in rec[site]: # 遍历该站点所属的路线
                    edge[i][j] = edge[j][i] = 1
                rec[site].append(i) # 该站点对应的路线

        takeBusesNum = [-1]*n # 记录从起点开始，到第i个公交线路需要坐多少个公交车
        queue = deque()
        for bus in rec[source]: # 一个站点可能在多个路线，因此建图中可能有多个起点
            takeBusesNum[bus] = 1 # 起点初始化为1
            queue.append(bus) # 每个起点都加入
        
        while queue:
            x = queue.popleft()
            for y in range(n):
                # 可以证明，最先到达某个公交路线的换乘是最少的
                if edge[x][y] and takeBusesNum[y] == -1:
                    takeBusesNum[y] = takeBusesNum[x] + 1
                    queue.append(y)

        ret = float("inf")
        for bus in rec[target]: # 遍历目标站点所属的所有公交线路
            if takeBusesNum[bus] != -1:
                ret = min(ret, takeBusesNum[bus])
        
        return -1 if ret == float("inf") else ret