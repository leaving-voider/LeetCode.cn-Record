###############################################################################################
# 题目类似01背包问题，不过背包的维度有两个：物品和容量，而该题有三个：字符串、0的容量、1的容量
# 因此需要三维动态规划数组
###########
# 时间复杂度：O(lmn+L)，遍历一次三维数组，L为所有字符串的长度，需要遍历一次求0和1的个数
# 空间复杂度：O(lmn)
###############################################################################################
class Solution:
    def getNumOf01(self, string):
        zeros = ones = 0
        for letter in string:
            if letter == "0":
                zeros += 1
            else:
                ones += 1
        return zeros, ones
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        len_ = len(strs)
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(len_+1)]
        for i in range(1, len_+1): # 前i个字符串
            num0, num1 = self.getNumOf01(strs[i-1])
            for j in range(m+1): # 容量j个0
                for k in range(n+1): # 容量k个1
                    dp[i][j][k] = dp[i-1][j][k] if (j<num0 or k<num1) else max(dp[i-1][j][k], dp[i-1][j-num0][k-num1]+1)
        return dp[len_][m][n]


###############################################################################################
# 因为dp[i][j][k]的状态只和dp[i-1]维度有关，因此可以采用【滚动数组】，空间复杂度优化为二维数组
# 又因为新的dp[j][k]的状态只可能和旧的dp[j][k]或旧的dp[j-num0][k-num1]有关，因此j、k循环采用【倒序】
# 又因为当j和k分别小于num0和num1时，新的dp[j][k]就等于旧的dp[j][k]，相当于没变，因此减少j、k【循环范围】
###########
# 时间复杂度：O(lmn+L)，遍历一次三维数组，L为所有字符串的长度，需要遍历一次求0和1的个数
# 空间复杂度：O(mn)
###############################################################################################
class Solution:
    def getNumOf01(self, string):
        zeros = ones = 0
        for letter in string:
            if letter == "0":
                zeros += 1
            else:
                ones += 1
        return zeros, ones
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        len_ = len(strs)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] # 优化为二维数组
        for i in range(1, len_+1): # 前i个字符串
            num0, num1 = self.getNumOf01(strs[i-1])
            for j in range(m,num0-1,-1): # 容量j个0
                for k in range(n,num1-1,-1): # 容量k个1
                    dp[j][k] = max(dp[j][k], dp[j-num0][k-num1]+1)
        return dp[m][n]