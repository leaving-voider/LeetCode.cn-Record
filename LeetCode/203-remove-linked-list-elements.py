###############################################################################################
# 构造一个头节点
###########
# 时间复杂度：O(n)，链表的长度
# 空间复杂度：O(1)
###############################################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = ListNode(0, head)
        res = node
        while(node.next):
            mid = node.next
            if mid.val == val:
                node.next = mid.next
            else:
                node = node.next
        return res.next
