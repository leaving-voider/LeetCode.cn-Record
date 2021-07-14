###############################################################################################
# 自己写的，时间超过100%的人
# 哈希+一次遍历；比官方的还好，我采用哈希表找到最合适替换值，而官方采用二分，需要排序
###########
# 时间复杂度：O(n)，一次遍历
# 空间复杂度：O(n)，哈希表
###############################################################################################
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        hash_ = set(nums1) # 把所有nums1的数加进去
        diffs = 0 # 计算原本的绝对差值和
        global_optimize = 0 # 查到最多能减少的值

        for i in range(len(nums1)):
            cur_diff = abs(nums1[i] - nums2[i]) # 当前nums1[i] 和 nums2[i]的差值
            if cur_diff > global_optimize: # 只有当前差值大于前面所找到的最大优化值，才有可能更加优化
                # 从0到cur_diff - global_optimize -1挨个找能不能有可替换的数在nums1中
                # 当 j >=了cur_diff - global_optimize，cur_diff - j就不可能再大于global_optimize
                for j in range(cur_diff - global_optimize): 
                    if nums2[i] + j in hash_ or nums2[i] - j in hash_:
                        if cur_diff - j > global_optimize:
                            global_optimize = cur_diff - j # 记下能减少的最多的值
                        break
            diffs += cur_diff # 依次加上差值
        return (diffs - global_optimize)%(int(1e9)+7)
