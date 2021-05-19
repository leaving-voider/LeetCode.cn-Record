###############################################################################################
# 自己写的，首次直接100%超过所有人，没再参考官方方法，基本思想已写入题解，链接如下
# https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value/solution/python3chao-duan-dai-ma-yong-shi-chao-gu-833c/
###########
# 时间复杂度：O(mn)，即遍历一次整个矩阵
# 空间复杂度：O(mn)，max2min存储所有计算值的开销
###############################################################################################
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix[0]) # 横
        # matrixXOR中(i)处x的值为matrix[某行][i]以上的全部值的XOR，然后遍历每行
        max2min, matrixXOR = [], [0]*n
        for i in range(len(matrix)):
            XORacc = 0
            for j in range(n):
                matrixXOR[j]^=matrix[i][j] # 更新matrixXOR
                XORacc = XORacc^matrixXOR[j]
                max2min.append(XORacc)
        
        return sorted(max2min, reverse=True)[k-1]