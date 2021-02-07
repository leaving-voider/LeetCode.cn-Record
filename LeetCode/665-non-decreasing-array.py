###############################################################################################
# 官方给的一次遍历方法
############
# 时间复杂度：O(n), n为数组长度
# 空间复杂度：O(1), 只需要存一个outlier，表示这是第几个nums[i] > nums[i+1]，如果多于一次，直接False
###############################################################################################
class Solution:
    def checkPossibility(self, nums) -> bool:
        outlier = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                outlier += 1
                if outlier >= 2:
                    return False
                # 这种情况下，把nums[i]改成nums[i+1]才不会打乱之前的递增顺序
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        return True

###############################################################################################
# 我的方法很简单，直接遍历，但时间和空间消耗都很大
###############################################################################################
# class Solution:
#     def checkPossibility(self, nums) -> bool:
#         if len(set(nums)) == 1:
#             return True
#         forward_离群点 = 0
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] > nums[j]:
#                     forward_离群点 += 1
#                     break
#         backward_离群点 = 0
#         for i in range(len(nums)-1, 0, -1):
#             for j in range(i-1, -1, -1):
#                 if nums[i] < nums[j]:
#                     backward_离群点 += 1
#                     break
#         if forward_离群点 <= 1 or backward_离群点 <= 1:
#             return True
#         print(forward_离群点, backward_离群点)
#         return False

