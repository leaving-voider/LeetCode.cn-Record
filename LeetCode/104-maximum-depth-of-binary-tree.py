###############################################################################################
# 递归
###########
# 时间复杂度：O(n)，每个节点遍历一次
# 空间复杂度：O(n)，最坏情况可能是一根链
###############################################################################################
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 0
        def dfs(u, level):
            nonlocal res
            if not u:
                return
            
            if level > res:
                res = level
            dfs(u.left, level+1)
            dfs(u.right, level+1)
        dfs(root, 1)
        return res