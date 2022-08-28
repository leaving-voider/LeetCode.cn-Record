###############################################################################################
# 参考官方方法，此方法是在C++ 的标准库函数 next_permutation 中被采用的方法
###########
# 时间复杂度：O(n), n为数组长，最多扫描两次，反转一次
# 空间复杂度：O(1)，常数消耗
###############################################################################################
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 找【较小，较大】组合：
        # 较小数尽可能右，较大数尽可能小（保证变大的幅度尽可能小）
        i = len(nums) - 2
        while i>=0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0: # 说明找到了较小数
            j = len(nums) - 1
            while i <= j and nums[i] >= nums[j]: # 一定能找到这个较大数
                j -= 1
            nums[i], nums[j] = nums[j], nums[i] # 交换
        
        # 双指针反转
        left, right = i+1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# 带英文注释
class Solution:
    def nextPermutation(self, s: List[int]) -> None:
        # step 1: find the smaller one that should be at as right as possible
        i = len(s) - 2
        while i>=0 and s[i] >= s[i+1]:
            i -= 1

        # step 2: if the smaller one is found
        if i >= 0:
            # find the larger one that should be as small as possible and be at the right of the smaller one
            j = len(s) - 1
            # the larger one must be found
            while i <= j and s[i] >= s[j]:
                j -= 1
            # step 3: exchange then we get the next permutation
            s[i], s[j] = s[j], s[i]

        # step 4: the numbers in range of [i+1, len(s) - 1] is in large-to-small
        # we inverse it to get the next smallest permutation (still than prev one)
        left, right = i+1, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
