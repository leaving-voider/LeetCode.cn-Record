###############################################################################################
# 纯数学推导减小遍历范围，并在O(1)复杂度内求出k
# 如果不会数学推导，那只能超时
###########
# 时间复杂度：O((log2n)^2)，遍历 O(logn) 次m值(位数)，检查该位数下求得的k对不对，检查的时间复杂度为 O(logn)
# 空间复杂度：O(1)
###############################################################################################
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        int_ = int(n)
        for bitsNum in range(int(log(int_, 2)), 1, -1):
            k = int(int_ ** (1/bitsNum))
            if sum([k**i for i in range(bitsNum+1)]) == int_:
                return str(k)
        return str(int_-1)