###############################################################################################
# 递归
###########
# 时间复杂度：O(n)，每个节点遍历一次
# 空间复杂度：O(n)，最坏情况二叉搜索树可能是一根链
###############################################################################################
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = 1
        def dfs(u):
            nonlocal res
            if not u:
                return float("inf"), float("-inf")
            lmin, lmax = dfs(u.left)
            if lmax >= u.val:
                res = 0
            rmin, rmax = dfs(u.right)
            if rmin <= u.val:
                res = 0
            return min(lmin, u.val, rmin), max(lmax, u.val, rmax)
        dfs(root)
        return bool(res)