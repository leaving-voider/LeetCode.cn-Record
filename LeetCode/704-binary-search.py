###############################################################################################
# 最近的题都很基本
###########
# 时间复杂度：O(logn)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r+1)>>1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        return -1 if nums[l] - target else l