###############################################################################################
# 邻接表 + 两次dfs遍历，第一次建立无向图，第二次直接找到距离为k的点
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        N = 1010
        h = [-1]*N
        val = [0]*N
        nex = [-1]*N
        idx = 0

        def insert(a, b):
            nonlocal idx
            val[idx] = b
            nex[idx] = h[a]
            h[a] = idx
            idx += 1
        
        def dfs(node):
            if not node:
                return
            if node.left:
                insert(node.val, node.left.val)
                insert(node.left.val, node.val)
            if node.right:
                insert(node.val, node.right.val)
                insert(node.right.val, node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        ans = []
        st = [0]*N
        def dfs2(value, level):
            if st[value]:
                return
            st[value] = 1
            if level == k:
                ans.append(value)
                return
            i = h[value]
            while i != -1:
                j = val[i]
                dfs2(j, level+1)
                i = nex[i]

        dfs2(target.val, 0)
        return ans

# 哈希表替代邻接表和st数组，实测消耗时间变多，空间消耗变少
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dict_ = defaultdict(list)

        def insert(a, b):
            dict_[a].append(b)
        
        def dfs(node):
            if not node:
                return
            if node.left:
                insert(node.val, node.left.val)
                insert(node.left.val, node.val)
            if node.right:
                insert(node.val, node.right.val)
                insert(node.right.val, node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        ans = []
        st = defaultdict(int)
        def dfs2(value, level):
            if st[value]:
                return
            st[value] = 1
            if level == k:
                ans.append(value)
                return

            for i in dict_[value]:
                dfs2(i, level+1)

        dfs2(target.val, 0)
        return ans