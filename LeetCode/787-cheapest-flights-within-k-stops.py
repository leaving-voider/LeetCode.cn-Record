###############################################################################################
# 典型的bellman_ford算法, 看了下官方所谓的DP解法，思路和bellman_ford是一模一样，两个循环，时间复杂度也一样
# 原来bellman_ford的内核思路是动态规划
###########
# 时间复杂度：O(mn)，mn是bellman_ford最坏的时间复杂度，因为一般k不会大于n，谁会找多于n步的最短路呢？
# 当然此题中的时间复杂度实际是O(km)，m是边的个数，如果算上深拷贝的时间，则为O((m+n)*k)
# 空间复杂度：O(n*k), 中间其实产生了k个n大小的数组
###############################################################################################
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf")]*n  # 到src的距离
        backup = [0]*n # 备份上一次的dist，因为dist可能被覆盖       
        def bellman_ford():
            dist[src], edgelen = 0, len(flights)
            for i in range(k+1): # 题目说的是src和dst之间最多k站，那就是最多k+1步
                backup = copy.deepcopy(dist)
                for j in range(edgelen):
                    fro, to, price = flights[j]
                    dist[to] = min(dist[to], backup[fro] + price)
            return dist[dst] if dist[dst] != float("inf") else -1

        return bellman_ford()        