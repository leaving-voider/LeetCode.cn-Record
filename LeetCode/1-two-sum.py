###############################################################################################
# 排序 + 哈希查找
###########
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = defaultdict(list)
        for i in range(len(nums)):
            dict_[nums[i]].append(i)
        nums.sort()
        i, j = 0, len(nums) - 1
        while nums[i] + nums[j] != target:
            if nums[i] + nums[j] > target:
                j -= 1
            if nums[i] + nums[j] < target:
                i += 1
        if nums[i] == nums[j]: # 可能有元素一样，则不能用同一个
            return [dict_[nums[i]][0], dict_[nums[j]][1]]
        return [dict_[nums[i]][0], dict_[nums[j]][0]]