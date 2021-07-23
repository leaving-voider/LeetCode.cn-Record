###############################################################################################
# 先排个序，再用类似于区间合并的思想即可
###########
# 时间复杂度：O(nlogn), 排序
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda x:x[0])
        for l, r in ranges:
            if l > left:
                return False
            elif r >= left:
                left = r + 1
            if left > right:
                return True
        return False