###################################################################################
# 我的思路从删除出发，过于复杂，看了教程后，从增加边的角度出发，简单很多！！！
###################################################################################

class UnionSet:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(self.n))
        # 连通分量，初始全是孤立点
        self.dist = self.n

    def FindRoot(self, x):
        if self.parent[x] == x:
            return x
        # 在搜索过程不断减小树的高度，这是一种优化方式，最好不和按秩合并同时使用
        # 因为 按秩合并 需要知道树的size或者高度，这样会破坏高度，不过不会破坏size
        # 但按秩合并的目的就是高度小的往高度大的树上挂，和size没啥关系
        self.parent[x] = self.FindRoot(self.parent[x])
        return self.parent[x]

    def Unite(self, x, y):
        root_x = self.FindRoot(x)
        root_y = self.FindRoot(y)
        if root_x == root_y:
            return False
        self.parent[root_x] = root_y
        self.dist -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        self.n = n
        # 初始化并查集
        Alice_set, Bob_set = UnionSet(self.n), UnionSet(self.n)
        # 记录能删除的个数（Unite返回False都是能删除的边，因为两个点在同一个连通分量）
        self.delete_ = 0

        # 和并查集里的parent保持一致，点都从0开始记
        for edge in edges:
            edge[1] -= 1
            edge[2] -= 1

        # 开始找公共边
        for type_, dot1, dot2 in edges:
            if type_ == 3:
                # 因为alice和bob的点都是一样的，对于公共边
                # 若alice没能成功添加，则两个人同时删除这条边，记一次delete
                # 如果alice成功了，bob也才添加
                if not Alice_set.Unite(dot1, dot2):
                    self.delete_ += 1
                else:
                    Bob_set.Unite(dot1, dot2)

        # 第二次遍历，找各自的边
        for type_, dot1, dot2 in edges:
            if type_ == 1:
                if not Alice_set.Unite(dot1, dot2):
                    self.delete_ += 1
            elif type_ == 2:
                if not Bob_set.Unite(dot1, dot2):
                    self.delete_ += 1
        
        if Alice_set.dist != 1 or Bob_set.dist != 1:
            return -1
        return self.delete_



# ###################################################################################
# # 这是我自己的代码，并不能通过全部80+的测试，原因在于我的思路从删除边出发
# # 而如何最大量地删除非type3的边（只在环上全是type3时才在两个link同时删除）是个问题
# ###################################################################################
# class Solution:
#     def init_links(self):
#         # 初始化自己指向自己（ link[i]代表第i个点的下一个点，其id只能比i大 ）
#         for i in range(self.n+1):
#             self.link_alice.append([i])
#             self.link_bob.append([i])
#         return

#     def go_next(self, this_, who):
#         ####################################################
#         #（问题出在删除上，毕竟之前我们删除了所有和type 3重合的type 1和type 2，进行了第一次优化）
#         # 因此，在找环删除的过程中，当我们删除公共的type 3时，分别在两条link中进行了删除
#         # 导致self.delete_比正常值更大
#         # 因此不能在删除alice的type 3边时，不考虑B，其实就不删除type 3的边就可以了，除非环上全是3
#         ####################################################

#         ##############################
#         # 放弃双边，直接遍历一遍，看有没有0入度的点，看能不能改变结果（不是这个原因）
#         # 毕竟导致结果141的不是因为引入了双边，引不引入在这道题都是一样的
#         # 双边和从头遍历都能解决入度0的点被忽略的问题
#         ##############################
#         if who == "alice":
#             # 当已经把和type 3重复的其他type的边都删除了，那对alice来说，link上剩下的边都是等价的
#             # 所以如果当前的要走的点之前走过了，直接删除这条边即可
#             if this_ in self.path_alice:
#                 self.delete_ += 1
#             else:
#                 self.path_alice.append(this_)
#                 for per in self.link_alice[this_]:
#                     if per == this_:
#                         continue
#                     self.go_next(per, "alice")
#         else: # bob
#             if this_ in self.path_bob:
#                 self.delete_ += 1
#             else:
#                 self.path_bob.append(this_)
#                 for per in self.link_bob[this_]:
#                     if per == this_:
#                         continue
#                     self.go_next(per, "bob")


#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
#         self.n = n
#         # 记录alice和bob各自能走的链路
#         self.link_alice = []
#         self.link_bob = []
#         self.init_links()
#         # 记录遍历Alice和bob的路径，便于检测成环和可删除的路
#         self.path_alice = []
#         self.path_bob = []
#         # 记录能删除的个数
#         self.delete_ = 0
#         # # 记录多余的算作delete的边数，最后需要减去
#         # self.align_del = 0

#         # 记录下各自的可以走的路线
#         for i in range(len(edges)):
#             # Alice
#             if edges[i][0] == 1:
#                 # 说明这条边type 3和type 1共存 且 type 3 先被记录，则type 1这条可以删去
#                 if edges[i][2] in self.link_alice[edges[i][1]]:
#                     # 这个只需要记下来删了一个，根据题目，我们并不需要知道删的什么type的线
#                     self.delete_ += 1
#                 else:
#                     # 题目中说明 edges[i][1] < edges[i][2]
#                     self.link_alice[edges[i][1]].append(edges[i][2])
#                     # # 需要加双向边，不然会导致某些入度为0的点不被遍历到（当然也可以直接从头遍历）
#                     # self.link_alice[edges[i][2]].append(edges[i][1])
#                     # # 不过这样又会导致多了一倍的边，形成许多两点间构成的环，会额外增加self.delete_
#                     # # 因此多余增加了多少条边，就会导致self.delete_增加多少，我们记录下来，最后减去
#                     # # (这种思路没问题)
#                     # self.align_del += 1
#             # Bob
#             elif edges[i][0] == 2:
#                 if edges[i][2] in self.link_bob[edges[i][1]]:
#                     self.delete_ += 1
#                 else:
#                     self.link_bob[edges[i][1]].append(edges[i][2])
#                     # self.link_bob[edges[i][2]].append(edges[i][1])
#                     # self.align_del += 1
#             # both
#             else:
#                 # 说明这条边type 3和type 1共存 且 type 1 先被记录，则type 1这条可以删去
#                 if edges[i][2] in self.link_alice[edges[i][1]]:
#                     self.delete_ += 1
#                 else:
#                     self.link_alice[edges[i][1]].append(edges[i][2])
#                     # self.link_alice[edges[i][2]].append(edges[i][1])
#                     # self.align_del += 1
#                 # 说明这条边type 3和type 2共存 且 type 2 先被记录，则type 2这条可以删去
#                 if edges[i][2] in self.link_bob[edges[i][1]]:
#                     self.delete_ += 1
#                 else:
#                     self.link_bob[edges[i][1]].append(edges[i][2])
#                     # self.link_bob[edges[i][2]].append(edges[i][1])
#                     # self.align_del += 1
        
#         # 开始遍历各自的link
#         self.go_next(1, "alice")
#         self.go_next(1, "bob")
#         ############ 双边的替代方案
#         # for i in range(1,n+1):
#         #     if i not in self.path_alice:
#         #         self.go_next(i, "alice")
#         #     if i not in self.path_bob:
#         #         self.go_next(i, "bob")
#         if len(self.path_alice) != n or len(self.path_bob) != n:
#             return -1
#         return self.delete_