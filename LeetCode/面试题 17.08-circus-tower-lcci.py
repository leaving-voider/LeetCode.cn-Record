###############################################################################################
# 他人方法：此题分两步，先按身高排序，相同身高体重降序排序，以防最后序列中出现身高相同的情况
# 再对体重使用和[300. 最长递增子序列]一模一样的方法完成此题，最后longest数组长度即历史最长序列长度
###########
# 时间复杂度：O(n*logn)，sorted排序时间复杂度为n*logn，产生长度为n的数组，遍历使用二分查找，同样n*logn
# 空间复杂度：O(n)，longest数组
###############################################################################################
class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        # 最后返回的就是x需要插入longest数组的地方
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
        longest = []
        # 先按x[0]递增排序，如果相同，则按-x[1]的递增排序，即x[1]的递减
        for h, w in sorted(zip(height,weight),key = lambda x:[x[0],-x[1]]):
            loc = bisect_(longest, w)
            longest[loc:loc+1] = [w]
        return len(longest)