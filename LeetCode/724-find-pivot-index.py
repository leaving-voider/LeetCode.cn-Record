################################################################
# 对官方给的方法学习后，发现比我的方法快很多，因为避免了很多重复计算
################################################################
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        # 记录当前index左边的和
        sum_ = 0
        for i in range(len(nums)):
            # 这个公式的意思就是，只有当左边和右边相等都为sum_时，这个等式才可能成立
            if 2*sum_ + nums[i] == total:
                return i
            # 一次遍历，走一个加一个，避免了切片，且不用重复计算sum值
            sum_ += nums[i]
        return -1

# ################################################################
# # 我的方法一次遍历，大量使用了切片，且重复计算了很多sum，导致速度较慢
# ################################################################
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         length = len(nums)
#         for i in range(length):
#             if i == 0 and sum(nums[1:]) == 0:
#                 return 0
#             elif i == (length-1) and sum(nums[:-1]) == 0:
#                 return length - 1
#             else:
#                 if sum(nums[:i]) == sum(nums[i+1:]):
#                     return i
#         return -1