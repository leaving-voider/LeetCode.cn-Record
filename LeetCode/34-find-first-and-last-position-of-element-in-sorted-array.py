###############################################################################################
# 经典二分
###########
# 时间复杂度：O(logn)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        len_ = len(nums)
        if not len_:
            return [-1, -1]
        l, r = 0, len_-1
        while l < r:
            mid = (l+r)>>1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        
        if nums[l] != target:
            return [-1, -1]
        else:
            res = [l]
            l, r = 0, len_-1
            while l < r:
                mid = (l+r+1)>>1
                if nums[mid] <= target:
                    l = mid
                else:
                    r = mid - 1
            res.append(l)
        return res