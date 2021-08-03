###############################################################################################
# 一次遍历
###########
# 时间复杂度：O(n)
# 空间复杂度：O(n)，额外存储，其实也可以不用
###############################################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        t = head
        count = [head]

        while t.next:
            t = t.next
            count.append(t)
        
        if len(count) >= (n+1):
            count[-n-1].next = count[-n].next
        else:
            head = head.next
        return head