###############################################################################################
# 使用堆，可以自己实现，也可以使用heapq
###########
# 时间复杂度：O(nlogn)，n为所有链表长度，排序只有O(n)，nlogn是最后一个一个弹出
# 空间复杂度：O(n)，堆
###############################################################################################
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        N = int(1e4+10)
        heap = [0]
        size = 0

        def down(x): # 对heap中第x个进行down操作
            t = x
            if x*2 <= size and heap[x*2] < heap[t]:
                t = x*2
            if x*2+1 <= size and heap[x*2+1] < heap[t]:
                t = x*2 + 1
            if t != x:
                heap[x], heap[t] = heap[t], heap[x]
                down(t)
        # 加入heap
        for li in lists:
            while li:
                heap.append(li.val)
                size += 1
                li = li.next
        # 堆排序，O(n)的时间复杂度
        for i in range(size//2, 0, -1):
            down(i)

        res = ListNode()
        i = res
        for _ in range(size):
            i.next = ListNode()
            i.next.val = heap[1] # 取最小的
            i = i.next
            heap[1] = heap[size] # 最后一个替换最小的
            size -= 1 # size -= 1
            down(1) # down操作
            
        return res.next

# python中heapq还是比自己用list实现堆运行更快，估计嵌套了C语言的代码
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        N = int(1e4+10)
        heap = []
        
        for li in lists:
            while li:
                heapq.heappush(heap, li.val)
                li = li.next

        res = ListNode()
        i = res
        for _ in range(len(heap)):
            i.next = ListNode()
            i.next.val = heapq.heappop(heap)
            i = i.next
            
        return res.next