###############################################################################################
# 广度
###########
# 时间复杂度：O(n + n^k), 建图 + 最多需要遍历 k 层，每个节点下最多有 n 个分支
# 空间复杂度：O(n^2 + n^k), 关系图 + 队列空间
###############################################################################################
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        relations = [[0]*n for _ in range(n)]
        for first, second in relation:
            relations[first][second] = 1
        
        def nextStatuses(where: int) -> Generator[int, None, None]:
            for location, flag in enumerate(relations[where]):
                if flag:
                    yield location

        queue = deque([(0, 0)])
        res = 0
        while queue:
            where, step = queue.popleft()
            for nextLocation in nextStatuses(where):
                if nextLocation == n - 1 and step + 1 == k:
                    res += 1
                if step +1 < k:
                    queue.append((nextLocation, step + 1))
        return res


###############################################################################################
# 深度
###########
# 时间复杂度：O(n + n^k), 建图 + 最多需要遍历 k 层，每个节点下最多有 n 个分支
# 空间复杂度：O(n^2 + k), 关系图 + 栈空间
###############################################################################################
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        relations = [[0]*n for _ in range(n)]
        for first, second in relation:
            relations[first][second] = 1
        
        self.res = 0
        def dfs(where: int, step: int):
            if step > k:
                return
            if where == n - 1 and step == k:
                self.res += 1
            for nextLocation, flag in enumerate(relations[where]):
                if flag:
                    dfs(nextLocation, step + 1)
        dfs(0, 0)
        return self.res


###############################################################################################
# 动规
###########
# 时间复杂度：O(k*m), 其中 m 为 relation 数组的长度
# 空间复杂度：O(n*k)
###############################################################################################
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        # 定义dp[i][j]：恰好经过i轮，到第j个玩家的方案数
        dp = [[0]*(n) for _ in range(k+1)]
        dp[0][0] = 1
        for i in range(1, k+1):
            for src, dst in relation:
                dp[i][dst] += dp[i-1][src] # 只有在i-1轮的位置能够到达i轮的这个位置，才加上去
        return dp[k][n-1]

# 优化空间为一维O(n)
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        # 定义dp[i][j]：恰好经过i轮，到第j个玩家的方案数
        dp = [0]*n
        dp[0] = 1
        for i in range(1, k+1):
            nextdp = [0]*n # 用nextdp来辅助, 因为dp中的值不论谁被先改变，之后都会有需要使用的可能
            for src, dst in relation:
                nextdp[dst] += dp[src]
            dp = nextdp
        return dp[n-1]