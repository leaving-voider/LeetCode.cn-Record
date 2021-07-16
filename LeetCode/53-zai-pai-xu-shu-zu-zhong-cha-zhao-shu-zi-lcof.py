###############################################################################################
# 很基础，直接二分
###########
# 时间复杂度：O(logn)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)>>1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            left = l
            l, r = 0, len(nums)-1
            while l < r:
                mid = (l+r+1)>>1
                if nums[mid] <= target:
                    l = mid
                else:
                    r = mid - 1
            return l - left + 1
        return 0