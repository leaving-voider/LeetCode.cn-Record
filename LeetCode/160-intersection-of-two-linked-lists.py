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

###############################################################################################
# 官方的优化，无需哈希，减小空间复杂度
###########
# 时间复杂度：O(m+n)，两个链表的长度
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        a, b = headA, headB
        while(a != b): # 当为同一个节点或同为None则退出循环
            a = a.next if a != None else headB
            b = b.next if b != None else headA
        return a # 返回a或者b都一样
