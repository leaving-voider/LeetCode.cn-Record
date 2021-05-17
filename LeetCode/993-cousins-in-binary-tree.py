###############################################################################################
# 深度优先搜索
###########
# 时间复杂度：O(n)，最坏情况下需要遍历整棵树
# 空间复杂度：O(n)，深度优先搜索需要的栈空间，最坏情况为树呈现链状结构，递归深度为n
###############################################################################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, fatherVal, level):
            if node.val == x or node.val == y:
                yield [fatherVal, level]
            if node.left:
                yield from dfs(node.left, node.val, level+1)
            if node.right:
                yield from dfs(node.right, node.val, level+1)
        res = list(dfs(root, -1, 0))

        return res[0][1] == res[1][1] and res[0][0] != res[1][0]