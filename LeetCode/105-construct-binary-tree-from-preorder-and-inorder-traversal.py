###############################################################################################
# 经典题，递归解决，每次递归即找当前子树的根节点，然后再递归构建左右子树
###########
# 时间复杂度：O(n)，每个节点遍历一次
# 空间复杂度：O(n)，最坏情况可能是一根链
###############################################################################################
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        len_ = len(preorder)
        mapping = {num:i for i, num in enumerate(inorder)} # 便于快速定位
        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r: # 说明已经没有节点了
                return None
            root = TreeNode(preorder[pre_l]) # 先通过先序遍历的第一节点来构建root
            t = mapping[preorder[pre_l]] # 通过哈希快速找到该root在中序遍历中的位置
            left_len = t - in_l # 得到该根节点左子树的长度
            root.left = build(pre_l+1, pre_l+left_len, in_l, t-1) # 递归处理左子树
            root.right = build(pre_l+left_len+1, pre_r, t+1, in_r) # 递归处理右子树
            return root # 返回根节点
        return build(0, len_-1, 0, len_-1)

# 稍微难理解一点的迭代做法
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        index = 0
        for i in range(1, len(preorder)): # 从1开始遍历每个前序值
            if inorder[index] != stack[-1].val: # 当index所指向的中序值不等于栈顶值
                stack[-1].left = TreeNode(preorder[i]) # 使第i前序值为栈顶左儿子
                stack.append(stack[-1].left) # 并插入此节点到栈顶
            else:
                while stack and stack[-1].val == inorder[index]: # 循环直到栈空或者栈顶值不等于中序index处的值
                    t = stack.pop()
                    index += 1
                t.right = TreeNode(preorder[i]) # 使第i前序值为最后一个弹出的右儿子
                stack.append(t.right) # 并插入此节点到栈顶
        return root