###############################################################################################
# 比昨天的hindexⅠ还简单，不用排序了
###########
# 时间复杂度：O(n)，遍历一次
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i in range(len(citations), 0, -1):
            if citations[len(citations) - i] >= i:
                return i
        return 0

###############################################################################################
# 二分，在模板的基础上需要额外进行判断
###########
# 时间复杂度：O(logn)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations)-1
        while l < r:
            mid = (l+r)>>1
            if citations[mid] >= len(citations) - mid:
                r = mid
            else:
                l = mid + 1
        return len(citations) - l if citations[l] >= len(citations) - l else 0