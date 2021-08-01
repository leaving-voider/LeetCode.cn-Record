###############################################################################################
# 类似高精度加法的做法
###########
# 时间复杂度：O(n), n = max(l1, l2)长度
# 空间复杂度：O(n)，新链表长度
###############################################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        t, c = res, 0
        while l1 and l2:
            s = l1.val + l2.val + c
            t.val = s % 10
            c = s // 10
            l1 = l1.next
            l2 = l2.next
            if l1 and l2:
                t.next = ListNode()
                t = t.next
        while l1:
            t.next = ListNode()
            t = t.next
            t.val = (l1.val + c) % 10
            c = (l1.val + c) // 10
            l1 = l1.next
        while l2:
            t.next = ListNode()
            t = t.next
            t.val = (l2.val + c) % 10
            c = (l2.val + c) // 10
            l2 = l2.next
        if c:
            t.next = ListNode()
            t = t.next
            t.val = c
        return res