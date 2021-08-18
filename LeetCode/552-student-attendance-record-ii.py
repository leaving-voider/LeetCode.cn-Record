###############################################################################################
# dfs超时
###########
# 时间复杂度：O(3^n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def checkRecord(self, n: int) -> int:
        res = 0
        def dfs(a, l, p, t):
            nonlocal res
            if a > 1: # a记录缺勤总数
                return
            if l > 2: # l记录连续的晚到数
                return
            if t == n:
                res += 1
                return 
            dfs(a+1, 0, p, t+1) # 缺勤,晚到归0
            dfs(a, l+1, p, t+1) # 晚到
            dfs(a, 0, p+1, t+1) # 出勤,晚到归0
        dfs(0,0,0,0)
        return res

###############################################################################################
# 由dfs变化出记忆化搜索，免除了很多重复计算，不过还是超时
###########
# 时间复杂度：O(3*n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [defaultdict(lambda : -1) for _ in range(n+1)] # dp[i][(a,l,p)]: 到第i天记录为(a,l,p)时，能得到奖学金的的方案数
        MOD = int(1e9+7)
        def dfs(a, l, p, t):
            if a > 1: # a记录缺勤总数
                return 0
            if l > 2: # l记录连续的晚到数
                return 0
            if t == n:
                return 1
            for i, j, k in [(a+1,0,p), (a,l+1,p), (a,0,p+1)]: # 缺勤,晚到,出勤
                if dp[t+1][(i, j, k)] == -1:
                    dp[t+1][(i, j, k)] = dfs(i, j, k, t+1) % MOD
            return (dp[t+1][(a+1,0,p)] + dp[t+1][(a,l+1,p)] + dp[t+1][(a,0,p+1)]) % MOD
        return dfs(0,0,0,0)

# 换了一种写法，快了一些，但还是超时
class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)] # dp[i][j][k]: 第i天时缺勤j次，连续迟到k次的情况下，能获得奖学金的可能数
        MOD = int(1e9+7)
        def dfs(a, l, p, t):
            if t == n:
                return 1
            if dp[t][a][l]:
                return dp[t][a][l]
            dp[t+1][a][0] = dfs(a, 0, p+1, t+1) % MOD # 下一天出勤
            res = dp[t+1][a][0]
            if a < 1: # 还可以缺勤
                dp[t+1][1][0] = dfs(1, 0, p, t+1) % MOD
                res += dp[t+1][1][0]
            if l < 2: # 还可以迟到
                dp[t+1][a][l+1] = dfs(a, l+1, p, t+1) % MOD
                res += dp[t+1][a][l+1]
            return res % MOD
        return dfs(0,0,0,0)

###############################################################################################
# 真的气死，只好换成循环式DP
###########
# 时间复杂度：O(n)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)] # dp[i][j][k]: 第i天时缺勤j次，连续迟到k次的情况下，能获得奖学金的可能数
        dp[0][0][0] = 1 # 第0天（即还没有任何记录），缺勤0次，迟到0次，可以获得奖学金，所以初始化为1
        MOD = int(1e9+7)
        for i in range(1, n+1):
            # 出勤
            dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2]) % MOD # 前一天的连续迟到为0、1、2都可以
            dp[i][1][0] = (dp[i-1][1][0] + dp[i-1][1][1] + dp[i-1][1][2]) % MOD
            # 迟到
            dp[i][0][1] = dp[i-1][0][0] # 前一天的连续迟到为0
            dp[i][0][2] = dp[i-1][0][1] # 前一天的连续迟到为1
            dp[i][1][1] = dp[i-1][1][0] # 前一天的连续迟到为0
            dp[i][1][2] = dp[i-1][1][1] # 前一天的连续迟到为1
            # 缺席
            dp[i][1][0] += dp[i-1][0][0] + dp[i-1][0][1] + dp[i-1][0][2] # 这里要+=，免得把前面计算出勤的给覆盖了
        res = 0
        for j in range(2):
            for k in range(3):
                res = (res + dp[n][j][k]) % MOD
        return res

# 滚动数组
class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[0]*3 for _ in range(2)] # dp[j][k]: 前一天缺勤j次，连续迟到k次的情况下，能获得奖学金的可能数
        dp[0][0] = 1 # 第0天（即还没有任何记录），缺勤0次，迟到0次，可以获得奖学金，所以初始化为1
        MOD = int(1e9+7)
        for i in range(1, n+1):
            newdp = [[0]*3 for _ in range(2)]
            # 出勤
            newdp[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD # 前一天的连续迟到为0、1、2都可以
            newdp[1][0] = (dp[1][0] + dp[1][1] + dp[1][2] + dp[0][0] + dp[0][1] + dp[0][2]) % MOD # 出勤 + 缺席
            # 迟到
            newdp[0][1] = dp[0][0] # 前一天的连续迟到为0
            newdp[0][2] = dp[0][1] # 前一天的连续迟到为1
            newdp[1][1] = dp[1][0] # 前一天的连续迟到为0
            newdp[1][2] = dp[1][1] # 前一天的连续迟到为1
            dp = newdp
        res = 0
        for j in range(2):
            for k in range(3):
                res = (res + newdp[j][k]) % MOD
        return res

# dp数组很小，直接二维降一维
class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [0]*6 # dp[0], dp[1], dp[2], dp[3], dp[4], dp[5] 分别代表之前的dp[0][0], dp[0][1], dp[0][2], dp[1][0], dp[1][1], dp[1][2]
        dp[0] = 1 # 第0天（即还没有任何记录），缺勤0次，迟到0次，可以获得奖学金，所以初始化为1
        MOD = int(1e9+7)
        for i in range(1, n+1):
            newdp = [0]*6
            # 出勤
            newdp[0] = (dp[0] + dp[1] + dp[2]) % MOD # 前一天的连续迟到为0、1、2都可以
            newdp[3] = (dp[3] + dp[4] + dp[5] + dp[0] + dp[1] + dp[2]) % MOD # 出勤 + 缺席
            # 迟到
            newdp[1] = dp[0] # 前一天的连续迟到为0
            newdp[2] = dp[1] # 前一天的连续迟到为1
            newdp[4] = dp[3] # 前一天的连续迟到为0
            newdp[5] = dp[4] # 前一天的连续迟到为1
            dp = newdp
        return sum(newdp) % MOD

###############################################################################################
# 矩阵快速幂，利用上面最后一维数组计算，得出dp[n] = dp[0] * mat^n，这个mat就是一个矩阵
# 因此可以用基于快速幂的方法在logn的时间复杂度内计算完成
###########
# 时间复杂度：O(logn)
# 空间复杂度：O(1), 常数级别的开销
###############################################################################################
class Solution:
    def checkRecord(self, n: int) -> int:
        mat = [
            [1, 1, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 0],
        ]
        MOD = int(1e9+7)
        def mat_multiply(a, b): # 保证输入矩阵能够相乘
            r, c, mid = len(a), len(b[0]), len(a[0])
            ret = [[0]*c for _ in range(r)]
            for i in range(r):
                for j in range(c):
                    ret[i][j] = sum([a[i][k]*b[k][j] for k in range(mid)]) % MOD
            return ret

        def mat_qmi(a, k):
            res = [[1, 0, 0, 0, 0, 0]] # 前面解法中的初始值dp[0]
            while k:
                if k&1:
                    res = mat_multiply(res, a)
                k >>= 1
                a = mat_multiply(a, a)
            return res
        return sum(mat_qmi(mat, n)[0]) % MOD