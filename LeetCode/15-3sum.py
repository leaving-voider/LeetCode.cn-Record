###############################################################################################
# 排序后，两重循环，第一层定k，第二层双指针遍历i和j，用哈希降重
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(logn), 排序的栈消耗
###############################################################################################
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_ = len(nums)
        nums.sort()

        res = set()
        for k in range(len_):
            i, j, sum_ = 0, len_-1, -nums[k]
            while i<j:
                if i >= k or j <= k: # 肯定在两边，超过就break，避免重复
                    break
                now = nums[i] + nums[j]
                if now == sum_:
                    res.add((nums[i], nums[j], nums[k]))
                
                if now >= sum_:
                    j -= 1
                else:
                    i += 1
        return list(res)