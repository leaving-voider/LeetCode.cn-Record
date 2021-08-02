###############################################################################################
# 经典区间dp，且其集合属性不同于一般的max min or 数量，而是True 和 False
# 所以以后考虑dp状态定义时，要根据具体的问题来看状态在什么情况能转移，我们就定义什么属性
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)
###############################################################################################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N, len_ = 1010, len(s)
        if len_ <= 1:
            return s
        dp = [[0]*N for _ in range(N)] # dp[i][j]: i到j之间是不是回文串；具体怎么定义这个，要看我们要求解问题的具体性质
        for i in range(len_):
            dp[i][i] = 1 # 只有一个就是自己，是回文

        begin, maxLen = 0, 1 # 初始化为第一个字母是最长回文
        for le in range(2, len_+1):
            for i in range(len_ - le + 1):
                l, r = i, i+le-1
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1] if l+1 <= r-1 else 1 # 当只有两个字符时，直接判是回文
                    if dp[l][r] and r - l + 1 > maxLen:
                        maxLen = r - l + 1
                        begin = l
        return s[begin:begin+maxLen]