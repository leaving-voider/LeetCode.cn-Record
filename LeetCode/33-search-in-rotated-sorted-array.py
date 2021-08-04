###############################################################################################
# 利用本题中所谓的【旋转】的定义，使用二分求解
###########
# 时间复杂度：O(logn)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        len_ = len(nums)
        l, r = 0, len_-1
        while l < r:
            mid = (l+r+1)>>1
            if nums[mid] >= nums[0]: # 因为nums[0]严格大于每个右边的递增序列
                l = mid
            else:
                r = mid - 1
        pivot = l
        l, r = 0, pivot
        while l < r:
            mid = (l+r)>>1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[r] == target:
            return r
        l, r = pivot, len_-1
        while l < r:
            mid = (l+r+1)>>1
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        if nums[l] == target:
            return l
        return -1