###############################################################################################
# 排序 + 遍历比较
# 本来想动规，发现太难转移了
###########
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        begin = end = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if begin == -1:
                    begin = i 
                else:
                    end = i 
        if begin == -1:
            return 0
        return end - begin + 1