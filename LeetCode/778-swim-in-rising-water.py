#########################################################################
# 由于已经做了很多到并查集的题了，该题思路就比较简单，同样使用并查集
# 按高度从小到大遍历所有的点，并将其和其旁边比其高度低的位置进行合并到同一集合
# 最后当起始点和终点相连通时，即为同一连通分量时，此时的高度也就是需要的时间t
#########################################################################
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
    def swimInWater(self, grid: List[List[int]]) -> int:
        heights = []
        N = len(grid)
        for i in range(N):
            for j in range(N):
                id_ = i*N + j
                heights.append((id_, grid[i][j]))

        heights.sort(key = lambda x: x[1])

        num = N*N
        gridSet = UnionSet(num)
        t = 0
        for i in range(num):
            id_ = heights[i][0]
            x = id_//N
            y = id_%N
            for x_, y_ in ((x-1,y), (x,y+1), (x+1,y), (x,y-1)):
                if x_ >= 0 and x_ <= N-1 and y_ >= 0 and y_ <= N-1:
                    if grid[x_][y_] < heights[i][1]:
                        gridSet.Unite(id_, x_*N+y_)
            if gridSet.Connected(0, num-1):
                t = heights[i][1]
                break
        return t