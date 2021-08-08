###############################################################################################
# 递归超时，有很多重复计算
###########
# 时间复杂度：O(3^n)
# 空间复杂度：O(logn)
###############################################################################################
class Solution:
    def tribonacci(self, n: int) -> int:
        def dfs(n):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            return dfs(n-1) + dfs(n-2) + dfs(n-3)
        return dfs(n)

# 数组优化
class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]
        for i in range(3, n+1):
            tri.append(tri[i-1] + tri[i-2] + tri[i-3])
        return tri[n]