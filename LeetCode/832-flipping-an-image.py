###############################################################################################
# 借鉴的方法有四种处理方式
# 情况一：A[i][left]=0,A[i][right]=0。对第 i 行进行水平翻转之后，A[i][left]=0,A[i][right]=0。进行反转之后，A[i][left]=1,A[i][right]=1。
# 情况二：A[i][left]=1,A[i][right]=1。对第 i 行进行水平翻转之后，A[i][left]=1,A[i][right]=1。进行反转之后，A[i][left]=0,A[i][right]=0。
# 情况三：A[i][left]=0,A[i][right]=1。对第 i 行进行水平翻转之后，A[i][left]=1,A[i][right]=0。进行反转之后，A[i][left]=0,A[i][right]=1。
# 情况四：A[i][left]=1,A[i][right]=0。对第 i 行进行水平翻转之后，A[i][left]=0,A[i][right]=1。进行反转之后，A[i][left]=1,A[i][right]=0。
###########
# 时间复杂度：O(n²)，其中 n 是矩阵边长，需要遍历矩阵一次
# 空间复杂度：O(1)，除了返回值以外，额外使用的空间为常数
###############################################################################################
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        for i in range(n):
            left, right = 0, n - 1
            while left < right:
                if A[i][left] == A[i][right]:
                    # 异或符号，和1取异或，即实现反转，0异或1为1，1异或1为0
                    A[i][left] ^= 1
                    A[i][right] ^= 1
                left += 1
                right -= 1
            # 处理奇数的情况
            if left == right:
                # 直接反转
                A[i][left] ^= 1
        return A

###############################################################################################
# 我采用使用numpy来处理，不过时间和空间消耗都挺大
###############################################################################################
import numpy as np
class Solution:
    def flipAndInvertImage(self, A):
        B = np.array(A)
        B[B==1] = -1
        B[B==0] = 1
        B[B==-1] = 0
        B = np.flip(B, 1)
        return B
