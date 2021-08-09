###############################################################################################
# 递归
###########
# 时间复杂度：O(n)，每个节点遍历一次
# 空间复杂度：O(n)，最坏情况可能是一根链
###############################################################################################
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level = 0
        res = []
        def dfs(u, lev):
            nonlocal level
            if not u:
                return
            
            if lev > level:
                res.append([])
                level += 1
            res[lev-1].append(u.val)
            dfs(u.left, lev+1)
            dfs(u.right, lev+1)
        dfs(root, 1)
        return res