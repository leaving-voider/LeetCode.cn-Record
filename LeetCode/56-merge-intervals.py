###############################################################################################
# 简单区间合并
###########
# 时间复杂度：O(nlogn), 主要排序消耗
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        start = end = -1
        for l, r in intervals:
            if l <= end:
                end = max(end, r)
            else:
                if start != -1:
                    res.append([start, end])
                start, end = l, r 
        res.append([start, end])
        return res