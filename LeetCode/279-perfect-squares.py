###############################################################################################
# 同样用动规的思想去解，居然超时了没想到
###########
# 时间复杂度：O(n*sqrt(n)*total)，total为总数/平方和
# 空间复杂度：O(n*sqrt(n))，动规数组开销
###############################################################################################
class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_ = int(sqrt(n))
        # 定义dp[i][j]：任意使用≤i的自然数的完全平方，组成和为j，使用的完全平方数的最少数量
        dp = [[0]*(n+1) for _ in range(sqrt_+1)]
        for i in range(1, sqrt_+1):
            dp[i][1] = 1
        for i in range(1, n+1):
            dp[1][i] = i
        for i in range(2, sqrt_+1):
            square = i**2
            for j in range(2, n+1):
                if square > j: # 没法使用这个square
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min([dp[i-1][j-per*square]+per for per in range(j//square+1)])
        return dp[sqrt_][n]

## 使用滚动数组，稍微化简后如下，但还是超时
class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_ = int(sqrt(n))
        # 定义dp[i][j]：任意使用≤i的自然数的完全平方，组成和为j，使用的完全平方数的最少数量
        dp = [0]*(n+1) # 直接从第1层开始
        for i in range(1, n+1):
            dp[i] = i
        
        for i in range(2, sqrt_+1):
            square = i**2
            for j in range(n, square-1, -1):
                dp[j] = min([dp[j-per*square]+per for per in range(j//square+1)])
        return dp[n]


###############################################################################################
# 继续化简，去掉第三重循环，只需要从小到大遍历每一个dp[j]的时候，和前面的dp[j-square]取min即可
# 至此，成功没看官方解法，解出此题，看来我对动规算法已经稍稍入门了
###########
# 时间复杂度：O(n*sqrt(n))
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def numSquares(self, n: int) -> int:
        # 定义dp[i][j]：任意使用≤i的自然数的完全平方，组成和为j，使用的完全平方数的最少数量
        dp = list(range(n+1)) # 直接从第1层开始
        for i in range(2, int(sqrt(n))+1):
            square = i**2
            for j in range(square, n+1):
                dp[j] = min(dp[j], dp[j-square]+1)
        return dp[n]


###############################################################################################
# 官方竟然给出了一个基于数学的定理【四平方和定理】，直接代替本题的动规法；仅判断四种情况即可
###########
# 时间复杂度：O(sqrt(n)), 判断能否被 4 整除的while循环的时间复杂度为 O(logn)，忽略
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    # 判断是否为完全平方数
    def isPerfectSquare(self, x):
        y = int(sqrt(x))
        return y * y == x

    # 判断是否能表示为 4^k*(8m+7)
    def checkAnswer4(self, x):
        while (x % 4 == 0):
            x /= 4
        return x % 8 == 7

    def numSquares(self, n: int) -> int:
        if self.isPerfectSquare(n): # 判断是否为完全平方数
            return 1
        if self.checkAnswer4(n): # 判断是否能表示为 4^k*(8m+7)
            return 4
        for i in range(1, int(sqrt(n))+1):
            if (self.isPerfectSquare(n - i**2)):
                return 2
        return 3