###############################################################################################
# 利用了【560. 和为K的子数组】的前缀和+哈希表方法，快速计算子数组和为k的个数
# 这样仅需要遍历所有的上下边界组合，然后依次对其中间的列进行求和，即可使用【560. 和为K的子数组】的方法
###########
# 时间复杂度：O(m²*n)，其中 m 和 n 分别是矩阵 matrix 的行数和列数，subArraySum时间复杂度只为O(n)
# 空间复杂度：O(n)，哈希表的空间消耗
###############################################################################################
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subArraySum(nums, k):
            res = sum_ = 0
            counter = Counter([0]) # 哈希表作用, 为了当sum-k = 0即sum_ 等于k时，有最初的一个1可以加上
            for num in nums:
                sum_ += num
                res += counter[sum_ - k]
                counter[sum_] += 1
            return res
        
        row, column = len(matrix), len(matrix[0])
        res = 0
        for i in range(row): # 枚举上边界
            sum_ = [0]*column
            for j in range(i, row): # 枚举下边界
                for c in range(column): # 计算边界内每一列的和
                    sum_[c] += matrix[j][c]
                res += subArraySum(sum_, target)
        return res