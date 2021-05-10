###############################################################################################
# 递归得到叶节点，并使用yield和yield from来统一返回结果，节点递归先左后右，当然也可先右后左
###########
# 时间复杂度：O(n1+n2)，n1和n2分别为两棵树的节点个数
# 空间复杂度：O(n1+n2)，主要消耗为递归所需的栈空间以及存储两个list的空间
###############################################################################################
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                yield node.val # 会继续执行后面的，然后统一把所有结果打包返回
            if node.left:
                yield from dfs(node.left) # 这里的dfs(node.left)返回也是generator，所以得加from
            if node.right:
                yield from dfs(node.right)
        
        list1 = list(dfs(root1))
        list2 = list(dfs(root2))
        return list1 == list2