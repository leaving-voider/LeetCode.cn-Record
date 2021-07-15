###############################################################################################
# 排序后，遍历一遍完事了
###########
# 时间复杂度：O(nlogn)，排序消耗
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        for i in range(len(arr)):
            if arr[i] > i + 1:
                arr[i] = i + 1
            if i > 0 and arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]