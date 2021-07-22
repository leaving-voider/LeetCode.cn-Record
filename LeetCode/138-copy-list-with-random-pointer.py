###############################################################################################
# 自从看了yxc的数组链表后，认为这种方式不好，很麻烦
###########
# 时间复杂度：O(n)，遍历两次
# 空间复杂度：O(n)
###############################################################################################
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p, link = head.next, [Node(head.val, None, None)]
        hash_ = defaultdict(int)
        i = 0
        hash_[head] = i
        while p:
            link.append(Node(p.val, None, None))
            link[-2].next = link[-1]
            i += 1
            hash_[p] = i
            p = p.next
        
        p, i = head, 0
        while p:
            if p.random:
                link[i].random = link[hash_[p.random]]
            else:
                link[i].random = None
            p = p.next
            i += 1
        return link[0]