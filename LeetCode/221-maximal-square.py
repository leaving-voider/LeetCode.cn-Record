###############################################################################################
# 利用矩阵前缀和，如果一个正方形里全是1，则和肯定是边长的平方
# 然后利用二分来查找可能的最大边长
###########
# 时间复杂度：O((n^2)*logn)，n^2是为了找某个宽度下所有的正方形
# 空间复杂度：O(n^2)
###############################################################################################
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N, r, c = 310, len(matrix), len(matrix[0])
        sums = [[0]*N for _ in range(N)]

        for i in range(r):
            for j in range(c):
                sums[i+1][j+1] = sums[i][j+1] + sums[i+1][j] - sums[i][j] + int(matrix[i][j])
        
        def getArea(x1,y1,x2,y2):
            return sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1]

        max_area = 0
        i, j = 1, min(r, c)
        while i <= j:
            w = (i+j)>>1 # 这就是要尝试的正方形宽度w
            area = w*w
            for a in range(w, r+1):
                for b in range(w, c+1):
                    if getArea(a-w+1,b-w+1,a,b) == area:
                        max_area = max(area, max_area)
            if max_area == area: # 说明面积可能更大
                i = w+1
            else:
                j = w-1
        return max_area

# 动规，时间复杂度降到O(n^2)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N, r, c = 310, len(matrix), len(matrix[0])
        
        res = 0 # 记录遇到的最大的边长
        dp = [[0]*N for _ in range(N)] # dp[i][j]: 以i、j结尾的最大正方形边长
        for i in range(r):
            if int(matrix[i][0]):
                dp[i][0] = res = 1
        for i in range(c):
            if int(matrix[0][i]):
                dp[0][i] = res = 1

        for i in range(1, r):
            for j in range(1, c):
                if int(matrix[i][j]):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
        return res*res # 返回面积