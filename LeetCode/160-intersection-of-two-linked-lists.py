###############################################################################################
# 数据结构采用字典不会超时，但用列表直接超时
###########
# 时间复杂度：O(m+n)，两个链表的长度
# 空间复杂度：O(m)，headA存储到字典的消耗
###############################################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A = {headA:1}
        a = headA.next
        while(a):
            A[a] = 1
            a = a.next
        b = headB
        while(b):
            if b in A:
                return b
            b = b.next
        return None
