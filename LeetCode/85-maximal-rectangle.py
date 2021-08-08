###############################################################################################
# 有点难，居然能拆分成【柱状图中最大矩形】来做，之前用于最大正方形的方法都不能用了，会严重超时
###########
# 时间复杂度：O(m*n)
# 空间复杂度：O(m*n)
###############################################################################################
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        if r == 0:
            return 0
        c = len(matrix[0])

        heights = [[0]*c for _ in range(r)]
        # 两个循环预处理每个点为基点的高度
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    heights[i][j] = heights[i-1][j] + 1 if i > 0 else 1
        res = 0
        for i in range(r): # 遍历每一层
            left, right, stack = [0]*c, [c]*c, [] # 类似【柱状图中最大的矩形】，预处理左右两边第一个比自己高度低的位置
            for j in range(c):
                while stack and heights[i][stack[-1]] >= heights[i][j]:
                    t = stack.pop()
                    right[t] = j
                left[j] = stack[-1] if stack else -1
                stack.append(j)
            
            # 预处理好后计算以该层为floor的最大矩形
            for j in range(c):
                res = max(res, (right[j]-left[j]-1)*heights[i][j])

        return res