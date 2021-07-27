###############################################################################################
# 宽搜 + 排序
###########
# 时间复杂度：O(nlogn), 排序消耗
# 空间复杂度：O(n)
###############################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        queue = [0]*30
        hh, tt = -1, 1
        queue[0] = root
        num = []
        while tt - hh > 1:
            hh += 1
            t = queue[hh]
            num.append(t.val)
            if t.left:
                queue[tt] = t.left
                tt += 1
            if t.right:
                queue[tt] = t.right
                tt += 1
        num = list(set(num))
        num.sort()
        return num[1] if len(num) > 1 and num[1] > num[0] else -1


###############################################################################################
# 深搜
###########
# 时间复杂度：O(n)
# 空间复杂度：O(logn)
###############################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.res = -1
        def dfs(node):
            if not node:
                return
            if node.val > self.res and self.res != -1:
                return
            if node.val > root.val:
                self.res = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res