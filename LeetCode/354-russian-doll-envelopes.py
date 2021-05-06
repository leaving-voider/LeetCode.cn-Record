###############################################################################################
# 此题和[面试题 17.08. 马戏团人塔]几乎同一个题型，同样先排序，再[300. 最长递增子序列]方法
###########
# 时间复杂度：O(n*logn)，sorted排序时间复杂度为n*logn，产生长度为n的数组并遍历使用二分查找，同样n*logn
# 空间复杂度：O(n)，maximum数组
###############################################################################################
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 二分查找，返回x插入点
        def bisect_(nums, x):
            l, r = 0, len(nums) - 1
            loc = r + 1
            while(l<=r):
                mid = (l+r)//2
                if nums[mid] >= x:
                    loc = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return loc
        
        maximum = []
        # 以宽为主升序排序（sorted默认），宽同则高降序排序
        for envelope in sorted(envelopes, key = lambda x:[x[0], -x[1]]):
            loc = bisect_(maximum, envelope[1])
            maximum[loc:loc+1] = [envelope[1]]
        return len(maximum)