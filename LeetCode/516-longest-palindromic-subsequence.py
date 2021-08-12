###############################################################################################
# 还是常规题，和【5. 最长回文子串】不同在于【子串】和【子数组】是【连续】的，而【子序列】可以不连续
# 因此定义dp的方式就不一样，对于【子序列】可以定义长度，而【连续】的【子串】则用是否
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)
###############################################################################################
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N, len_ = len(s)+1, len(s)
        dp = [[0]*N for _ in range(N)] # dp[i][j]: i到j之间的回文序列长度
        for i in range(len_):
            dp[i][i] = 1
            if i < len_-1:
                dp[i][i+1] = 2 if s[i] == s[i+1] else 1
        for le in range(3, len_+1):
            for i in range(len_-le+1):
                l, r = i, i+le-1
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                else:
                    dp[l][r] = max(dp[l][r-1], dp[l+1][r], dp[l+1][r-1]) # 其实dp[l+1][r-1]不需要，因为它是最短的，dp[l][r-1]或dp[l+1][r]都包含了此种情况
        return dp[0][len_-1]