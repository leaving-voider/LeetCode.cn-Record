###############################################################################################
# 很明显大小根堆能解决的题
###########
# 时间复杂度：O(nlogn), 主要是排序消耗，n个数，每个数最坏都是logn
# 空间复杂度：O(n)，堆消耗
###############################################################################################
class MedianFinder:

    def __init__(self):
        self.heap_small = [] # 存更大的一半
        self.small = 0
        self.heap_big = [] # 存小的一半
        self.big = 0

    def addNum(self, num: int) -> None:
        if self.small and num >= self.heap_small[0]:
            heapq.heappush(self.heap_small, num)
            self.small += 1
        else:
            heapq.heappush(self.heap_big, -num) # 变负数，就成大根堆了
            self.big += 1
        if self.small - self.big == 2:
            heapq.heappush(self.heap_big, -self.heap_small[0])
            self.big += 1
            heapq.heappop(self.heap_small)
            self.small -= 1
        elif self.big > self.small:
            heapq.heappush(self.heap_small, -self.heap_big[0])
            self.small += 1
            heapq.heappop(self.heap_big)
            self.big -= 1

    def findMedian(self) -> float:
        if self.small == self.big:
            return (self.heap_small[0] - self.heap_big[0]) / 2
        return self.heap_small[0]