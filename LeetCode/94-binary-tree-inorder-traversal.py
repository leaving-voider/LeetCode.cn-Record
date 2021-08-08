###############################################################################################
# 基本递归
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)
###############################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(u):
            if not u:
                return
            dfs(u.left)
            res.append(u.val)
            dfs(u.right)
        dfs(root)
        return res