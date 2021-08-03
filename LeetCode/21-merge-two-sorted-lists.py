###############################################################################################
# 经典归并应用
###########
# 时间复杂度：O(n)，两个链表总长n
# 空间复杂度：O(n)
###############################################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        i = head
        t1, t2 = l1, l2
        while t1 and t2:
            i.next = ListNode()
            if t1.val <= t2.val:
                i.next.val = t1.val
                i = i.next
                t1 = t1.next
            else:
                i.next.val = t2.val
                i = i.next
                t2 = t2.next
        
        while t1:
            i.next = ListNode()
            i.next.val = t1.val
            i = i.next
            t1 = t1.next
        while t2:
            i.next = ListNode()
            i.next.val = t2.val
            i = i.next
            t2 = t2.next
        return head.next
                