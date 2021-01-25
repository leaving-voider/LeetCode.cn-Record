class Solution:
    # 并查集初始化，根节点均指向自己
    def Init(self):
        for i in range(self.N * self.N * 4):
            self.fa.append(i)
    
    # 寻找该id所在树的根节点的id
    def Find(self, id_):
        if self.fa[id_] == id_:
            return id_
        else:
            self.fa[id_] = self.Find(self.fa[id_])
            return self.fa[id_]

    # 合并两个id所在树，这里没使用 按秩合并
    def Merge(self, id1, id2):
        root1 = self.Find(id1)
        root2 = self.Find(id2)
        # 若根相同，直接退出
        if (root1 == root2):
            return
        self.fa[root1] = root2
        # 每合并一次，总区域数就 - 1
        self.dist -= 1

    def regionsBySlashes(self, grid: List[str]) -> int:
        self.N = len(grid) # N * N
        self.fa = []
        self.Init()
        id_ = 0
        self.dist = self.N*self.N*4
        for i in range(self.N): # 竖排
            for j in range(self.N): # 横排
                id_ = (i*self.N + j)*4 # 表示当前标号，都从0开始，到N*N - 1
                # 块内合并
                if grid[i][j] == '/':
                    self.Merge(id_, id_ + 3) # 左上合并
                    self.Merge(id_ + 1, id_ + 2) # 右下合并
                elif grid[i][j] == '\\':
                    self.Merge(id_, id_ + 1) # 右上合并
                    self.Merge(id_ + 3, id_ + 2) # 左下合并
                else: # 四个全合并
                    self.Merge(id_, id_ + 1) 
                    self.Merge(id_ + 1, id_ + 2)
                    self.Merge(id_ + 2, id_ + 3)
                # between
                if ( j + 1 < self.N): # 只要还在同一排
                    self.Merge(id_ + 1, (i*self.N + j + 1)*4 + 3) # 和右边的最左合并
                if ( i + 1 < self.N): # 只要还有下一排
                    self.Merge(id_ + 2, ((i+1)*self.N + j)*4) # 和下一排的最上合并
        return self.dist
