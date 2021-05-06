###############################################################################################
# 此题采用贪心算法，基本思想是，从第1天开始迭代，在当天可参加的event中选择end day最早的来参加
###########
# 时间复杂度：O(t*logn)，t是所有event的最大时间跨度，logn为小根堆的push和pop的最坏情况的时间复杂度
# 空间复杂度：O(t)，即begins数组空间开销，小根堆开销仅为n，n是events个数
###############################################################################################
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        lastest_end = max(x[1] for x in events)
        begins = [[] for _ in range(lastest_end+1)]
        # 记录开始时间所对应的event序号
        for i in range(len(events)):
            begins[events[i][0]].append(i)

        res = 0
        small = list() # 小根堆，存放event结束日期（其特点为父节点必小于等于两个子节点）
        for day in range(1, lastest_end+1):
            # 今天开始的event的结束日期放入小根堆
            for begin_at_today in begins[day]:
                heapq.heappush(small, events[begin_at_today][1])
            # 今天之前已结束的则踢出小根堆
            while(small and small[0] < day):
                heapq.heappop(small)
            # 参加结束日期最早的，即小根堆的根，并删除该event的记录
            if small: # 判断不为空
                res += 1
                heapq.heappop(small)
        return res