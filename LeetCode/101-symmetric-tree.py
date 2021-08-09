###############################################################################################
# 递归，妈的第一次用两个指针的树形递归
###########
# 时间复杂度：O(n)，每个节点遍历一次
# 空间复杂度：O(n)，最坏情况二叉搜索树可能是一根链
###############################################################################################
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)


# 同样算法，使用队列迭代实现，连续两个值相同即说明对称
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root.left, root.right]
        hh, tt = -1, 2
        while tt - hh > 1:
            hh += 1
            a = queue[hh]
            hh += 1
            b = queue[hh]
            if not a and not b:
                continue
            if (not a or not b) and (a or b): # a和b只有1个为None
                return False
            if a.val != b.val:
                return False
            queue.append(a.left)
            tt += 1
            queue.append(b.right)
            tt += 1
            queue.append(a.right)
            tt += 1
            queue.append(b.left)
            tt += 1
        return True