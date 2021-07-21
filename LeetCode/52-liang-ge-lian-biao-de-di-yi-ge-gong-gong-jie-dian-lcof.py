###############################################################################################
# 以前做过，有点忘了，循环跳出条件是为同一个节点 或者 同为None
###########
# 时间复杂度：O(m+n)，最多两个链表
# 空间复杂度：O(1)
###############################################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a