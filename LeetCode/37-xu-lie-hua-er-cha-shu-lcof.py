###############################################################################################
# 深度先序遍历
###########
# 时间复杂度：O(n), 在序列化和反序列化函数中，我们只访问每个节点一次, 其中 n 是节点数
# 空间复杂度：O(n), 递归会使用栈空间
###############################################################################################
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def left2rightSer(node):
            if node == None:
                yield "None"
            else:
                yield f"{node.val}"
                yield from left2rightSer(node.left)
                yield from left2rightSer(node.right)
        
        res = list(left2rightSer(root))
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def left2rightDes(deque_):
            x = deque_.popleft()
            if x == "None":
                return None
            else:
                t = TreeNode(int(x))
                t.left = left2rightDes(deque_)
                t.right = left2rightDes(deque_)
                return t

        deque_ = deque(data.split(","))
        return left2rightDes(deque_)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))