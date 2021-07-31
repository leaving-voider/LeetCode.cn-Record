###############################################################################################
# 深搜一次，时间消耗主要在于排序
###########
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)
###############################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dict_ = defaultdict(list)

        def dfs(u, r, c):
            dict_[c].append((r, u.val)) # 进来的都是同列的，还需要记录行
            if u.left:
                dfs(u.left, r+1, c-1)
            if u.right:
                dfs(u.right, r+1, c+1)
        
        dfs(root, 0, 0)

        res = []
        for per in sorted(list(dict_)):
            res.append([per[1] for per in sorted(dict_[per], key=lambda x:(x[0], x[1]))])
        return res