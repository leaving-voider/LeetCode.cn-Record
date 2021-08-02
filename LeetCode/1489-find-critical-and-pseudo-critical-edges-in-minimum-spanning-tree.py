###############################################################################################
# 此题用Kruskal解最小生成树问题，但引入了关键边和伪关键边，需要分析如何判断这两类边
# 由于原题给的数据范围小，所以也是一种提示，大概可以最高到n^2logn的级别
# 因此在得到最小生成树的权值value后，遍历每条边，先删除它，对其他边使用Kruskal，如果得到的权值不等于value，说明要么大要么小，若小，说明构不成最小生成树，其为关键边；
# 若能构成，但v > value，说明它还是关键边
# 当这条边不是关键边，则来判断伪关键边，首先加入这条边，如果其在不是关键边的情况下，所得到的生成树还能构成最小生成树同样权值，说明它是伪关键边，有其他可替代边
###########
# 时间复杂度：O((m^2)*α(n)), 原本kruskal的时间复杂度为mlogm，因为主要消耗是排序，但这里就比较复杂了，因为只排了一次序，后面纯使用kruskal
# 是这样的，添加路径压缩后的并查集时间复杂度为α(n), α是阿克曼函数的反函数，n是节点数，因此这里的时间复杂度就是mlogm + (m^2)*α(n) ≈ (m^2)*α(n)
# 空间复杂度：O(n + m)，并查集消耗 + 为边记录原始的index消耗
###############################################################################################
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        N = 100
        father = [0]*N
        for i in range(n):
            father[i] = i # 每个点先指向自己，一个数一个集合

        def find(x):
            # 返回x的祖宗节点（根节点） + 路径压缩
            if (father[x] != x):
                father[x] = find(father[x])
            return father[x]

        def connect(a, b):
            father[find(a)] = find(b)

        for i in range(len(edges)):
            edges[i].append(i) # 记录下原本的位置，因为后面要排序
        edges = sorted(edges, key=lambda x:x[2])

        value = 0
        for a, b, w, _ in edges:
            fa, fb = find(a), find(b)
            if fa != fb:
                value += w
                connect(a, b)

        res = [[], []]
        for i, edge in enumerate(edges):
            # 判断i是否是关键边，判断方法就是不加入它，看会不会得到最小生成树的v == value
            # 如果小于，说明不能形成最小生成树，它就是关键边，如果大于，说明它不能被替换，也是关键边
            father = list(range(n))
            v = 0
            for j, (a, b, w, _) in enumerate(edges):
                if i != j: # 不加入第i条边
                    fa, fb = find(a), find(b)
                    if fa != fb:
                        v += w
                        connect(a, b)
            if v != value: # 说明i是关键边
                res[0].append(edge[3]) # 按自己原来的index加入
                continue

            # 当i不是关键边，判断是否是伪关键边，判断方法就是首先加入它，看最后是不是最小生成树
            # 如果是，因为它不是关键边，那肯定就是伪关键边
            father = list(range(n))
            connect(edge[0], edge[1]) # 首先就连通
            v = edge[2] # 初始化此生成树权值
            for j, (a, b, w, _) in enumerate(edges):
                fa, fb = find(a), find(b)
                if fa != fb:
                    v += w
                    connect(a, b)
            if v == value:
                res[1].append(edge[3])
        return res
