###############################################################################################
# 参考官方的动规方法，主要思路是动规某处(i, j)的值表示第step步在第j个位置的方案数
# 在官方的基础上进一步优化了时间和空间复杂度
###########
# 时间复杂度：O(steps×min(arrLen,steps//2+1))
# 空间复杂度：O(steps×min(arrLen,steps//2+1))
###############################################################################################
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        # 优化，减少dp所占空间，并减少循环次数
        maxColumn = min(arrLen - 1, steps//2+1) # 官方用的steps，我进一步将其优化为steps//2+1

        # 该动规表示在第i个step到达数组第j个位置的方案数
        dp = [[0] * (maxColumn + 1) for _ in range(steps + 1)]
        dp[0][0] = 1

        for i in range(1, steps + 1): # 遍历每步
            for j in range(0, maxColumn + 1):
                dp[i][j] = dp[i - 1][j] # 上一个
                if j - 1 >= 0: # 左上
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod # 取模来减少下一步加法的计算量
                if j + 1 <= maxColumn: # 右上
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
        
        return dp[steps][0]

###############################################################################################
# 进一步优化空间复杂度，压缩dp为一维
###########
# 时间复杂度：O(steps×min(arrLen,steps//2+1))
# 空间复杂度：O(min(arrLen,steps//2+1))
###############################################################################################
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7
        # 进一步优化，减少dp所占空间，并减少循环次数
        maxColumn = min(arrLen - 1, steps//2+1) # 官方用的steps，我进一步将其优化为steps//2+1

        # 该动规表示在第i个step到达数组第j个位置的方案数
        dp = [0] * (maxColumn + 1)
        dp[0] = 1

        for i in range(1, steps + 1): # 遍历每步
            dpNext = [0] * (maxColumn + 1)
            for j in range(0, maxColumn + 1):
                dpNext[j] = dp[j] # 上一个
                if j - 1 >= 0: # 左上
                    dpNext[j] = (dpNext[j] + dp[j - 1]) % mod # 取模来减少下一步加法的计算量
                if j + 1 <= maxColumn: # 右上
                    dpNext[j] = (dpNext[j] + dp[j + 1]) % mod
            dp = dpNext
        return dp[0]

###############################################################################################
# 自己最初写的递归，但很快就超出时间限制了，未知能否通过所有测试
###############################################################################################
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # floor 从0开始，即第0步，floor为4表示第4步
        def dig(addr, floor):
            if floor == steps:
                if addr == 0:
                    yield 1
                return
            # 向左
            if addr > 0:
                yield from dig(addr-1, floor+1)
            # 不动
            yield from dig(addr, floor+1)
            # 向右
            if addr < arrLen-1:
                yield from dig(addr+1, floor+1)

        return len(list(dig(0, 0)))