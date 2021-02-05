############################################################################################
# 官方给的方法，阅读后加上详细注释，方法较为复杂，比并查集更复杂得多
# 不过这给我在滑动窗口的题解法提供了一个新的思路，用大小根堆+延时删除来维护滑动窗口
# 对于小根堆的增删操作，python的heapq模块已经提供了方法，不用自己实现
############
# 空间复杂度：【延时删除】导致大小根堆在最坏情况下可能包含所有的元素，因此空间复杂度为n
# 时间复杂度：insert(num) 和 erase(num) 的单次时间复杂度为 O(logn)，因此总时间复杂度为 O(nlogn)
############################################################################################
import collections
import heapq
class DualHeap:
    def __init__(self, k: int):
        # 大根堆，维护较小的一半元素，注意 python 没有大根堆，需要将所有元素取相反数并使用小根堆
        self.small = list()
        # 小根堆，维护较大的一半元素
        self.large = list()
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        self.delayed = collections.Counter()

        self.k = k
        # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
        self.smallSize = 0
        self.largeSize = 0


    # 不断地弹出 heap 的堆顶元素，并且更新哈希表
    def prune(self, heap):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    self.delayed.pop(num)
                heapq.heappop(heap)
            # 当堆顶这个不在delayed里，则表示此时的堆顶元素不需要被「延迟删除」，退出
            else:
                break
    
    # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
    def makeBalance(self):
        if self.smallSize > self.largeSize + 1:
            # small 比 large 元素多 2 个
            heapq.heappush(self.large, -self.small[0])
            heapq.heappop(self.small)
            self.smallSize -= 1
            self.largeSize += 1
            # small 堆顶元素被移除，需要进行 prune
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            # large 比 small 元素多 1 个
            heapq.heappush(self.small, -self.large[0])
            heapq.heappop(self.large)
            self.smallSize += 1
            self.largeSize -= 1
            # large 堆顶元素被移除，需要进行 prune
            self.prune(self.large)

    def insert(self, num: int):
        # 若大根堆为空 or 大根堆最大元素（大根堆是取反后按小根堆组织的）比num大，则可以插入大根堆
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        # 否则都插入小根堆
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        # 使大小根堆符合size条件
        self.makeBalance()

    def erase(self, num: int):
        # 先按「延迟删除」加入delayed序列
        self.delayed[num] += 1
        # 属于大根堆
        if num <= -self.small[0]:
            # 虽然「延迟删除」，但真实的size也得-1
            self.smallSize -= 1
            # 如果相等就直接去掉
            if num == -self.small[0]:
                self.prune(self.small)
        else: # 属于小根堆
            self.largeSize -= 1
            if num == self.large[0]:
                self.prune(self.large)
        # 删除一个元素后也得保持大小根堆的size规则
        self.makeBalance()

    # 得到中位数
    def getMedian(self) -> float:
        # 如果大小根堆的总size为奇数，则一定是大根堆比小根堆多一个，则直接返回大根堆的堆顶
        # 否则返回大小根堆堆顶的元素和/2的值
        return float(-self.small[0]) if self.k % 2 == 1 else (-self.small[0] + self.large[0]) / 2

class Solution:
    def medianSlidingWindow(self, nums, k: int):
        dh = DualHeap(k)
        # 先加入初始的k个元素
        for num in nums[:k]:
            dh.insert(num)
        # 得到初始K个元素的中位数
        ans = [dh.getMedian()]
        # 依次遍历后面的元素
        for i in range(k, len(nums)):
            # 加入新的
            dh.insert(nums[i])
            # 删除最左移除的那个
            dh.erase(nums[i - k])
            # 加入新的中位数
            ans.append(dh.getMedian())
        return ans

# ############################################################################################
# # 我的方法很简单，直接遍历，但时间和空间消耗都很大
# ############################################################################################
# import numpy as np
# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         array = []
#         for i in range(len(nums)-k+1):
#             per = nums[i:i+k]
#             per.sort()
#             array.append(np.median(per))
#         return array