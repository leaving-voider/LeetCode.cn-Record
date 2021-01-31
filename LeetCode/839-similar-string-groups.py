##############################################################
# 又是并查集的题，对我来说已经比较简单了，并查集就是做这种归类
# 并最后给出连通分量，比较每对字符串是否相似，相似就归到同一集合
##############################################################
class UnionSet:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(self.n))
        # 连通分量初始化
        self.dist = n

    def FindRoot(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.FindRoot(self.parent[x])
        return self.parent[x]

    def Unite(self, x, y):
        root1 = self.FindRoot(x)
        root2 = self.FindRoot(y)
        if root1 == root2:
            return
        self.parent[root1] = root2
        self.dist -= 1

    def Connected(self, x, y):
        return self.FindRoot(x) == self.FindRoot(y)


class Solution:
	# 比较两个字符串是否相似
    def is_similar_anagram(self, x, y):
        first = -1
        second = -1
        for i in range(self.len_word):
            if x[i] != y[i] and first == -1:
                first = i
            elif x[i] != y[i] and second == -1:
                second = i
            # 当不止两个字母不同时，则一定不相似
            elif x[i] != y[i] and second != -1 and first != -1:
                return False
        # 都为-1表示相等，都不为-1且异位的字母相同则相似
        if (first == -1 and second == -1) or (second != -1 and first != -1 and x[first] == y[second] and x[second] == y[first]):
            return True
        # 在这里返回就是只有一个位置的字母不同，那还是不相似
        return False

    def numSimilarGroups(self, strs: List[str]) -> int:
        self.len_ = len(strs)
        self.len_word = len(strs[0])

        Set = UnionSet(self.len_)

        # 从第1个开始遍历（0为起始），和其前面的所有（而不是所有）进行比较，这样避免一些比较上的重复，减少时间复杂度
        for i in range(1, self.len_):
            for j in range(0, i):
            	# 这里做小小的优化，仅当两个字符串不连通时，才比较并合并
                if not Set.Connected(i,j):
                    if self.is_similar_anagram(strs[i], strs[j]):
                        Set.Unite(i, j)
        return Set.dist