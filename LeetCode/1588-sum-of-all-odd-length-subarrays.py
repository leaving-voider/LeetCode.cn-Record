###############################################################################################
# 确实简单，基本前缀和，遍历不同长度即可
###########
# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
###############################################################################################
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_sum = [0]
        for per in arr:
            arr_sum.append(per + arr_sum[-1])
        res, len_ = 0, len(arr)
        for i in range(1, len_+1, 2):
            for j in range(i, len_+1):
                res += arr_sum[j] - arr_sum[j-i]
        return res

# 下面这种更快，因为利用了一点规律
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_sum = [0]
        for per in arr:
            arr_sum.append(per + arr_sum[-1])
        res, len_ = 0, len(arr)
        for i in range(1, len_+1, 2):
            for j in range(i):
                res += arr_sum[len_-j] - arr_sum[j]
        return res

# 利用规律，一次遍历！奇数层就加上到ji变量，偶数层就加到ou变量
# 每次到奇数层的时候，统一加上所有前面的层
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        arr_sum = [0]
        for per in arr:
            arr_sum.append(per + arr_sum[-1])
        res, len_ = 0, len(arr)
        ou = ji = 0
        for i in range(len_):
            if i % 2:
                ou += arr_sum[len_-i] - arr_sum[i]
            else:
                ji += arr_sum[len_-i] - arr_sum[i]
                res += ji + ou
        return res