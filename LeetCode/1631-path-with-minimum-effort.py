#################################################################################################
# 本题从官方解法学习到，使用并查集，精妙之处在于对每个位置之间的边的代价进行从小到大的排序
# 然后依次加入这个边，直到最终起始和终点属于同一集合，此时我们就能保证，使之相连的边的代价，一定是最小的
# 因为是从小到大加入的边，直接返回最后一个使首尾连通的边的代价即是最小代价
#################################################################################################
class UnionSet:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(self.n))
    
    def FindRoot(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.FindRoot(self.parent[x])
        return self.parent[x]

    def Unite(self, x, y):
        root1 = self.FindRoot(x)
        root2 = self.FindRoot(y)
        if root1 == root2:
            return
        self.parent[root1] = root2

    def Connected(self, x, y):
        return self.FindRoot(x) == self.FindRoot(y)

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        edges = []
        row = len(heights)
        column = len(heights[0])
        for i in range(row):
            for j in range(column):
                id_ = i*column + j
                # 下
                if i != row - 1:
                    edges.append((id_, id_ + column, abs(heights[i][j] - heights[i+1][j])))
                # 右
                if j != column - 1:
                    edges.append((id_, id_ + 1, abs(heights[i][j] - heights[i][j+1])))

        edges.sort(key = lambda x: x[2])

        n = row*column
        pathSet = UnionSet(n)
        least = 0
        for x, y, len_ in edges:
            pathSet.Unite(x, y)
            if pathSet.Connected(0, n-1):
                least = len_
                break
        return least