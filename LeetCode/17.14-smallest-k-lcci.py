###############################################################################################
# 堆排序，这种写法是nlogn的复杂度
###########
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for per in arr:
            heapq.heappush(heap, per)
        return [heapq.heappop(heap) for _ in range(k)]

###############################################################################################
# 手写实现堆排序，理论上应该是n的时间复杂度，只不过可能python比较慢
###########
# 时间复杂度：O(n)
# 空间复杂度：O(k)
###############################################################################################
class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        size = len(arr)
        def down(x):
            t = x
            if 2*x < size and arr[2*x] < arr[t]:
                t = 2*x
            if 2*x+1 < size and arr[2*x+1] < arr[t]:
                t = 2*x+1
            if t - x:
                arr[t], arr[x] = arr[x], arr[t]
                down(t)
        for i in range(size//2-1, -1, -1):
            down(i)
        res = []
        for _ in range(k):
            res.append(arr[0])
            arr[0] = arr[size-1]
            size -= 1
            down(0)
        return res