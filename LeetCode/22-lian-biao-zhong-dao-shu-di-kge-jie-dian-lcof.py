###############################################################################################
# 思路很简单，res直接指向头节点，直到遍历到第k个之后，res才跟着指向其next，这样最终res必是倒数第k个
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        i = 1
        j = res = head
        while j.next:
            i += 1
            j = j.next
            if i > k:
                res = res.next # 自从第k个往后开始，res也跟着指向下一个
        return res if i >= k else None # 有这么长，才返回，否则为None