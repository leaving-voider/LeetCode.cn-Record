###############################################################################################
# 一遍遍历
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        start = res = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                res += i - start - 1 # 和前面start后每一个开头都能组成arithmetic
            else:
                start = i - 1
        return res