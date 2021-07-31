###############################################################################################
# 排序后，分析 + 枚举
###########
# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = float("inf")
        # 前3
        res = min(res, nums[-1] - nums[3])
        # 后3
        res = min(res, nums[-4] - nums[0])
        # 前2后1
        res = min(res, nums[-2] - nums[2])
        # 前1后2
        res = min(res, nums[-3] - nums[1])
        return res