###############################################################################################
# 经典最长公共子序列解法
###########
# 时间复杂度：O(mn)，对每个dp值进行计算
# 空间复杂度：O(mn)，dp数组消耗
###############################################################################################
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1) # 横排
        len2 = len(nums2) # 纵列
        # 动规，dp[i][j]为nums1[:i]与nums2[:j]最长公共子序列长度
        dp = [[0]*(len1+1) for _ in range(len2+1)]

        for i in range(1, len2+1):
            for j in range(1, len1+1):
                if nums1[j-1] == nums2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]